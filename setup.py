#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import os
try:
    import configparser
except ImportError:
    import ConfigParser as configparser

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


version = '0.0.1'


class PyTest(TestCommand):

    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


setup(
    name='gauss_hash',
    version=version,
    description="Gauss Algorithmic Hash Module",
    scripts=['gauss-hash'],
    long_description="",
    classifiers=[],
    author='Jiří Polcar',
    author_email='polcar@gaussalgo.com',
    license='GPL',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        'unidecode',
    ],
)

# vim: set cin et ts=4 sw=4 ft=python :11

