"""Build the examples from the Cantera repository into Nikola listings.

This plugin finds the Cantera examples directory in the Cantera repository
to process the examples into nicely formatted HTML along the lines of
Nikola listings. The Cantera examples are found in the ``EXAMPLES_FOLDERS``
configuration option from the top-level config.py.
"""
from pathlib import Path
import ast
from collections import OrderedDict

from nikola.plugin_categories import Task
from nikola import utils
import natsort
from pygments import highlight
from pygments.lexers import Python3Lexer


def render_example_index(site, kw, headers, output_file):
    n = 3
    for head_dict in headers.values():
        head_files = head_dict["files"]
        head_dict["files"] = [
            head_files[i : i + n] for i in range(0, len(head_files), n)
        ]

    permalink = output_file.relative_to(kw["output_folder"])
    title = "Python Examples"
    context = {
        "headers": headers,
        "lang": kw["default_lang"],
        "pagekind": ["example"],
        "permalink": str(permalink),
        "title": title,
        "description": title,
    }
    site.render_template("python-example-index.tmpl", str(output_file), context)


def render_example(site, kw, in_name, out_name):
    code = highlight(
        in_name.read_bytes(), Python3Lexer(), utils.NikolaPygmentsHTML(in_name.name)
    )

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
    }
    site.render_template("examples.tmpl", str(out_name), context)


class RenderPythonExamples(Task):

    name = "render_python_examples"

    def set_site(self, site):
        """Set Nikola site."""
        # Verify that a Python output folder appears only once in EXAMPLES_FOLDERS
        found_python = False
        for source, dest in site.config["EXAMPLES_FOLDERS"].items():
            if "python" in dest:
                if found_python:
                    self.logger.error(
                        "More than one folder to output Python examples was found in EXAMPLES_FOLDERS, exiting"
                    )
                else:
                    found_python = True
                    self.input_folder = source
                    self.examples_folder = dest

        if not found_python:
            self.logger.warn(
                "Didn't find an output folder for Python examples in EXAMPLES_FOLDERS"
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
            "python-example-index.tmpl"
        )
        python_headers = OrderedDict(
            thermo=dict(files=[], summaries={}, name="Thermodynamics"),
            kinetics=dict(files=[], summaries={}, name="Kinetics"),
            transport=dict(files=[], summaries={}, name="Transport"),
            reactors=dict(files=[], summaries={}, name="Reactor Networks"),
            onedim=dict(files=[], summaries={}, name="One-Dimensional Flames"),
            multiphase=dict(files=[], summaries={}, name="Multiphase Mixtures"),
            surface_chemistry=dict(files=[], summaries={}, name="Surface Chemistry"),
        )

        python_examples = list(Path(self.input_folder).resolve().glob("*/*.py"))
        uptodate["d"] = python_headers.keys()
        uptodate["f"] = list(map(str, python_examples))

        for py_ex_file in python_examples:
            ex_category = py_ex_file.parent.stem

            if not python_headers.get(ex_category, False):
                self.logger.warn(
                    "The category {} in the Python examples has no header. "
                    "Please add the folder to the python_headers dictionary in the "
                    "render_python_examples plugin".format(ex_category)
                )
                continue

            python_headers[ex_category]["files"].append(py_ex_file)
            mod = ast.parse(py_ex_file.read_bytes())
            for node in mod.body:
                if isinstance(node, ast.Expr) and isinstance(node.value, ast.Str):
                    doc = node.value.s.strip().split("\n\n")[0].strip()
                    if not doc.endswith("."):
                        doc += "."
                    break
            python_headers[ex_category]["summaries"][py_ex_file.name] = doc

            out_name = kw["output_folder"].joinpath(
                self.examples_folder,
                ex_category,
                py_ex_file.with_suffix(".py.html").name,
            )
            yield {
                "basename": self.name,
                "name": str(out_name),
                "file_dep": examples_template_deps + [py_ex_file],
                "targets": [out_name],
                "actions": [(render_example, [self.site, kw, py_ex_file, out_name])],
                # This is necessary to reflect changes in blog title,
                # sidebar links, etc.
                "uptodate": [utils.config_changed(uptodate, "python_examples:source")],
                "clean": True,
            }

            out_name = kw["output_folder"].joinpath(
                self.examples_folder, ex_category, py_ex_file.name
            )
            yield {
                "basename": self.name,
                "name": out_name,
                "file_dep": [py_ex_file],
                "targets": [out_name],
                "actions": [(utils.copy_file, [py_ex_file, out_name])],
                "clean": True,
            }

        for head in python_headers.keys():
            python_headers[head]["files"] = natsort.natsorted(
                python_headers[head]["files"], alg=natsort.IC
            )

        out_name = kw["output_folder"].joinpath(self.examples_folder, kw["index_file"])
        yield {
            "basename": self.name,
            "name": str(out_name),
            "file_dep": index_template_deps,
            "targets": [out_name],
            "actions": [
                (
                    render_example_index,
                    [self.site, kw, python_headers, out_name],
                )
            ],
            # This is necessary to reflect changes in blog title,
            # sidebar links, etc.
            "uptodate": [utils.config_changed(uptodate, "python_examples:folder")],
            "clean": True,
        }
