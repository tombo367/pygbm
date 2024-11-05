# conf.py for your Sphinx documentation

import os
import sys
from datetime import datetime

# Add the project's root directory to sys.path to allow imports
sys.path.insert(0, os.path.abspath('..'))  # Adjust the path as necessary

# -- Project information -----------------------------------------------------

project = 'GBM Simulator'  # Name of your project
author = 'Tom Borrett'  # Your name or the name of the author(s)
release = 'beta'
year = datetime.now().year  # Current year for copyright


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
	'nbsphinx',
    'myst_parser',
    'sphinx.ext.autodoc',    # Autodoc extension for extracting docstrings
	'sphinx.ext.mathjax',
	'sphinx_rtd_theme',
    'sphinx_gallery.load_style',  # load CSS for gallery (needs SG >= 0.6)
]



# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'


master_doc = 'index'

highlight_language = 'python3'

nbsphinx_execute_arguments = [
    "--InlineBackend.figure_formats={'svg', 'pdf'}",
    "--InlineBackend.rc={'figure.dpi': 96}",
]


# Disable section numbering
secnumber_suffix = ''  # No suffix means no section numbers# -- Options for manual page output ------------------------------------------

man_pages = [
    (master_doc, 'gbm_simulator', 'GBM Simulator Documentation',
     [author], 1)
]

# -- Options for Texinfo output ----------------------------------------------

texinfo_documents = [
    (master_doc, 'GBM Simulator', 'GBM Simulator Documentation',
     author, 'gbm_simulator', 'One line description of project.',
     'Miscellaneous'),  # The label and category for Texinfo output
]

# -- Options for intersphinx extension ---------------------------------------

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    # Add any other project mappings here
}

# -- Options for extensions --------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',  # Automatically generate documentation from docstrings
    'sphinx.ext.viewcode',  # Add links to highlighted source code
    'sphinx.ext.napoleon',  # Support for Google and NumPy style docstrings
    'sphinx.ext.intersphinx',  # Link to other projects’ documentation
]

# -- Other settings -----------------------------------------------------------

# Set to True to enable the use of mathjax
mathjax_path = 'https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js'

