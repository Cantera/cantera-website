"""
Parse the documentation to allow Sphinx-style docs references
"""
from pathlib import Path

from nikola.plugin_categories import Task
from nikola.utils import get_logger
import lxml
from lxml.html import tostring


class ParseDocs(Task):
    """
    Parse the documentation to find link targets. Since this
    has to be done before any posts are read (so that the targets
    dictionaries are available to the class roles), put it in
    set_site so it runs when the plugin is loaded. Hack suggested
    in a Nikola issue:
    https://github.com/getnikola/nikola/issues/1553#issuecomment-68594294
    """

    name = 'parse_docs'

    def set_site(self, site):
        self.site = site
        self.logger = get_logger(self.name)
        self.site.cython_targets = {}
        self.site.cti_targets = {}
        self.site.matlab_targets = {}

        base_dir = Path('api-docs/docs/sphinx/html')
        # This needs to be just 'matlab' after changes are merged to Cantera
        dirs = ['cython', 'matlab/code-docs', 'cti']
        for dir in dirs:
            target_name = '{}_targets'.format(dir.split('/')[0])
            targets_dict = getattr(self.site, target_name)
            files = (base_dir/dir).glob('*.html')
            duplicate_targets = []
            for file in files:

                with open(file, 'r') as html_file:
                    tree = lxml.html.parse(html_file)

                location = str(file.relative_to('api-docs/docs'))
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

        for dir in dirs:
            target_name = '{}_targets'.format(dir.split('/')[0])
            cached_target = site.cache.get(target_name)
            if cached_target is not None:
                cached_target.update(getattr(site, target_name))
                site.cache.set(target_name, cached_target)
            else:
                site.cache.set(target_name, getattr(site, target_name))

        return super(ParseDocs, self).set_site(site)

    def gen_tasks(self):
        # Make sure that this task is created, even if nothing ends up needing to be done
        yield self.group_task()
