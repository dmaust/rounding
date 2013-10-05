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
    'url': 'https://github.com/dmaust/rounding',
    'download_url': 'http://www.dmaust.net',
    'author_email': 'david@dmaust.net',
    'version': '0.02',
    'install_requires': ['nose'],
    'packages': ['rounding'],
    'scripts': [],
    'classifiers':[ 'Development Status :: 3 - Alpha',
                   'Intended Audience :: Science/Research',
                   'License :: OSI Approved :: Apache Software License' ],

    'license': 'Apache License, Version 2.0',
    'name': 'rounding'
}

setup(**config)
