"""
Parser for :class: and :func: roles
"""

from docutils import nodes
from docutils.parsers.rst import roles

from nikola.utils import split_explicit_title, get_logger
from nikola.plugin_categories import RestExtension


LOGGER = get_logger('rest_class')


class Plugin(RestExtension):
    """Plugin for class role."""

    name = 'rest_class'

    def set_site(self, site):
        """Set Nikola site."""
        self.site = site
        roles.register_canonical_role('class', class_role)
        roles.register_canonical_role('cti:class', class_role)
        roles.register_canonical_role('py:class', class_role)
        roles.register_canonical_role('mat:class', class_role)
        roles.register_canonical_role('func', class_role)
        roles.register_canonical_role('cti:func', class_role)
        roles.register_canonical_role('py:func', class_role)
        roles.register_canonical_role('mat:func', class_role)
        class_role.site = site
        return super(Plugin, self).set_site(site)


def _class_link(name, rawtext, text):
    """Handle the class role."""
    if class_role.site.processing_labels:
        return True, True, None, None, None, None

    context_map = {'py': 'cython', 'mat': 'matlab', 'cti': 'cti'}
    context = name.split(':', 1)[0]
    if context == name:
        context = class_role.site.config['DEFAULT_CONTEXT']
        default_context = True
    else:
        default_context = False

    target = '{}_targets'.format(context_map[context])

    if class_role.site.cache.get(target) is not None:
        targets = class_role.site.cache.get(target).copy()
    else:
        targets = getattr(class_role.site, target).copy()

    has_explicit_title, title, label = split_explicit_title(text)

    if label not in targets and not default_context:
        LOGGER.error('The label {label} was not found in the context {context}'.format(
            label=label, context=context))
        return False, False, None, None, None, label
    elif label not in targets and default_context:
        c_map = context_map.copy()
        c_map.pop(context)
        found_label = False
        for context, t in c_map.items():
            target = '{}_targets'.format(t)
            if class_role.site.cache.get(target) is not None:
                targets = class_role.site.cache.get(target).copy()
            else:
                targets = getattr(class_role.site, target).copy()

            if label not in targets:
                continue
            else:
                found_label = True
                LOGGER.info('The label {} was found in the context {}. Consider explicitly '
                            'specifying the context for this link'.format(label, context))
                break

        if not found_label:
            LOGGER.error('The label {} could not be found in any context'.format(label))
            return False, False, None, None, None, label

    doc_file = targets[label][0]
    permalink = '/documentation/docs-{}/'.format(class_role.site.config['CANTERA_VERSION'])
    permalink += doc_file + '#' + targets[label][1]
    code_node = nodes.literal(rawtext, targets[label][2] + '()', classes=['code', 'xref', context])
    if not has_explicit_title:
        title = targets[label][1]

    return True, False, title, code_node, permalink, label


def class_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    """Handle the class role."""
    success, processing, title, code_node, permalink, label = _class_link(name, rawtext, text)
    if processing:
        return [nodes.raw('', text, format='html')], []
    if success:
        node = make_link_node(rawtext, title, code_node, permalink, options)
        return [node], []
    else:
        msg = inliner.reporter.warning(
            'The label {0} was not found'.format(label), line=lineno)
        prb = inliner.problematic(rawtext, rawtext, msg)
        return [prb], [msg]


def make_link_node(rawtext, text, code_node, url, options):
    """Make a reST link node."""
    node = nodes.reference('', '', refuri=url, *options)
    node.append(code_node)
    return node
