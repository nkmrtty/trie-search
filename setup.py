#!/usr/bin/env python
# coding: utf-8
from __future__ import absolute_import
from __future__ import unicode_literals

from setuptools import setup, find_packages

try:
    with open('README.rst') as f:
        readme = f.read()
except IOError:
    readme = ''


setup(
    name="trie-search",
    version='0.1.4',
    url='https://github.com/nkmrtty/trie-search',
    author='Tatsuya Nakamura',
    author_email='nkmrtty.com@gmail.com',
    maintainer='Tatsuya Nakamura',
    maintainer_email='nkmrtty.com@gmail.com',
    description='Trie-search is a package for text pattern search using marisa-trie',
    long_description=readme,
    packages=find_packages(),
    install_requires=['marisa-trie'],
    license="MIT",
    classifiers=[
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'License :: OSI Approved :: MIT License',
        'Topic :: Text Processing',
    ], )
