"""Build the examples from the Cantera repository into Nikola listings.

This plugin finds the Cantera examples directory in the Cantera repository
to process the examples into nicely formatted HTML along the lines of
Nikola listings. The Cantera examples are found in the ``EXAMPLES_FOLDERS``
configuration option from the top-level config.py.
"""
from pathlib import Path
import ast
import re
import base64
import mimetypes

from collections import OrderedDict
import lxml.html
import json

from nikola.plugin_categories import Task
from nikola import utils

from pygments import highlight
from pygments.util import ClassNotFound
from pygments.lexers import get_lexer_for_filename, guess_lexer, TextLexer, MatlabLexer
import natsort


class BuildExamples(Task):
    """Build the Cantera examples into the documentation."""

    name = "build_examples"

    def set_site(self, site):
        """Set Nikola site."""
        self.kw = {
            "default_lang": site.config["DEFAULT_LANG"],
            "examples_folders": site.config["EXAMPLES_FOLDERS"],
            "output_folder": Path(site.config["OUTPUT_FOLDER"]),
            "index_file": site.config["INDEX_FILE"],
            "strip_indexes": site.config["STRIP_INDEXES"],
            "cache_folder": site.config["CACHE_FOLDER"],
        }

        # Verify that no folder in EXAMPLES_FOLDERS appears twice (on output side)
        appearing_paths = set()
        for source, dest in self.kw["examples_folders"].items():
            if source in appearing_paths or dest in appearing_paths:
                problem = source if source in appearing_paths else dest
                utils.LOGGER.error(
                    "The examples input or output folder '{0}' appears in more "
                    "than one entry in EXAMPLES_FOLDERS, exiting.".format(problem)
                )
                continue
            appearing_paths.add(source)
            appearing_paths.add(dest)

        return super(BuildExamples, self).set_site(site)

    def gen_tasks(self):
        """Render examples."""
        # Things to ignore in examples
        self.ignored_extensions = (".pyc", ".pyo", ".cti", ".dat", ".ipynb_checkpoints")

        def render_example_index(
            ex_type, headers, input_folder, output_folder, output_file
        ):
            def chunks(l, n):
                """Yield successive n-sized chunks from l.

                https://stackoverflow.com/a/312464
                """
                for i in range(0, len(l), n):
                    yield l[i : i + n]

            for head, file_dict in headers.items():
                file_dict["files"] = list(chunks(file_dict["files"], 3))

            permalink = output_file.relative_to(self.kw["output_folder"])
            title = "{} Examples".format(ex_type).title()
            context = {
                "headers": headers,
                "lang": self.kw["default_lang"],
                "pagekind": ["example"],
                "permalink": str(permalink),
                "title": title,
                "description": title,
            }
            self.site.render_template(
                "{}-example-index.tmpl".format(ex_type), str(output_file), context
            )

        def render_example(in_name, out_name, input_folder, output_folder):
            needs_ipython_css = False
            if in_name.suffix == ".ipynb":
                # Special handling: render ipynb in listings (Issue #1900)
                ipynb_compiler = self.site.plugin_manager.getPluginByName(
                    "ipynb", "PageCompiler"
                ).plugin_object
                with in_name.open(mode="r") as in_file:
                    nb_json = ipynb_compiler._nbformat_read(in_file)
                ipynb_raw = ipynb_compiler._compile_string(nb_json)
                ipynb_html = lxml.html.fromstring(ipynb_raw)
                code = lxml.html.tostring(ipynb_html, encoding="unicode")
                needs_ipython_css = True
            elif in_name.suffix == ".m":
                lexer = MatlabLexer()
                code = highlight(
                    in_name.read_bytes(), lexer, utils.NikolaPygmentsHTML(in_name.name)
                )
            else:
                try:
                    lexer = get_lexer_for_filename(in_name.name)
                except ClassNotFound:
                    try:
                        lexer = guess_lexer(in_name.read_bytes())
                    except ClassNotFound:
                        lexer = TextLexer()
                code = highlight(
                    in_name.read_bytes(), lexer, utils.NikolaPygmentsHTML(in_name.name)
                )

            title = in_name.name

            permalink = out_name.relative_to(self.kw["output_folder"])
            source_link = permalink.stem  # remove '.html'
            context = {
                "code": code,
                "title": title,
                "permalink": str(permalink),
                "lang": self.kw["default_lang"],
                "description": title,
                "source_link": source_link,
                "pagekind": ["example"],
            }
            if needs_ipython_css:
                # If someone does not have ipynb posts and only listings, we
                # need to enable ipynb CSS for ipynb listings.
                context["needs_ipython_css"] = True
            self.site.render_template("examples.tmpl", str(out_name), context)

        yield self.group_task()

        # When any key or value in the uptodate dictionary changes, the
        # examples pages need to be rebuilt.
        uptodate = {"c": self.site.GLOBAL_CONTEXT}

        for k, v in self.site.GLOBAL_CONTEXT["template_hooks"].items():
            uptodate["||template_hooks|{0}||".format(k)] = v.calculate_deps()

        for k in self.site._GLOBAL_CONTEXT_TRANSLATABLE:
            uptodate[k] = self.site.GLOBAL_CONTEXT[k](self.kw["default_lang"])

        # save navigation links as dependencies
        uptodate["nav_links"] = uptodate["c"]["navigation_links"](
            self.kw["default_lang"]
        )

        uptodate["kw"] = self.kw

        examples_template_deps = self.site.template_system.template_deps(
            "examples.tmpl"
        )
        for input_folder, example_folder in self.kw["examples_folders"].items():

            #########################################################
            # Build the Python examples
            #########################################################
            if "python" in example_folder:
                index_template_deps = self.site.template_system.template_deps(
                    "python-example-index.tmpl"
                )
                headers = OrderedDict(
                    thermo=dict(files=[], summaries={}, name="Thermodynamics"),
                    kinetics=dict(files=[], summaries={}, name="Kinetics"),
                    transport=dict(files=[], summaries={}, name="Transport"),
                    reactors=dict(files=[], summaries={}, name="Reactor Networks"),
                    onedim=dict(files=[], summaries={}, name="One-Dimensional Flames"),
                    multiphase=dict(files=[], summaries={}, name="Multiphase Mixtures"),
                    surface_chemistry=dict(
                        files=[], summaries={}, name="Surface Chemistry"
                    ),
                )

                python_examples = list(Path(input_folder).resolve().glob("*/*.py"))
                uptodate2 = uptodate.copy()
                uptodate2["d"] = headers.keys()
                uptodate2["f"] = list(map(str, python_examples))

                for py_ex_file in python_examples:
                    ex_category = py_ex_file.parent.stem
                    headers[ex_category]["files"].append(py_ex_file)
                    mod = ast.parse(py_ex_file.read_bytes())
                    for node in mod.body:
                        if isinstance(node, ast.Expr) and isinstance(
                            node.value, ast.Str
                        ):
                            doc = node.value.s.strip().split("\n\n")[0].strip()
                            if not doc.endswith("."):
                                doc += "."
                            break
                    headers[ex_category]["summaries"][py_ex_file.name] = doc

                    out_name = self.kw["output_folder"].joinpath(
                        example_folder,
                        ex_category,
                        py_ex_file.with_suffix(".py.html").name,
                    )
                    yield {
                        "basename": self.name,
                        "name": str(out_name),
                        "file_dep": examples_template_deps + [py_ex_file],
                        "targets": [out_name],
                        "actions": [
                            (
                                render_example,
                                [py_ex_file, out_name, input_folder, example_folder],
                            )
                        ],
                        # This is necessary to reflect changes in blog title,
                        # sidebar links, etc.
                        "uptodate": [
                            utils.config_changed(uptodate2, "build_examples:source")
                        ],
                        "clean": True,
                    }

                    out_name = self.kw["output_folder"].joinpath(
                        example_folder, ex_category, py_ex_file.name
                    )
                    yield {
                        "basename": self.name,
                        "name": out_name,
                        "file_dep": [py_ex_file],
                        "targets": [out_name],
                        "actions": [(utils.copy_file, [py_ex_file, out_name])],
                        "clean": True,
                    }

                for head in headers.keys():
                    headers[head]["files"] = natsort.natsorted(
                        headers[head]["files"], alg=natsort.IC
                    )

                out_name = self.kw["output_folder"].joinpath(
                    example_folder, self.kw["index_file"]
                )
                yield {
                    "basename": self.name,
                    "name": str(out_name),
                    "file_dep": index_template_deps,
                    "targets": [out_name],
                    "actions": [
                        (
                            render_example_index,
                            ["python", headers, input_folder, example_folder, out_name],
                        )
                    ],
                    # This is necessary to reflect changes in blog title,
                    # sidebar links, etc.
                    "uptodate": [
                        utils.config_changed(uptodate2, "build_examples:folder")
                    ],
                    "clean": True,
                }

            #########################################################
            # Build the Matlab examples
            #########################################################
            elif "matlab" in example_folder:
                index_template_deps = self.site.template_system.template_deps(
                    "matlab-example-index.tmpl"
                )
                matlab_examples = list(Path(input_folder).resolve().glob("*.m"))
                headers = {
                    "examples": {"name": "Examples", "files": [], "summaries": {}}
                }

                uptodate2 = uptodate.copy()
                uptodate2["d"] = headers.keys()
                uptodate2["f"] = list(map(str, matlab_examples))

                for mat_ex_file in matlab_examples:
                    if "tut" in mat_ex_file.name or "test" in mat_ex_file.name:
                        continue
                    headers["examples"]["files"].append(mat_ex_file)
                    doc = ""
                    for line in mat_ex_file.read_text().split("\n"):
                        line = line.strip()
                        if line.startswith("%"):
                            doc = line.strip("%").strip()
                        if doc:
                            break
                    # TODO: Warn if example doesn't have a docstring
                    if not doc:
                        pass
                    name = mat_ex_file.stem.replace("_", " ")
                    if doc.lower().replace("_", " ").startswith(name):
                        # This is too aggressive at removing leading -
                        # It also removes from things like "zero-dimensional"
                        doc = doc[len(name) :].replace("-", "").strip()
                    headers["examples"]["summaries"][mat_ex_file.name] = doc

                    out_name = self.kw["output_folder"].joinpath(
                        example_folder, mat_ex_file.with_suffix(".m.html").name
                    )

                    yield {
                        "basename": self.name,
                        "name": str(out_name),
                        "file_dep": examples_template_deps + [mat_ex_file],
                        "targets": [out_name],
                        "actions": [
                            (
                                render_example,
                                [mat_ex_file, out_name, input_folder, example_folder],
                            )
                        ],
                        # This is necessary to reflect changes in blog title,
                        # sidebar links, etc.
                        "uptodate": [
                            utils.config_changed(uptodate2, "build_examples:source")
                        ],
                        "clean": True,
                    }

                    out_name = self.kw["output_folder"].joinpath(
                        example_folder, mat_ex_file.name
                    )
                    yield {
                        "basename": self.name,
                        "name": str(out_name),
                        "file_dep": [mat_ex_file],
                        "targets": [out_name],
                        "actions": [(utils.copy_file, [mat_ex_file, out_name])],
                        "clean": True,
                    }

                headers["examples"]["files"] = natsort.natsorted(
                    headers["examples"]["files"], alg=natsort.IC
                )

                out_name = self.kw["output_folder"].joinpath(
                    example_folder, self.kw["index_file"]
                )
                yield {
                    "basename": self.name,
                    "name": str(out_name),
                    "file_dep": index_template_deps,
                    "targets": [out_name],
                    "actions": [
                        (
                            render_example_index,
                            ["matlab", headers, input_folder, example_folder, out_name],
                        )
                    ],
                    # This is necessary to reflect changes in blog title,
                    # sidebar links, etc.
                    "uptodate": [
                        utils.config_changed(uptodate2, "build_examples:folder")
                    ],
                    "clean": True,
                }

            #########################################################
            # Build the Jupyter examples
            #########################################################
            elif "jupyter" in example_folder:
                index_template_deps = self.site.template_system.template_deps(
                    "jupyter-example-index.tmpl"
                )
                headers = OrderedDict(
                    thermo=dict(name="Thermodynamics", files=[], summaries={}),
                    reactors=dict(name="Reactor Networks", files=[], summaries={}),
                    flames=dict(name="One-Dimensional Flames", files=[], summaries={}),
                    electrochemistry=dict(
                        name="Electrochemistry", files=[], summaries={}
                    ),
                )

                def get_b64_str(parent, img_fname):
                    img_path = parent / img_fname
                    b64_str = base64.b64encode(img_path.read_bytes()).decode("utf-8")
                    mime = mimetypes.guess_type(img_path.name)[0]
                    b64_str = "data:{mime};base64,{b64_str}".format(
                        mime=mime, b64_str=b64_str
                    )
                    return b64_str

                jupyter_examples = list(Path(input_folder).resolve().glob("*/*.ipynb"))
                uptodate2 = uptodate.copy()
                uptodate2["d"] = headers.keys()
                uptodate2["f"] = list(map(str, jupyter_examples))

                cache_folder = Path(self.kw["cache_folder"])

                for jpy_ex_file in jupyter_examples:
                    ex_category = jpy_ex_file.parent.stem
                    if ex_category == ".ipynb_checkpoints":
                        continue

                    headers[ex_category]["files"].append(jpy_ex_file)

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
                                cell["source"][img_idx] = re.sub(
                                    "<img.*/>", new_img, cell_src
                                )
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

                    cache_file = cache_folder.joinpath(
                        example_folder, ex_category, jpy_ex_file.name
                    )
                    cache_file.parent.mkdir(parents=True, exist_ok=True)

                    with cache_file.open(mode="w") as jfile:
                        json.dump(data, jfile)

                    headers[ex_category]["summaries"][jpy_ex_file.name] = doc

                    out_name = self.kw["output_folder"].joinpath(
                        example_folder,
                        ex_category,
                        jpy_ex_file.with_suffix(".ipynb.html").name,
                    )

                    yield {
                        "basename": self.name,
                        "name": str(out_name),
                        "file_dep": examples_template_deps + [jpy_ex_file, cache_file],
                        "targets": [out_name],
                        "actions": [
                            (
                                render_example,
                                [cache_file, out_name, input_folder, example_folder],
                            )
                        ],
                        # This is necessary to reflect changes in blog title,
                        # sidebar links, etc.
                        "uptodate": [
                            utils.config_changed(uptodate2, "build_examples:source")
                        ],
                        "clean": True,
                    }

                    out_name = self.kw["output_folder"].joinpath(
                        example_folder, ex_category, jpy_ex_file.name
                    )
                    yield {
                        "basename": self.name,
                        "name": out_name,
                        "file_dep": [jpy_ex_file],
                        "targets": [out_name],
                        "actions": [(utils.copy_file, [jpy_ex_file, out_name])],
                        "clean": True,
                    }

                headers[ex_category]["files"] = natsort.natsorted(
                    headers[ex_category]["files"], alg=natsort.IC
                )

                out_name = self.kw["output_folder"].joinpath(
                    example_folder, self.kw["index_file"]
                )
                yield {
                    "basename": self.name,
                    "name": str(out_name),
                    "file_dep": index_template_deps,
                    "targets": [out_name],
                    "actions": [
                        (
                            render_example_index,
                            [
                                "jupyter",
                                headers,
                                input_folder,
                                example_folder,
                                out_name,
                            ],
                        )
                    ],
                    # This is necessary to reflect changes in blog title,
                    # sidebar links, etc.
                    "uptodate": [
                        utils.config_changed(uptodate2, "build_examples:folder")
                    ],
                    "clean": True,
                }
