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
copyright = '2024, Tom Borrett'
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


