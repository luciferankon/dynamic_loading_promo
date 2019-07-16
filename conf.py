# -*- coding: utf-8 -*-
#
# Gauge documentation build configuration file, created by
# sphinx-quickstart on Wed Jan  4 14:06:00 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('_ext'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
needs_sphinx = '1.5.2'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.todo', 'sphinx.ext.ifconfig', 'gauge_lexer', 'code_lineno_highlighter', 'tabs', 'sphinx_sitemap']
# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Gauge'
copyright = u'2018, ThoughtWorks'
author = u'ThoughtWorks'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = u'0.9.9'
# The full version, including alpha/beta/rc tags.
release = u'0.9.9'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'README.md']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'monokai'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

site_url = 'https://docs.gauge.org/master/'

html_theme = "gauge_theme"

html_theme_path = ["themes"]

html_context = {
    "display_github": True,
    "last_updated": True,
    "github_user": "getgauge",
    "github_repo": "docs.gauge.org",
    "conf_py_path": "/",
}

html_theme_options = {
    "no-sidebar":True,
    'docs_version': 'latest'
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

html_favicon = "favicon.ico"

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'Gaugedoc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
        # The paper size ('letterpaper' or 'a4paper').
        #
        # 'papersize': 'letterpaper',

        # The font size ('10pt', '11pt' or '12pt').
        #
        # 'pointsize': '10pt',

        # Additional stuff for the LaTeX preamble.
        #
        # 'preamble': '',

        # Latex figure (float) alignment
        #
        # 'figure_align': 'htbp',
        }

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
        (master_doc, 'Gauge.tex', u'Gauge Documentation',
            u'Gauge Team', 'manual'),
        ]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
        (master_doc, 'gauge', u'Gauge Documentation',
            [author], 1)
        ]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
        (master_doc, 'Gauge', u'Gauge Documentation',
            author, 'Gauge', 'One line description of project.',
            'Miscellaneous'),
        ]
