"""Copy an entire tree of files."""
from shutil import copytree, ignore_patterns
import os

from nikola.plugin_categories import Task
from nikola.utils import config_changed


class CopyTree(Task):
    """Copy an entire tree of files."""

    name = 'copy_tree'

    def gen_tasks(self):
        """Copy static files into the output folder."""
        kw = {
            'files_folders': self.site.config['FILES_FOLDERS'],
            'output_folder': self.site.config['OUTPUT_FOLDER'],
            'filters': self.site.config['FILTERS'],
        }

        # Ensure this task is created even if nothing needs to be done
        yield self.group_task()

        for src, rel_dst in kw['files_folders'].items():
            final_dst = os.path.join(kw['output_folder'], rel_dst)
            yield {
                'basename': self.name,
                'name': rel_dst,
                'targets': [final_dst],
                'uptodate': [config_changed(kw, 'copy_tree')],
                'actions': [
                    (copytree, [src, final_dst], {'ignore': ignore_patterns('*.md5', '*.map')}),
                ],
            }
