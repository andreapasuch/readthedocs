# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import sys, os
import recommonmark
from recommonmark.transform import AutoStructify
from recommonmark.parser import CommonMarkParser

source_parsers = {
    '.md': 'recommonmark.parser.CommonMarkParser',
}
extensions = ['sphinx.ext.ifconfig','sphinx_markdown_tables']

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

sys.path.append(os.path.abspath(os.pardir))

__version__ = '1.0'

# -- General configuration -----------------------------------------------------

#source_suffix = '.rst'
source_suffix = ['.rst', '.md']
master_doc = 'index'
project = 'PagoPA'
copyright = '2021, PagoPA'

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

extlinks = {}

# -- Options for HTML output ---------------------------------------------------

html_theme = 'default'

html_static_path = ['static']

def setup(app):
    # overrides for wide tables in RTD theme
    app.add_css_file('theme_overrides.css') # path relative to static

"""
  You might want to uncomment the “latex_documents = []” if you use CKJ characters in your document.
  Because the pdflatex raises exception when generate Latex documents with CKJ characters.
"""
#latex_documents = []

# inserire un logo in alto a sinistra (mettendo l’immagine nella cartella “static”)
latex_logo = "static/pagopa.png"
html_logo = "static/pagopa.png"