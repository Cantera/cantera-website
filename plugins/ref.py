"""
Parser for :ref: role
"""

from docutils import nodes
from docutils.parsers.rst import roles

from nikola.utils import split_explicit_title, LOGGER
from nikola.plugin_categories import RestExtension


class Plugin(RestExtension):
    """Plugin for doc role."""

    name = 'rest_ref'

    def set_site(self, site):
        """Set Nikola site."""
        self.site = site
        roles.register_canonical_role('ref', ref_role)
        ref_role.site = site
        return super(Plugin, self).set_site(site)


def _ref_link(rawtext, text, options={}, content=[]):
    """Handle the ref role."""
    # If we're just processing the labels, ignore the role
    if ref_role.site.processing_labels:
        return True, True, None, None, None

    has_explicit_title, title, label = split_explicit_title(text)

    if ref_role.site.cache.get('ref_labels') is not None:
        ref_labels = ref_role.site.cache.get('ref_labels').copy()
    else:
        ref_labels = ref_role.site.ref_labels.copy()
    if label not in ref_labels:
        LOGGER.error('Unknown reference label: {}'.format(label))
        # LOGGER.error('ref_labels is: {}'.format(ref_role.site.ref_labels))
        return False, False, None, None, label

    permalink = ref_labels[label][0]
    if permalink.endswith('/'):
        permalink += 'index.html'
    if not has_explicit_title:
        title = ref_labels[label][2]

    permalink += '#' + label

    return True, False, title, permalink, label


def ref_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    """Handle the ref role."""
    success, processing, title, permalink, label = _ref_link(rawtext, text, options, content)
    if processing:
        return [nodes.raw('', text, format='html')], []
    if success:
        node = make_link_node(rawtext, title, permalink, options)
        return [node], []
    else:
        msg = inliner.reporter.warning(
            'Unknown reference label: {0}"'.format(label), line=lineno)
        prb = inliner.problematic(rawtext, rawtext, msg)
        return [prb], [msg]


def make_link_node(rawtext, text, url, options):
    """Make a reST link node."""
    node = nodes.reference(rawtext, text, refuri=url, *options)
    return node
