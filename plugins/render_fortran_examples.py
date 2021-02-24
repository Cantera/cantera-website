"""Render the Fortran examples from the Cantera repository into Nikola listings.

This plugin renders Fortran examples from the main Cantera repository into the
examples/fortran output folder. It looks for the examples in the folder configured
in the top-level conf.py file in the ``EXAMPLES_FOLDERS`` dictionary. That
dictionary has keys with the source folder and values with the destination
folder (relative to the ``OUTPUT_FOLDER``). The relevant source folder is found
as the key associated with the value that contains the string ``fortran``,
typically ``"../cantera/samples/f90": "examples/fortran"``.
"""
from pathlib import Path

from nikola.plugin_categories import Task
from nikola import utils
from pygments import highlight
from pygments.lexers import FortranLexer, CppLexer
from itertools import chain
import re
import natsort


def render_example_index(site, kw, headers, output_file):
    """Render the index of all of the Fortran examples.

    Parameters
    ==========
    site:
        An instance of a Nikola site, available in any plugin as ``self.site``
    kw:
        A dictionary of keywords for this task
    headers:
        A dictionary of the example categories and the summaries of each example
    output_file:
        A pathlib.Path instance representing the output file that will be rendered

    """
    n = 3
    for head_dict in headers.values():
        head_files = head_dict["files"]
        head_dict["files"] = [
            head_files[i : i + n] for i in range(0, len(head_files), n)  # NOQA: E203
        ]

    permalink = output_file.relative_to(kw["output_folder"])
    title = "Fortran Examples"
    context = {
        "headers": headers,
        "lang": kw["default_lang"],
        "pagekind": ["example"],
        "permalink": str(permalink),
        "title": title,
        "description": title,
    }
    site.render_template("fortran-example-index.tmpl", str(output_file), context)


def render_example(site, kw, in_name, out_name):
    """Render a single source file to HTML with formatting.

    Parameters
    ==========
    site:
        An instance of a Nikola site, available in any plugin as ``self.site``
    kw:
        A dictionary of keywords for this task
    in_name:
        The file to be rendered, as an instance of pathlib.Path
    out_name:
        A pathlib.Path instance pointing to the rendered output file

    """
    if str(in_name).endswith('.cpp'):
        lexer = CppLexer()
    else:
        lexer = FortranLexer()
    code = highlight(
        in_name.read_bytes(), lexer, utils.NikolaPygmentsHTML(in_name.name)
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


class RenderFortranExamples(Task):
    """Render the Fortran examples with a Nikola Task.

    As with all Nikola ``Tasks``, the key method here is the ``gen_tasks``
    method, which yields dictionaries that represent tasks that doit needs
    to run. There are two primary kinds of tasks, one that renders each
    example file, and one that renders an index of all of the examples.
    """

    name = "render_fortran_examples"

    def set_site(self, site):
        """Set Nikola site."""
        # Verify that an output folder appears only once in EXAMPLES_FOLDERS
        found_fortran = False
        for source, dest in site.config["EXAMPLES_FOLDERS"].items():
            if "fortran" in dest:
                if found_fortran:
                    self.logger.error(
                        "More than one folder to output Fortran examples was found in "
                        "EXAMPLES_FOLDERS, exiting"
                    )
                else:
                    found_fortran = True
                    self.input_folder = source
                    self.examples_folder = dest

        if not found_fortran:
            self.logger.warn(
                "Didn't find an output folder for Fortran examples in EXAMPLES_FOLDERS"
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
            "fortran-example-index.tmpl"
        )
        folder = Path(self.input_folder).resolve()
        fortran_examples = list(chain(
            folder.glob("*.f90"),
            folder.glob("../f77/*.f"),  # hack to combine all Fortran samples on one page
            folder.glob("../f77/*.cpp"),
        ))
        fortran_headers = {
            "examples": {
                "name": "Examples",
                "files": [],
                "titles": {},
                "summaries": {},
            }
        }

        uptodate["d"] = fortran_headers.keys()
        uptodate["f"] = list(map(str, fortran_examples))

        for fortran_ex_file in fortran_examples:
            # Take the first non-empty, non "@file..." line as the title.
            # Take the following comments, up to the next blank line
            # (not including comment characters) as the summary.
            # Combination of detection for F77, F90, and C/C++ comments.
            fortran_headers["examples"]["files"].append(fortran_ex_file)
            doc = []
            def append_doc(line):
                line = line.lstrip('/* !')
                if line.startswith('@file'):
                    line = re.sub(r'@file \w+.\w+\s*', '', line)
                doc.append(line)

            in_block_comment = False
            for line in fortran_ex_file.read_text(encoding="utf-8").split("\n"):
                line = line.strip()
                if '*/' in line:
                    in_block_comment = False
                    append_doc(line[:line.find('*/')])
                if line.startswith('/*'):
                    append_doc(line)
                    in_block_comment = True
                if (in_block_comment or line.startswith('!') or line.startswith("//")
                    or line.startswith('* ')):
                    append_doc(line)
                elif line.startswith('c     '):
                    append_doc(line[6:])
                elif line == 'c':
                    append_doc('')
                elif any(doc):
                    break

            title = ''
            summary = []
            for line in doc:
                if line and not title:
                    title = line
                elif line:
                    summary.append(line)
                elif summary:
                    break
            summary = ' '.join(summary)

            if not summary:
                self.logger.warn(
                    f"The Fortran example {fortran_ex_file!s} doesn't have "
                    "an appropriate summary."
                )
            fortran_headers["examples"]["summaries"][fortran_ex_file.name] = summary
            fortran_headers["examples"]["titles"][fortran_ex_file.name] = title
            out_name = kw["output_folder"].joinpath(
                self.examples_folder, fortran_ex_file.name + '.html'
            )

            yield {
                "basename": self.name,
                "name": str(out_name),
                "file_dep": examples_template_deps + [fortran_ex_file],
                "targets": [out_name],
                "actions": [(render_example, [self.site, kw, fortran_ex_file, out_name])],
                # This is necessary to reflect changes in blog title,
                # sidebar links, etc.
                "uptodate": [utils.config_changed(uptodate, "fortran_examples:source")],
                "clean": True,
            }

            out_name = kw["output_folder"].joinpath(
                self.examples_folder, fortran_ex_file.name
            )
            yield {
                "basename": self.name,
                "name": str(out_name),
                "file_dep": [fortran_ex_file],
                "targets": [out_name],
                "actions": [(utils.copy_file, [fortran_ex_file, out_name])],
                "clean": True,
            }

        fortran_headers["examples"]["files"] = natsort.natsorted(
            fortran_headers["examples"]["files"], alg=natsort.IC
        )

        out_name = kw["output_folder"].joinpath(self.examples_folder, kw["index_file"])
        yield {
            "basename": self.name,
            "name": str(out_name),
            "file_dep": index_template_deps + list(map(str, fortran_examples)),
            "targets": [out_name],
            "actions": [
                (render_example_index, [self.site, kw, fortran_headers, out_name])
            ],
            # This is necessary to reflect changes in blog title,
            # sidebar links, etc.
            "uptodate": [utils.config_changed(uptodate, "fortran_examples:folder")],
            "clean": True,
        }
