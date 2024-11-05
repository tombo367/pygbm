import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.abspath('..'))

project = 'GBM Simulator'
author = 'Tom Borrett'
release = 'beta'
copyright = '2024, Tom Borrett'
year = datetime.now().year

extensions = [
    'nbsphinx',
    'myst_parser',
    'sphinx.ext.autodoc',
    'sphinx.ext.mathjax',
    'sphinx_rtd_theme',
    'sphinx_gallery.load_style',
]

# NBSphinx settings
nbsphinx_execute = 'never'  # Don't execute notebooks during build
nbsphinx_allow_errors = True  # Continue building even if there are notebook errors

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '**.ipynb_checkpoints']

html_theme = 'sphinx_rtd_theme'
