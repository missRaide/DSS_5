#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='shared',
      version='0.0.1',
      description='This package has shared components.',
      author='Susma Rai',
      author_email='missrai.de@email.com',
      packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
      license='LICENSE.txt',
    )