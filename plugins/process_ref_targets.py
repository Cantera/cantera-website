"""Find and process reference targets in reST files.

References in reST files can be in the form ``:ref:``.
This module processes labels in the form of

.. code:: rest

   .. labelname:

and stores the resulting page location and anchor tag for the
label. This information is stored in the ``site.ref_targets``
and ``site.anon_ref_targets` attributes.
"""
import tempfile
from copy import copy
from pathlib import Path

import requests
from docutils import nodes
from docutils.core import Publisher
from docutils.io import StringInput, StringOutput
from docutils.readers.standalone import Reader
from nikola.plugin_categories import Task
from nikola.utils import config_changed, get_logger

HERE = Path(__file__).parent


class ProcessRefTargets(Task):
    """Find and process targets in reST files."""

    name = "process_ref_targets"

    def set_site(self, site):
        """Set the Nikola site instance for this plugin."""
        self.site = site
        self.logger = get_logger(self.name)
        self.site.anon_ref_targets = {}
        self.site.ref_targets = {}
        # This attribute is set to True when the targets are being
        # processed to avoid spurious warnings about missing targets
        self.site.processing_targets = False

        # Ensure that this Task is run before the posts are rendered
        # We need to enforce this order because rendering the posts
        # requires the targets that we generate here
        self.inject_dependency("render_posts", self.name)

        return super(ProcessRefTargets, self).set_site(site)

    def gen_tasks(self):
        """Generate the set of processing tasks."""
        self.site.scan_posts()
        kw = {
            "translations": self.site.config["TRANSLATIONS"],
            "timeline": self.site.timeline,
        }
        self.tl_changed = False
        # Ensure that this task is created, even if nothing needs to be done
        yield self.group_task()

        def tl_ch():
            self.tl_changed = True

        yield {
            "basename": self.name,
            "name": "timeline_changes",
            "actions": [tl_ch],
            "uptodate": [config_changed({1: kw["timeline"]})],
        }

        for lang in kw["translations"]:
            deps_dict = copy(kw)
            deps_dict.pop("timeline")
            for post in self.site.timeline:
                if not post.source_ext() == ".rst":
                    continue
                source = post.translated_source_path(lang)
                task = {
                    "basename": self.name,
                    "name": source,
                    "task_dep": ["process_ref_targets:timeline_changes"],
                    "actions": [
                        (
                            process_targets,
                            [self.site, self.logger, source, post.permalink()],
                        ),
                        (update_cache, [self.site]),
                    ],
                }
                yield task

        # These are YAML API docs. They are parsed here because they aren't
        # the typical Sphinx-generated documentation for functions and
        # classes, most of the text is broken out into sections with ref
        # targets.
        cantera_version = self.site.config["CANTERA_VERSION"]
        yaml_rst_path = f"api-docs/docs-{cantera_version}/sphinx/html/_sources/yaml"
        for rest_file in Path(yaml_rst_path).glob("**/*.rst.txt"):
            stem = rest_file.name.split(".")[0]
            permalink = (
                f"/documentation/docs-{cantera_version}"
                f"/sphinx/html/yaml/{stem}.html"
            )
            yield {
                "basename": self.name,
                "name": str(rest_file),
                "task_dep": ["process_ref_targets:timeline_changes"],
                "actions": [
                    (
                        process_targets,
                        [self.site, self.logger, str(rest_file), permalink],
                    ),
                    (update_cache, [self.site]),
                ],
            }


def update_cache(site):
    """Update the Nikola build cache."""
    cached_targets = site.cache.get("ref_targets")
    anon_cached_targets = site.cache.get("anon_ref_targets")
    if cached_targets is not None:
        cached_targets.update(site.ref_targets)
        site.cache.set("ref_targets", cached_targets)
    else:
        site.cache.set("ref_targets", site.ref_targets)

    if anon_cached_targets is not None:
        anon_cached_targets.update(site.anon_ref_targets)
        site.cache.set("anon_ref_targets", anon_cached_targets)
    else:
        site.cache.set("anon_ref_targets", site.anon_ref_targets)


def process_targets(site, logger, source, permalink):
    """Process the target locations in the reST files."""
    site.processing_targets = True
    reader = Reader()
    reader.l_settings = {"source": source}
    with open(source, "r", encoding="utf8") as in_file:
        data = in_file.read()
    pub = Publisher(
        reader=reader,
        parser=None,
        writer=None,
        settings=None,
        source_class=StringInput,
        destination_class=StringOutput,
    )
    pub.set_components(None, "restructuredtext", "html")
    # Reading the file will generate output/errors that we don't care about
    # at this stage. The report_level = 5 means no output
    pub.process_programmatic_settings(
        settings_spec=None, settings_overrides={"report_level": 5}, config_section=None
    )
    pub.set_source(data, None)
    pub.set_destination(None, None)
    pub.publish()
    document = pub.document
    site.processing_targets = False

    # Code based on Sphinx std domain
    for name, is_explicit in document.nametypes.items():
        if not is_explicit:
            continue
        labelid = document.nameids[name]
        if labelid is None:
            continue
        node = document.ids[labelid]
        if node.tagname == "target" and "refid" in node:
            node = document.ids.get(node["refid"])
            labelid = node["names"][0]
        if (
            node.tagname == "footnote"
            or "refuri" in node
            or node.tagname.startswith("desc_")
        ):
            continue
        if name in site.ref_targets:
            logger.warn(
                "Duplicate label {dup}, other instance in {other}".format(
                    dup=name, other=site.ref_targets[name][0]
                )
            )
        site.anon_ref_targets[name] = permalink, labelid

        def clean_astext(node):
            """Like node.astext(), but ignore images.

            Taken from sphinx.util.nodes
            """
            node = node.deepcopy()
            for img in node.traverse(nodes.image):
                img["alt"] = ""
            for raw in node.traverse(nodes.raw):
                raw.parent.remove(raw)
            return node.astext()

        if node.tagname in ("section", "rubric"):
            sectname = clean_astext(node[0])
        else:
            continue
        site.ref_targets[name] = permalink, labelid, sectname
