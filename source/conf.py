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
    "_extension.bootstrap",
    "_extension.gallery_extension",
]

myst_enable_extensions = ["colon_fence"]
# Add any paths that contain templates here, relative to this directory.
# templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["files"]
html_extra_path = ["files/license/license.txt", "files/surveys/"]

root_doc = "index"

# -- Internationalization ---------------------------------------------------
language = "en"

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
html_favicon = "_static/img/favicon.ico"
html_css_files = ["css/custom.css"]
html_js_files = ["js/copybutton.js"]
html_sidebars: dict[str, list | list[str]] = {"index": []}
html_theme_options = {
    "external_links": [
        {
            "url": "https://numfocus.org/",
            "name": "NumFocus",
        },
        {
            "url": "https://numfocus.org/donate-to-cantera",
            "name": "Donate to NumFocus",
        },
    ],
    "github_url": "https://github.com/Cantera/cantera",
    "twitter_url": "https://twitter.com/cantera-software",
    "header_links_before_dropdown": 6,
    "icon_links": [
        {
            "name": "PyPI",
            "url": "https://pypi.org/project/cantera",
            "icon": "fa-solid fa-box",
        },
    ],
    # "logo": {
    #     "text": "PyData Theme",
    #     "image_dark": "_static/logo-dark.svg",
    #     "alt_text": "PyData Theme",
    # },
    "use_edit_page_button": True,
    "show_toc_level": 1,
    # [left, content, right] For testing that the navbar items align properly
    "navbar_align": "right",
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
