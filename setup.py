'''
Created on Sep 22, 2013

@author: dmaust
'''

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Stochastic Rounding',
    'author': 'David Maust',
    'url': 'http://www.dmaust.net/',
    'download_url': 'http://www.dmaust.net',
    'author_email': 'david@dmaust.net',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['rounding'],
    'scripts': [],
    'name': 'rounding'
}

setup(**config)