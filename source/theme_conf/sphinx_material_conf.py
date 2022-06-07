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


# -- Project information -----------------------------------------------------

project = '可持续生活手册'
copyright = '2017-2022, ZeroTogether'
author = '壹个兜子'

# The full version, including alpha/beta/rc tags
release = 'v0.0.1'
master_doc = 'index'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.githubpages',
    'recommonmark',
    'sphinx_markdown_tables',
    'sphinxemoji.sphinxemoji',
    'sphinx_material',
    #'cakephp_theme',
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
    '.txt': 'markdown',
}

sphinxemoji_style = 'twemoji'

# Use custom CSS configs
# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'zh_CN'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'alabaster'
#html_theme = 'sphinx_rtd_theme'
html_theme = 'sphinx_material'
html_title = '可持续生活手册'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = [
    'css/common.css',
    'css/custom.css',
]

html_favicon = '_static/images/zerotogether_favicon_500.png'

html_js_files = [
    'js/baidutongji.js'
]

#---sphinx_material-----
import sphinx_material

html_theme_options = {
    # 'base_url': base_url,
    'color_primary': 'green',  # light-green
    'color_accent': 'orange',
    'logo_icon': '&#xe152',  # &#xe869  &#xe150
    'master_doc': False,

    # Set you GA account ID to enable tracking
    # 'google_analytics_account': 'UA-XXXXX',

    # Set the repo location to get a badge with stats
    'repo_url': 'https://github.com/luhuadong/GreenGuide',
    'repo_name': 'GitHub',

    # Visible levels of the global TOC; -1 means unlimited
    'globaltoc_depth': 2,
    # If False, expand all TOC entries
    'globaltoc_collapse': False,
    # If True, show hidden TOC entries
    'globaltoc_includehidden': False, 

    # An open-source sustainable living guide
    'heroes': {'index': 'An open-source document for writing sustainable living guide',
               '文档结构样式/index': 'Structure, Focus, Unity and Flow',
               '语言风格/index': 'Stay Close to Your Users',
               '文档内容元素/index': 'Details Matter',
               '标点符号/index': 'Details Matter'},
}

html_theme_path = sphinx_material.html_theme_path()
html_context = sphinx_material.get_html_context()
html_sidebars = {
    "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]
}

