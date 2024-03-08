from __future__ import annotations

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import sys
from pathlib import Path

# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

sys.path.insert(0, str(Path(__file__).parent.resolve()))
needs_sphinx = "6.2"


# -- Project information -----------------------------------------------------

project = "Cantera"
copyright = "2023, Cantera Developers"
author = "Cantera Developers"
html_title = "Cantera"

# The full version, including alpha/beta/rc tags
version = "2.6"
release = "2.6.0"

source_suffix = {
    ".rst": "restructuredtext",
    ".txt": "restructuredtext",
    ".md": "markdown",
}

# Print warnings into the built HTML files
keep_warnings = True

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions: list[str] = [
    "sphinx_design",
    "myst_parser",
    "sphinx.ext.duration",
    "sphinx.ext.mathjax",
    "sphinxcontrib.mermaid",
    "ablog",
    "sphinx.ext.intersphinx",
]

myst_enable_extensions = ["colon_fence", "deflist", "attrs_block", "attrs_inline"]
myst_url_schemes = {
    "http": None,
    "https": None,
    "mailto": {"url": "mailto:{{path}}", "title": "{{path}}"},
}
# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["files"]
html_extra_path = ["files/license/license.txt", "files/surveys/"]

root_doc = "index"

# -- Internationalization ---------------------------------------------------
language = "en"

intersphinx_mapping = {
    'stable': ('/stable', '../dev-docs/objects.inv'),
    'dev': ('/dev', '../dev-docs/objects.inv'),
    'ct30': ('/3.0', '../api-docs/docs-3.0/sphinx/html/objects.inv'),
    'ct26': ('/2.6', '../api-docs/docs-2.6/sphinx/html/objects.inv'),
}

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_logo = "_static/img/cantera-logo.png"
html_favicon = "_static/img/favicon.png"
html_css_files = ["css/custom.css"]
html_js_files = ["js/copybutton.js"]
html_sidebars: dict[str, list | list[str]] = {
    "index": [],
    "news/**": [
          'ablog/postcard.html', 'ablog/recentposts.html',
          'ablog/tagcloud.html']
}
html_theme_options = {
    "navbar_align": "left",
    "navbar_center": ["initial-sections", "navbar-nav"],
    "navbar_end": ["theme-switcher", "navbar-icon-links"],
    # Search bar is overridden to the stable docs except for the "News" section
    "navbar_persistent": ["search-button-field", "search-stable"],

    "show_prev_next": False,
    "logo": {
        "link": "/index.html",
        "alt_text": "Cantera",
    },
    "github_url": "https://github.com/Cantera/cantera",
    "header_links_before_dropdown": 6,
    # "logo": {
    #     "text": "PyData Theme",
    #     "image_dark": "_static/logo-dark.svg",
    #     "alt_text": "PyData Theme",
    # },
    "use_edit_page_button": True,
    "show_toc_level": 1,
    # [left, content, right] For testing that the navbar items align properly
    # "navbar_center": ["version-switcher", "navbar-nav"],
    # "announcement": "https://raw.githubusercontent.com/pydata/pydata-sphinx-theme/main/docs/_templates/custom-template.html",
    # "show_nav_level": 2,
    # "navbar_start": ["navbar-logo"],
    # "navbar_end": ["theme-switcher", "navbar-icon-links"],
    # "navbar_persistent": ["search-button"],
    # "primary_sidebar_end": ["custom-template.html", "sidebar-ethical-ads.html"],
    # "article_footer_items": ["prev-next.html", "test.html", "test.html"],
    # "content_footer_items": ["prev-next.html", "test.html", "test.html"],
    # "footer_start": ["test.html", "test.html"],
    # "secondary_sidebar_items": ["page-toc.html"],  # Remove the source buttons
    # "switcher": {
    #     "json_url": json_url,
    #     "version_match": version_match,
    # },
}
html_context = {
    "github_user": "cantera",
    "github_repo": "cantera",
    "github_version": "main",
    "doc_path": "docs",
}

# ABlog options
blog_path = "news"
blog_title = "Cantera News"
blog_baseurl = "https://cantera.org"
blog_post_pattern = "news/*"
