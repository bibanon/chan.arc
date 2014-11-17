#!/usr/bin/env python
# coding: utf-8

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

with open('../README.rst') as file:
    long_description = file.read()


setup(
    name='chan_arc',
    version='0.0.1',
    description='Imageboard Archiving Format reference library (stub, no code yet).',
    long_description=long_description,
    author='Daniel Oaks <daniel@danieloaks.net>',
    author_email='daniel@danieloaks.net',
    url='https://github.com/DanielOaks/chan.arc',
    keywords='4chan imageboard archive archiving',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: Public Domain',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ]
)
