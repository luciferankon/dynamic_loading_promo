# -*- coding: utf-8 -*-

import sys, os

# sys.path.insert(0, os.path.abspath('extensions'))

# extensions = ['sphinx.ext.autodoc', 'sphinx.ext.doctest', 'sphinx.ext.todo',
#               'sphinx.ext.coverage', 'sphinx.ext.pngmath', 'sphinx.ext.ifconfig',
#               'epub2', 'mobi', 'autoimage', 'code_example']

source_suffix = '.rst'
master_doc = 'index'
project = u'Gauge'
copyright = u'2018, ThoughtWorks'
author = u'ThoughtWorks'

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'README.md']

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
    'docs_version': 'latest'
}
# html_theme = 'basicstrap'
html_theme_options = {

    # Set the lang attribute of the html tag. Defaults to 'en'
    # 'lang': 'en',
    # Disable showing the sidebar. Defaults to 'false'
    'nosidebar': True,
    # Show header searchbox. Defaults to false. works only "nosidber=True",
    # Set the Size of Heading text. Defaults to None
    # 'h1_size': '3.0em',
    # 'h2_size': '2.6em',
    # 'h3_size': '2.2em',
    # 'h4_size': '1.8em',
    # 'h5_size': '1.4em',
    # 'h6_size': '1.1em',
}
#add_module_names = True
# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# project = u''
# copyright = u''


# -- Options for HTML output ---------------------------------------------------

# html_theme = 'book'
#html_short_title = None
#html_logo = None
#html_favicon = None

#latex_logo = None
#latex_show_urls = False


# -- Options for Code Examples output ---------------------------------------------------


# code_example_dir = "code-example"
# code_add_python_path = ["../py"]


################################################################################


# def setup(app):
#      from sphinx.util.texescape import tex_replacements
#      tex_replacements += [(u'♮', u'$\\natural$'),
#                           (u'ē', u'\=e'),
#                           (u'♩', u'\quarternote'),
#                           (u'↑', u'$\\uparrow$'),
#                           ]