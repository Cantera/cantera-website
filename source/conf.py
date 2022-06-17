# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
needs_sphinx = "5.0"


# -- Project information -----------------------------------------------------

project = "Cantera"
copyright = "2022, Cantera Developers"
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
extensions: list[str] = ["myst_parser", "sphinx.ext.duration", "sphinx.ext.mathjax"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["files"]
html_extra_path = ["files/license/license.txt", "files/surveys/"]

root_doc = "contents"

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
html_additional_pages = {"index": "index.html"}
html_sidebars: dict[str, list | list[str]] = {"index": []}
