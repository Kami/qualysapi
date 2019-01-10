#!/usr/bin/env python

import os
import sys
import re

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

__author__ = 'Parag Baxi <parag.baxi@gmail.com>'
__copyright__ = 'Copyright 2011-2013, Parag Baxi'
__license__ = 'BSD-new'
# Make pyflakes happy.
__pkgname__ = None
__version__ = None

PKG_ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
os.chdir(PKG_ROOT_DIR)

def get_version_string():
    version_re = re.compile('__version__ = \'(.*?)\'')

    with open(os.path.join(PKG_ROOT_DIR, 'qualysapi/version.py')) as fp:
        content = fp.read()

    match = version_re.search(content)
    version = match.groups()[0]
    return version

# A utility function to read the README file into the long_description field.
def read(fname):
    """ Takes a filename and returns the contents of said file relative to
    the current directory.
    """
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name=__pkgname__,
      version=get_version_string(),
      author='Parag Baxi',
      author_email='parag.baxi@gmail.com',
      description='QualysGuard(R) Qualys API Package',
      license ='BSD-new',
      keywords ='Qualys QualysGuard API helper network security',
      url='https://github.com/paragbaxi/qualysapi',
      package_dir={'': '.'},
      packages=['qualysapi',],
      # package_data={'qualysapi':['LICENSE']},
      # scripts=['src/scripts/qhostinfo.py', 'src/scripts/qscanhist.py', 'src/scripts/qreports.py'],
      long_description=read('README.md'),
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Topic :: Utilities',
          'License :: OSI Approved :: Apache Software License',
          'Intended Audience :: Developers',
      ],
      install_requires=[
          'requests',
          'six',
          'lxml'
      ],
     )
