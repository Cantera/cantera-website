from nikola.plugin_categories import Task
from nikola.utils import get_logger, config_changed
from docutils import nodes
from docutils.readers.standalone import Reader
from docutils.core import Publisher
from copy import copy


class ProcessLabels(Task):
    """Find and process labels in reST files"""

    name = "process_labels"

    def set_site(self, site):
        self.site = site
        self.logger = get_logger(self.name)
        self.site.anon_ref_labels = {}
        self.site.ref_labels = {}
        # This attribute is set to True when the labels are being
        # processed to avoid spurious warnings about missing labels
        self.site.processing_labels = False
        return super(ProcessLabels, self).set_site(site)

    def gen_tasks(self):
        self.site.scan_posts()
        kw = {
            "translations": self.site.config["TRANSLATIONS"],
            "timeline": self.site.timeline,
        }
        self.tl_changed = False
        # Make sure that this task is created, even if nothing ends up needing to be done
        yield self.group_task()

        def tl_ch():
            self.tl_changed = True

        yield {
            'basename': self.name,
            'name': 'timeline_changes',
            'actions': [tl_ch],
            'uptodate': [config_changed({1: kw['timeline']})],
        }

        for lang in kw["translations"]:
            deps_dict = copy(kw)
            deps_dict.pop('timeline')
            for post in self.site.timeline:
                if not post.source_ext() == '.rst':
                    continue
                # self.logger.error('The post fragment is {}'.format(post.fragment_deps(lang)))
                targets = [p for p in post.fragment_deps(lang) if not p.startswith("####MAGIC####")]
                source = post.translated_source_path(lang)
                task = {
                    'basename': self.name,
                    'name': source,
                    'targets': targets,
                    'task_dep': ['process_labels:timeline_changes'],
                    'actions': [(process_labels, [self.site, self.logger, source, post, lang]),
                                (update_cache, [self.site]),
                                ],
                    'uptodate': [config_changed(deps_dict, 'process_labels')] +
                    post.fragment_deps_uptodate(lang),
                }
                yield task


def update_cache(site):
    cached_labels = site.cache.get('ref_labels')
    anon_cached_labels = site.cache.get('anon_ref_labels')
    if cached_labels is not None:
        cached_labels.update(site.ref_labels)
        site.cache.set('ref_labels', cached_labels)
    else:
        site.cache.set('ref_labels', site.ref_labels)

    if anon_cached_labels is not None:
        anon_cached_labels.update(site.anon_ref_labels)
        site.cache.set('anon_ref_labels', anon_cached_labels)
    else:
        site.cache.set('anon_ref_labels', site.anon_ref_labels)


def process_labels(site, logger, source, post, lang=None):
    site.processing_labels = True
    pub = Publisher(reader=Reader(), parser=None, writer=None)
    pub.set_components(None, 'restructuredtext', 'html')
    # Reading the file will generate output/errors that we don't care about
    # at this stage. The report_level = 5 means no output
    pub.process_programmatic_settings(
        settings_spec=None,
        settings_overrides={'report_level': 5},
        config_section=None,
    )
    pub.set_source(None, source)
    pub.publish()
    document = pub.document
    site.processing_labels = False

    # Code based on Sphinx std domain
    for name, is_explicit in document.nametypes.items():
        if not is_explicit:
            continue
        labelid = document.nameids[name]
        if labelid is None:
            continue
        node = document.ids[labelid]
        if node.tagname == 'target' and 'refid' in node:
            node = document.ids.get(node['refid'])
            labelid = node['names'][0]
        if node.tagname == 'footnote' or 'refuri' in node or node.tagname.startswith('desc_'):
            continue
        if name in site.ref_labels:
            logger.warn('Duplicate label {dup}, other instance in {other}'.format(
                dup=name, other=site.ref_labels[name][0]
            ))
        site.anon_ref_labels[name] = post.permalink(), labelid

        def clean_astext(node):
            """Like node.astext(), but ignore images.
            Taken from sphinx.util.nodes"""
            node = node.deepcopy()
            for img in node.traverse(nodes.image):
                img['alt'] = ''
            for raw in node.traverse(nodes.raw):
                raw.parent.remove(raw)
            return node.astext()

        if node.tagname in ('section', 'rubric'):
            sectname = clean_astext(node[0])
        else:
            continue
        site.ref_labels[name] = post.permalink(), labelid, sectname
