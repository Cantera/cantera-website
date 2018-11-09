"""Plugin to format Bootstrap directives.

Portions of this code are adapted from the bootstrap-rst project
https://github.com/rougier/bootstrap-rst
which is licensed under the MIT license

Copyright (c) 2014 Nicolas P. Rougier

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

from docutils import nodes, utils
import docutils
from docutils.parsers.rst import directives, Directive
from nikola.plugin_categories import RestExtension


class Bootstrap(RestExtension):
    """Extend the reST parser with directives for Bootstrap classes."""

    name = "boostrap_rst"

    def set_site(self, site):
        """Set the Nikola site."""
        self.site = site
        directives.register_directive("container", Container)
        directives.register_directive("jumbotron", Jumbotron)
        directives.register_directive("row", Row)
        directives.register_directive("section", Section)
        directives.register_directive("card", Card)
        directives.register_directive("card-deck", CardDeck)
        directives.register_directive("card-body", CardBody)
        directives.register_directive("card-header", CardHead)
        directives.register_directive("card-footer", CardFoot)
        directives.register_directive("button", Button)
        directives.register_directive("accordion", Accordion)

        add_node("container", visit_container, depart_container)

        return super(Bootstrap, self).set_site(site)


def visit_container(self, node):
    """Docutils visit function for the Container."""
    attrs = node.non_default_attributes().copy()
    if "classes" in attrs:
        del attrs["classes"]
    if "endless" in attrs:
        del attrs["endless"]
    self.body.append(self.starttag(node, node.tagname, **attrs))


def depart_container(self, node):
    """Docutils depart function for the Container."""
    if "endless" not in node:
        self.body.append("</%s>\n" % node.tagname)
    else:
        pass


class Container(Directive):
    """Overridden Container.

    You can choose any tag name just like a barebones computer or a wild card.
    Default tag name is div.
    This is based on the code at docutils.parsers.rst.directives.html.
    Derived classes:
    default_class = None
    default_tagname = None
    default_attributes = None
    Derived class example::

        class Thumbnail(Container):
            default_class = ['thumbnail']

        class Html5Header(Container):
            default_tagname = 'header'

    RestructuredText example::

        .. container::
           :tagname: header
           .. container:: navbar navbar-expand-md navbar-dark fixed-top bg-dark
              :tagname: nav
              .. container:: navbar-brand
                 :tagname: a
                 :attributes: href=#
                 Carousel
              .. container:: navbar-toggler
                 :tagname: button
                 :attributes: type=button
                              data-toggle=collapse
                              data-target=#navbarCollapse
                              aria-controls=navbarCollapse
                              aria-expanded=false
                              aria-label="Toggle navigation"
                 .. raw:: html
                    <span class="navbar-toggler-icon"></span>
    """

    optional_arguments = 1
    final_argument_whitespace = True
    option_spec = {
        "name": directives.unchanged,
        "tagname": directives.unchanged,
        "attributes": directives.unchanged,
        "endless": directives.flag,
    }
    has_content = True
    default_class = None
    default_tagname = None
    default_attributes = None
    default_endless = False

    def set_classes(self, node):
        """Set the classes on the node."""
        try:
            if self.default_class is not None and self.arguments:
                classes = self.default_class + self.arguments
            elif self.arguments:
                classes = directives.class_option(self.arguments[0])
            else:
                classes = self.default_class
        except ValueError:
            raise self.error(
                "Invalid class attribute value for '{}' directive: '{}'.".format(
                    self.name, self.arguments[0]
                )
            )

        if classes:
            node["classes"].extend(classes)

        return node

    def set_tagname(self, node):
        """Set the node tagname."""
        try:
            if "tagname" in self.options:
                node.tagname = self.options.get("tagname", "div")
            elif self.default_tagname is not None:
                node.tagname = self.default_tagname
            else:
                node.tagname = "div"
        except ValueError:
            raise self.error(
                "Invalid tag name for '{}' directive: '{}'.".format(
                    self.name, node.tagname
                )
            )

        return node

    def set_attributes(self, node):
        """Set the node attributes."""
        attrs = None
        if "attributes" in self.options:
            attrs = self.options.get("attributes", "")
        elif self.default_attributes:
            attrs = self.default_attributes
        if attrs is not None:
            tokens = attrs.split("\n")
            try:
                attname, val = utils.extract_name_value(tokens[0])[0]
                if attname == "id":
                    node["ids"].append(val)
                else:
                    node.attributes.update({attname: val})
            except utils.NameValueError:
                node["name"] = tokens[0]
            for token in tokens[1:]:
                try:
                    attname, val = utils.extract_name_value(token)[0]
                    if attname == "id":
                        node["ids"].append(val)
                    else:
                        node.attributes.update({attname: val})
                except utils.NameValueError as detail:
                    line = self.state_machine.line
                    msg = self.state_machine.reporter.error(
                        'Error parsing %s tag attribute "%s": %s.'
                        % (node.tagname, token, detail),
                        nodes.literal_block(line, line),
                    )
                    return [msg]

        return node

    def run(self):
        """Run the directive."""
        text = "\n".join(self.content)
        node = nodes.container(text)

        node = self.set_classes(node)
        node = self.set_tagname(node)
        node = self.set_attributes(node)
        if "endless" in self.options or self.default_endless:
            node["endless"] = True
        if self.content:
            self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


class Jumbotron(Container):
    """Class for Bootstrap ``jumbotron``s."""

    default_class = ["jumbotron"]


class Accordion(Container):
    """Class for Bootstrap ``accordion``s."""

    default_class = ["accordion"]


class Row(Container):
    """Class for Bootstrap ``row``s."""

    default_class = ["row"]


class Card(Container):
    """Class for Bootstrap ``card``s."""

    default_class = ["card"]


class CardDeck(Container):
    """Class for Bootstrap ``card-deck``s."""

    default_class = ["card-deck"]


class CardBody(Container):
    """Class for Bootstrap ``card-body``s."""

    default_class = ["card-body"]


class CardHead(Container):
    """Class for Bootstrap ``card-header``s."""

    default_class = ["card-header"]


class CardFoot(Container):
    """Class for Bootstrap ``card-footer``s."""

    default_class = ["card-footer"]


class Section(Container):
    """Class for Bootstrap ``section``s."""

    default_tagname = "section"


class Button(Container):
    """Class for Bootstrap ``button``s."""

    default_tagname = "button"


def add_node(node_name, visit_function=None, depart_function=None):
    """Register a Docutils node class."""
    nodes._add_node_class_names([node_name])
    if visit_function is not None:
        setattr(
            docutils.writers._html_base.HTMLTranslator,
            "visit_" + node_name,
            visit_function,
        )
    if depart_function is not None:
        setattr(
            docutils.writers._html_base.HTMLTranslator,
            "depart_" + node_name,
            depart_function,
        )
