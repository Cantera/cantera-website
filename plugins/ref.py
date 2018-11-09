"""Parser for :ref: role.

This plugin is an extension for the reST parser in Nikola that looks
for the ``:ref:`` role and replaces that reference with a link node
to the appropriate target from the `process_ref_targets` plugin.
"""

from docutils import nodes
from docutils.parsers.rst import roles

from nikola.utils import split_explicit_title, get_logger
from nikola.plugin_categories import RestExtension

LOGGER = get_logger('rest_ref')


class Plugin(RestExtension):
    """Plugin for ref role."""

    name = 'rest_ref'

    def set_site(self, site):
        """Set Nikola site."""
        self.site = site
        roles.register_canonical_role('ref', ref_role)
        ref_role.site = site
        return super(Plugin, self).set_site(site)


def _ref_link(rawtext, text, options={}, content=[]):
    """Handle the ref role."""
    # If we're just processing the targets, ignore the role
    if ref_role.site.processing_targets:
        return True, True, None, None, None

    has_explicit_title, title, target = split_explicit_title(text)

    if ref_role.site.cache.get('ref_targets') is not None:
        ref_targets = ref_role.site.cache.get('ref_targets').copy()
    else:
        ref_targets = ref_role.site.ref_targets.copy()

    if ref_role.site.cache.get('anon_ref_targets') is not None:
        anon_ref_targets = ref_role.site.cache.get('anon_ref_targets').copy()
    else:
        anon_ref_targets = ref_role.site.anon_ref_targets.copy()

    if target not in ref_targets and (target in anon_ref_targets and not has_explicit_title):
        LOGGER.error('Anonymous targets must have a link text: {}'.format(target))
        return False, False, None, None, target
    elif target in anon_ref_targets:
        permalink = anon_ref_targets[target][0]
        if permalink.endswith('/'):
            permalink += 'index.html'

        permalink += '#' + target

        return True, False, title, permalink, target
    else:
        LOGGER.error('Unknown reference target: {}'.format(target))
        return False, False, None, None, target

    if target not in ref_targets:
        LOGGER.error('Unknown reference target: {}'.format(target))
        return False, False, None, None, target

    permalink = ref_targets[target][0]
    if permalink.endswith('/'):
        permalink += 'index.html'
    if not has_explicit_title:
        title = ref_targets[target][2]

    permalink += '#' + target

    return True, False, title, permalink, target


def ref_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    """Handle the ref role.

    The function signature here is a standard signature for roles in reST plugins.
    """
    success, processing, title, permalink, target = _ref_link(rawtext, text, options, content)
    if processing:
        return [nodes.raw('', text, format='html')], []
    if success:
        node = nodes.reference(rawtext, title, refuri=permalink, *options)
        return [node], []
    else:
        msg = inliner.reporter.warning(
            'Unknown reference target: {0}"'.format(target), line=lineno)
        prb = inliner.problematic(rawtext, rawtext, msg)
        return [prb], [msg]
