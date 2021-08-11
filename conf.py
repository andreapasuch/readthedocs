import recommonmark
from recommonmark.transform import AutoStructify

from recommonmark.parser import CommonMarkParser

source_parsers = {
    '.md': 'recommonmark.parser.CommonMarkParser',
}

source_suffix = ['.rst', '.md']

extensions = ['sphinx.ext.ifconfig','sphinx_markdown_tables']