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
        return super(OverrideHTMLFormatter, self).set_site(site)


class PygmentsHtmlFormatter(HtmlFormatter):
    """The default version of the Pygments HTML Formatter."""

    def __init__(self, *args, **kwargs):
        """Initialize the formatter with default options,
        no matter what options Nikola passes it."""
        super(PygmentsHtmlFormatter, self).__init__()
