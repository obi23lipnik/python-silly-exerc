__author__ = 'obi'
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Projekt',
    'author': 'David Lipnik',
    'url': '/',
    'download_url': '/',
    'author_email': 'obi_lipnik@yahoo.co.uk',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex47'],
    'scripts': [],
    'name': 'Projekt'
}

setup(**config)