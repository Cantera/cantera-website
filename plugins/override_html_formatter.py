"""Override Nikola's modification of the Pygments HTML Formatter,
reverting it back to the unmodified version.

Any attempted initialization of a NikolaPygmentsHTML object (from the nikola.utils
package) for codeblock to HTML formatting will now result in the initialization of
a default HtmlFormatter object (from the pygments.formatters package).

To create a codeblock to HTML formatter with nondefault options,
call pygments.formatters.HtmlFormatter([options])
"""
from nikola.plugin_categories import RestExtension
from pygments.formatters import HtmlFormatter
import nikola.utils


class OverrideHTMLFormatter(RestExtension):
    """Override Nikola's modification of the Pygments HTML Formatter,
    reverting it back to the unmodified version."""

    name = "override_html_formatter"

    def set_site(self, site):
        """Set the Nikola site."""
        self.site = site
        nikola.utils.NikolaPygmentsHTML = PygmentsHtmlFormatter
        return super().set_site(site)


class PygmentsHtmlFormatter(HtmlFormatter):
    """The default version of the Pygments HTML Formatter."""

    def __init__(self, *args, **kwargs):
        """Initialize the formatter with default options,
        no matter what options Nikola passes it."""
        super().__init__()
