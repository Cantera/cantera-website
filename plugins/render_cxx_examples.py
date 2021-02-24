"""Render the C++ examples from the Cantera repository into Nikola listings.

This plugin renders C++ examples from the main Cantera repository into the
examples/cpp output folder. It looks for the examples in the folder configured
in the top-level conf.py file in the ``EXAMPLES_FOLDERS`` dictionary. That
dictionary has keys with the source folder and values with the destination
folder (relative to the ``OUTPUT_FOLDER``). The relevant source folder is found
as the key associated with the value that contains the string ``cxx``,
typically ``"../cantera/samples/cxx": "examples/cxx"``.
"""
from pathlib import Path

from nikola.plugin_categories import Task
from nikola import utils
from pygments import highlight
from pygments.lexers import CppLexer
from itertools import chain
import re
import natsort


def render_example_index(site, kw, headers, output_file):
    """Render the index of all of the C++ examples.

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
        head_files = head_dict["names"]
        head_dict["names"] = [
            head_files[i : i + n] for i in range(0, len(head_files), n)  # NOQA: E203
        ]

    permalink = output_file.relative_to(kw["output_folder"])
    title = "C++ Examples"
    context = {
        "headers": headers,
        "lang": kw["default_lang"],
        "pagekind": ["example"],
        "permalink": str(permalink),
        "title": title,
        "description": title,
    }
    site.render_template("cxx-example-index.tmpl", str(output_file), context)


def render_example(site, kw, in_names, out_name):
    """Render a set of .h and .cpp files to HTML with formatting.

    Parameters
    ==========
    site:
        An instance of a Nikola site, available in any plugin as ``self.site``
    kw:
        A dictionary of keywords for this task
    in_names:
        The files to be rendered, as a list of pathlib.Path objects
    out_name:
        A pathlib.Path instance pointing to the rendered output file

    """
    items = []
    for source_file in in_names:
        code = highlight(
            source_file.read_bytes(),
            CppLexer(),
            utils.NikolaPygmentsHTML(source_file.name)
        )
        items.append({
            "code": code,
            "title": source_file.name,
            "source_link": source_file.name,
        })

    context = {
        "items": items,
        "title": out_name,
        "lang": kw["default_lang"],
        "pagekind": ["example"],
    }
    site.render_template("multifile-example.tmpl", str(out_name), context)


class RenderCxxExamples(Task):
    """Render the C++ examples with a Nikola Task.

    As with all Nikola ``Tasks``, the key method here is the ``gen_tasks``
    method, which yields dictionaries that represent tasks that doit needs
    to run. There are two primary kinds of tasks, one that renders each
    example file, and one that renders an index of all of the examples.
    """

    name = "render_cxx_examples"

    def set_site(self, site):
        """Set Nikola site."""
        # Verify that a C++ output folder appears only once in EXAMPLES_FOLDERS
        found_cxx = False
        for source, dest in site.config["EXAMPLES_FOLDERS"].items():
            if "cxx" in dest:
                if found_cxx:
                    self.logger.error(
                        "More than one folder to output C++ examples was found in "
                        "EXAMPLES_FOLDERS, exiting"
                    )
                else:
                    found_cxx = True
                    self.input_folder = source
                    self.examples_folder = dest

        if not found_cxx:
            self.logger.warn(
                "Didn't find an output folder for C++ examples in EXAMPLES_FOLDERS"
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
            "cxx-example-index.tmpl"
        )
        folder = Path(self.input_folder).resolve()
        cxx_examples = {
            subdir: list(chain(subdir.glob("*.h"), subdir.glob("*.cpp")))
            for subdir in folder.glob("*")
        }
        cxx_headings = {
            "examples": {
                "name": "Examples",
                "names": [],
                "titles": {},
                "summaries": {},
            }
        }

        uptodate["d"] = cxx_headings.keys()
        uptodate["f"] = list(map(str, cxx_examples))


        for subdir, cxx_ex_files in cxx_examples.items():
            if not cxx_ex_files:
                # Skip items that are not directories containing C++ files
                continue

            # Take the first non-empty, non "@file..." line as the title.
            # Take the following comments, up to the next blank line
            # (not including comment characters) as the summary.
            doc = []
            def append_doc(line):
                line = line.lstrip('/* !')
                if line.startswith('@file'):
                    line = re.sub(r'@file \w+.\w+\s*', '', line)
                doc.append(line)

            for ex_file in cxx_ex_files:
                if not ex_file.name.endswith('.cpp'):
                    continue
                in_block_comment = False
                for line in ex_file.read_text(encoding="utf-8").split("\n"):
                    line = line.strip()
                    if '*/' in line:
                        in_block_comment = False
                        append_doc(line[:line.find('*/')])
                    elif line.startswith('/*'):
                        in_block_comment = True
                        append_doc(line)
                    elif in_block_comment or line.startswith("//")  or line.startswith('* '):
                        append_doc(line)
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
                    f"The C++ example {ex_file!s} doesn't have an appropriate summary"
                )
            name = subdir.stem.replace("_", " ")

            cxx_headings["examples"]["names"].append(name)
            cxx_headings["examples"]["titles"][name] = title
            cxx_headings["examples"]["summaries"][name] = summary
            out_name = kw["output_folder"].joinpath(
                self.examples_folder, name.replace(' ', '-') + '.html'
            )

            yield {
                "basename": self.name,
                "name": str(out_name),
                "file_dep": examples_template_deps + cxx_ex_files,
                "targets": [out_name],
                "actions": [(render_example, [self.site, kw, cxx_ex_files, out_name])],
                # This is necessary to reflect changes in blog title,
                # sidebar links, etc.
                "uptodate": [utils.config_changed(uptodate, "cxx_examples:source")],
                "clean": True,
            }

            for ex_file in cxx_ex_files:
                out_name = kw["output_folder"].joinpath(
                    self.examples_folder, ex_file.name
                )
                yield {
                    "basename": self.name,
                    "name": str(out_name),
                    "file_dep": cxx_ex_files,
                    "targets": [out_name],
                    "actions": [(utils.copy_file, [ex_file, out_name])],
                    "clean": True,
                }

        cxx_headings["examples"]["names"] = natsort.natsorted(
            cxx_headings["examples"]["names"], alg=natsort.IC
        )

        out_name = kw["output_folder"].joinpath(self.examples_folder, kw["index_file"])
        all_files = [str(name[0]) for name in chain(cxx_examples.values()) if name]
        yield {
            "basename": self.name,
            "name": str(out_name),
            "file_dep": index_template_deps + all_files,
            "targets": [out_name],
            "actions": [
                (render_example_index, [self.site, kw, cxx_headings, out_name])
            ],
            # This is necessary to reflect changes in blog title,
            # sidebar links, etc.
            "uptodate": [utils.config_changed(uptodate, "cxx_examples:folder")],
            "clean": True,
        }
