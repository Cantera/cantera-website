"""Parse the documentation to allow Sphinx-style docs references.

This plugin allows referring to other locations in the documentation
with ``:class:`` style references.
"""
from pathlib import Path

from nikola.plugin_categories import Task
from nikola.utils import get_logger
from lxml.html import tostring, parse


class ParseDocs(Task):
    """Parse the documentation to find link targets."""

    name = 'parse_docs'

    def set_site(self, site):
        """Set up the Nikola site instance for this plugin."""
        self.site = site

        # Ensure that this Task is run before the posts are rendered
        # We need to enforce this order because rendering the posts
        # requires the targets that we generate here
        self.inject_dependency('render_posts', self.name)

        self.logger = get_logger(self.name)
        self.site.cython_targets = {}
        self.site.cti_targets = {}
        self.site.matlab_targets = {}

        self.kw = {
            'output_folder': site.config['OUTPUT_FOLDER'],
            'docs_folders': site.config['FILES_FOLDERS'],
            'cantera_version': site.config['CANTERA_VERSION']
        }

        return super(ParseDocs, self).set_site(site)

    def gen_tasks(self):
        """Generate the tasks to be done."""
        # Ensure that this task is created, even if nothing needs to be done
        yield self.group_task()

        def process_targets(dirname, base_dir, docs_folder):
            files = (base_dir/dirname).glob('*.html')

            target_name = '{}_targets'.format(dirname)
            targets_dict = getattr(self.site, target_name)

            duplicate_targets = []

            for file in files:
                file = Path(file)
                with open(file, 'r') as html_file:
                    tree = parse(html_file)

                location = str(file.relative_to(docs_folder))
                for elem in tree.xpath('//dt'):
                    if elem.get('id') is None:
                        continue

                    elem_id = elem.get('id')
                    parts = elem_id.split('.')
                    try:
                        title = elem.xpath('code[@class="descname"]/text()')[0]
                    except IndexError:
                        self.logger.error('Unknown title for class: {}'.format(tostring(elem)))
                        title = parts[-1]

                    targets = ['.'.join(parts[x:]) for x in range(len(parts))]
                    for target in targets:
                        # Don't allow targets that are duplicated within a context
                        # This means we can't link to overloaded attributes with the
                        # :class: role and the unqualified name, but it's not clear
                        # where those should link anyways. You can always use the
                        # qualified name such as ClassName.property
                        if target in duplicate_targets:
                            continue
                        elif target in targets_dict:
                            duplicate_targets.append(target)
                            targets_dict.pop(target)
                        else:
                            targets_dict[target] = (location, elem_id, title)

            cached_target = self.site.cache.get(target_name)
            if cached_target is not None:
                cached_target.update(getattr(self.site, target_name))
                self.site.cache.set(target_name, cached_target)
            else:
                self.site.cache.set(target_name, getattr(self.site, target_name))

        # Make sure that this task is created, even if nothing ends up needing to be done
        yield self.group_task()

        output_folder = Path(self.kw['output_folder'])
        # Uncomment these two lines when 2.4 is released and put into the api-docs folder
        cantera_version = self.kw['cantera_version']
        docs_folder = self.kw['docs_folders']['api-docs/docs-{}'.format(cantera_version)]
        # docs_folder = Path(self.kw['docs_folders']['../cantera/build/docs'])

        base_dir = output_folder/docs_folder/'sphinx'/'html'

        dirs = ['cython', 'matlab', 'cti']
        for dirname in dirs:
            yield {
                'basename': self.name,
                'name': dirname,
                'task_dep': ['copy_tree'],
                'actions': [(process_targets, [dirname, base_dir, output_folder/docs_folder])],
            }
