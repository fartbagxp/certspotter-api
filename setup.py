#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from setuptools import setup
from setuptools.command.install import install

VERSION = "1.0.9"


def readme():
  """print long description"""
  with open('README.md') as f:
    return f.read()


setup(name='certspotter',
      version=VERSION,
      description='sslmate CertSpotter API',
      long_description=readme(),
      long_description_content_type="text/markdown",
      url="https://github.com/fartbagxp/certspotter-api",
      author='Boris Ning',
      author_email='fartbagxp@gmail.com',
      py_modules=['certspotter'],
      packages=['certspotter'],
      package_dir={'certspotter': 'src/certspotter'},
      license='MIT')
