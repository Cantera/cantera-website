"""Copy an entire tree of files.

Replacement plugin for the default Nikola copy_tree plugin.
This plugin copies entire folders at once, rather than individually
copying files within the folder. This substantially reduces the
printed output to stdout during the copying process and is much
faster. We prefer this plugin since we are copying folders around
for the API documentation.
"""
import os
from pathlib import Path
from shutil import copytree, ignore_patterns, rmtree

from nikola.plugin_categories import Task
from nikola.utils import config_changed


class CopyTree(Task):
    """Copy an entire tree of files."""

    name = "copy_tree"

    def gen_tasks(self):
        """Copy docs files into the output folder."""
        # Put these into a dictionary so that if they change,
        # the task is marked as out-of-date
        kw = {
            "docs_folders": self.site.config["DOCS_FOLDERS"],
            "output_folder": self.site.config["OUTPUT_FOLDER"],
        }

        # Ensure this task is created even if nothing needs to be done
        yield self.group_task()

        def copytree_task(src, dst, ignore):
            if os.path.exists(dst):
                rmtree(dst)

            copytree(src=src, dst=dst, ignore=ignore)

        for src, rel_dst in kw["docs_folders"].items():
            final_dst = os.path.join(kw["output_folder"], rel_dst)
            all_files = [i for i in Path(src).glob("**/*") if not i.is_dir()]
            yield {
                "basename": self.name,
                "name": rel_dst,
                "targets": [final_dst],
                "uptodate": [config_changed(kw, "copy_tree")],
                "file_dep": all_files,
                "actions": [
                    (
                        copytree_task,
                        [],
                        {
                            "src": src,
                            "dst": final_dst,
                            "ignore": ignore_patterns("*.md5", "*.map"),
                        },
                    )
                ],
            }
