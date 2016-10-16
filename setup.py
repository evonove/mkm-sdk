# -*- coding: utf-8 -*-
# !/usr/bin/env python

from setuptools import setup, find_packages
import sys
import os
import re


def get_version(package):
    """
    Return package version as listed in `__version__` in `__init__.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)

version = get_version('mkmsdk')


LONG_DESCRIPTION = open('README.rst').read()


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist bdist_wheel')
    os.system('twine upload dist/*')
    print("You probably want to also tag the version now:")
    print(" git tag -a %s -m '%s'" % (version, version))
    print(" git push --tags")
    sys.exit()


setup(
    name='mkmsdk',
    version=version,
    author='Evonove',
    author_email='dev@evonove.it',
    packages=find_packages(exclude=['docs', 'tests*']),
    scripts=[],
    url='https://evonove.it',
    license='MIT',
    description='MagicKardMarket sdk',
    long_description=LONG_DESCRIPTION,
    install_requires=['requests', 'requests_oauthlib', 'six'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    keywords="mkm magickardmarket magiccardmarket sdk",
)
