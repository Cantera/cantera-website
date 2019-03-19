"""Build the examples from the Cantera repository into Nikola listings.

This plugin finds the Cantera examples directory in the Cantera repository
to process the examples into nicely formatted HTML along the lines of
Nikola listings. The Cantera examples are found in the ``EXAMPLES_FOLDERS``
configuration option from the top-level config.py.
"""
from pathlib import Path
import re
import base64
import mimetypes

from collections import OrderedDict
import lxml.html
import json

from nikola.plugin_categories import Task
from nikola import utils
import natsort


def render_example_index(site, kw, headers, output_file):
    n = 3
    for head_dict in headers.values():
        head_files = head_dict["files"]
        head_dict["files"] = [
            head_files[i : i + n] for i in range(0, len(head_files), n)
        ]

    permalink = output_file.relative_to(kw["output_folder"])
    title = "Jupyter Examples"
    context = {
        "headers": headers,
        "lang": kw["default_lang"],
        "pagekind": ["example"],
        "permalink": str(permalink),
        "title": title,
        "description": title,
    }
    site.render_template("jupyter-example-index.tmpl", str(output_file), context)


def render_example(site, kw, in_name, out_name):
    ipynb_compiler = site.plugin_manager.getPluginByName(
        "ipynb", "PageCompiler"
    ).plugin_object
    with in_name.open(mode="r") as in_file:
        nb_json = ipynb_compiler._nbformat_read(in_file)
    ipynb_raw = ipynb_compiler._compile_string(nb_json)
    ipynb_html = lxml.html.fromstring(ipynb_raw)
    code = lxml.html.tostring(ipynb_html, encoding="unicode")

    title = in_name.name

    permalink = out_name.relative_to(kw["output_folder"])
    source_link = permalink.stem  # remove '.html'
    context = {
        "code": code,
        "title": title,
        "permalink": str(permalink),
        "lang": kw["default_lang"],
        "description": title,
        "source_link": source_link,
        "pagekind": ["example"],
        "needs_ipython_css": True,
    }
    site.render_template("examples.tmpl", str(out_name), context)


class RenderJupyterExamples(Task):

    name = "render_jupyter_examples"

    def set_site(self, site):
        """Set Nikola site."""
        # Verify that a Python output folder appears only once in EXAMPLES_FOLDERS
        found_jupyter = False
        for source, dest in site.config["EXAMPLES_FOLDERS"].items():
            if "jupyter" in dest:
                if found_jupyter:
                    self.logger.error(
                        "More than one folder to output Jupyter examples was found in EXAMPLES_FOLDERS, exiting"
                    )
                else:
                    found_jupyter = True
                    self.input_folder = source
                    self.examples_folder = dest

        if not found_jupyter:
            self.logger.warn(
                "Didn't find an output folder for Jupyter examples in EXAMPLES_FOLDERS"
            )

        return super().set_site(site)

    def gen_tasks(self):
        """Render examples."""
        kw = {
            "default_lang": self.site.config["DEFAULT_LANG"],
            "examples_folders": self.site.config["EXAMPLES_FOLDERS"],
            "output_folder": Path(self.site.config["OUTPUT_FOLDER"]),
            "index_file": self.site.config["INDEX_FILE"],
            "strip_indexes": self.site.config["STRIP_INDEXES"],
            "cache_folder": Path(self.site.config["CACHE_FOLDER"]),
        }

        yield self.group_task()

        # When any key or value in the uptodate dictionary changes, the
        # examples pages need to be rebuilt.
        uptodate = {"c": self.site.GLOBAL_CONTEXT}

        for k, v in self.site.GLOBAL_CONTEXT["template_hooks"].items():
            uptodate["||template_hooks|{0}||".format(k)] = v.calculate_deps()

        for k in self.site._GLOBAL_CONTEXT_TRANSLATABLE:
            uptodate[k] = self.site.GLOBAL_CONTEXT[k](kw["default_lang"])

        # save navigation links as dependencies
        uptodate["nav_links"] = uptodate["c"]["navigation_links"](kw["default_lang"])

        uptodate["kw"] = kw

        examples_template_deps = self.site.template_system.template_deps(
            "examples.tmpl"
        )

        index_template_deps = self.site.template_system.template_deps(
            "jupyter-example-index.tmpl"
        )
        jupyter_headers = OrderedDict(
            thermo=dict(name="Thermodynamics", files=[], summaries={}),
            reactors=dict(name="Reactor Networks", files=[], summaries={}),
            flames=dict(name="One-Dimensional Flames", files=[], summaries={}),
            electrochemistry=dict(name="Electrochemistry", files=[], summaries={}),
        )

        def get_b64_str(parent, img_fname):
            img_path = parent / img_fname
            b64_str = base64.b64encode(img_path.read_bytes()).decode("utf-8")
            mime = mimetypes.guess_type(img_path.name)[0]
            b64_str = "data:{mime};base64,{b64_str}".format(mime=mime, b64_str=b64_str)
            return b64_str

        jupyter_examples = list(Path(self.input_folder).resolve().glob("*/*.ipynb"))
        uptodate["d"] = jupyter_headers.keys()
        uptodate["f"] = list(map(str, jupyter_examples))

        for jpy_ex_file in jupyter_examples:
            ex_category = jpy_ex_file.parent.stem
            if ex_category == ".ipynb_checkpoints":
                continue
            if not jupyter_headers.get(ex_category, False):
                self.logger.warn(
                    "The category {} in the Jupyter examples has no header. "
                    "Please add the folder to the jupyter_headers dictionary in the "
                    "render_jupyter_examples plugin".format(ex_category)
                )
                continue

            jupyter_headers[ex_category]["files"].append(jpy_ex_file)

            data = json.loads(jpy_ex_file.read_text())
            doc = ""
            for cell in data["cells"]:
                if cell["cell_type"] != "markdown":
                    continue
                if not doc:
                    doc = cell["source"][0].replace("#", "").strip()
                for img_idx, cell_src in enumerate(cell["source"]):
                    if "img" in cell_src:
                        img = lxml.html.fromstring(cell_src)
                        img_fname = img.attrib["src"]
                        b64_str = get_b64_str(jpy_ex_file.parent, img_fname)
                        img.attrib["src"] = b64_str
                        new_img = lxml.html.tostring(img).decode("utf-8")
                        cell["source"][img_idx] = re.sub("<img.*/>", new_img, cell_src)
                    elif "![" in cell_src:
                        img_alt, img_fname = re.findall(
                            r"!\[(.*?)\]\((.*?)\)", cell_src
                        )[0]
                        if "attachment" in img_fname:
                            img_fname = img_fname.split(":", 1)[1]
                            mime = mimetypes.guess_type(img_fname)[0]
                            b64_src = cell["attachments"][img_fname][mime]
                            b64_str = "data:{mime};base64,{b64_src}".format(
                                mime=mime, b64_src=b64_src
                            )
                        else:
                            b64_str = get_b64_str(jpy_ex_file.parent, img_fname)

                        new_img = '<img src="{b64_str}" alt="{img_alt}"/>'.format(
                            b64_str=b64_str, img_alt=img_alt
                        )
                        cell["source"][img_idx] = re.sub(
                            r"!\[.*?\]\(.*?\)", new_img, cell_src
                        )
                    else:
                        continue

            cache_file = kw["cache_folder"].joinpath(
                self.examples_folder, ex_category, jpy_ex_file.name
            )
            cache_file.parent.mkdir(parents=True, exist_ok=True)

            with cache_file.open(mode="w") as jfile:
                json.dump(data, jfile)

            jupyter_headers[ex_category]["summaries"][jpy_ex_file.name] = doc

            out_name = kw["output_folder"].joinpath(
                self.examples_folder,
                ex_category,
                jpy_ex_file.with_suffix(".ipynb.html").name,
            )

            yield {
                "basename": self.name,
                "name": str(out_name),
                "file_dep": examples_template_deps + [jpy_ex_file, cache_file],
                "targets": [out_name],
                "actions": [(render_example, [self.site, kw, cache_file, out_name])],
                # This is necessary to reflect changes in blog title,
                # sidebar links, etc.
                "uptodate": [utils.config_changed(uptodate, "jupyter_examples:source")],
                "clean": True,
            }

            out_name = kw["output_folder"].joinpath(
                self.examples_folder, ex_category, jpy_ex_file.name
            )
            yield {
                "basename": self.name,
                "name": out_name,
                "file_dep": [jpy_ex_file],
                "targets": [out_name],
                "actions": [(utils.copy_file, [jpy_ex_file, out_name])],
                "clean": True,
            }

            jupyter_headers[ex_category]["files"] = natsort.natsorted(
                jupyter_headers[ex_category]["files"], alg=natsort.IC
            )

        out_name = kw["output_folder"].joinpath(self.examples_folder, kw["index_file"])
        yield {
            "basename": self.name,
            "name": str(out_name),
            "file_dep": index_template_deps,
            "targets": [out_name],
            "actions": [
                (render_example_index, [self.site, kw, jupyter_headers, out_name])
            ],
            # This is necessary to reflect changes in blog title,
            # sidebar links, etc.
            "uptodate": [utils.config_changed(uptodate, "jupyter_examples:folder")],
            "clean": True,
        }
