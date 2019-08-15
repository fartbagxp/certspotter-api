#!/usr/bin/env python

from distutils.core import setup
setup(name='certspotter',
      version='1.0',
      description='sslmate CertSpotter API'
      author='Boris Ning',
      author_email='fartbagxp@gmail.com',
      py_modules=['certspotter'],
      packages=['certspotter'],
      package_dir={'certspotter': 'src/certspotter'},
      license='MIT')
