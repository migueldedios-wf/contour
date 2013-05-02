#!/usr/bin/env python

import os
import sys

import contour

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

packages = [
    'contour',
]

requires = []

setup(
    name='contour',
    version=contour.__version__,
    description='Python configuration.',
    long_description=open('README.md').read() + '\n\n' +
                     open('HISTORY.md').read(),
    author='Beau Lyddon',
    author_email='beau.lyddon@webfilings.com',
    url='http://github.com/beaulyddon-wf/contour',
    packages=packages,
    package_data={'': ['LICENSE', 'NOTICE'], 'contour': ['*.pem']},
    package_dir={'contour': 'contour'},
    include_package_data=True,
    install_requires=requires,
    setup_requires=['sphinx'],
    license=open('LICENSE').read(),
    zip_safe=False,
    classifiers=(
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ),
)