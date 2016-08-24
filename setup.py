# -*- coding: utf-8 -*-
# !/usr/bin/env python
import sys
import os

version = '0.3.0'

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print(" git tag -a %s -m 'version %s'" % (version, version))
    print(" git push --tags")
    sys.exit()


setup(
    name='mkmsdk',
    version=version,
    author='Evonove',
    author_email='dev@evonove.it',
    packages=['mkmsdk', 'tests'],
    scripts=[],
    url='https://evonove.it',
    license='MIT',
    description='MagicKardMarket base sdk',
    long_description="""
    Magic Kard Market sdk with use of some endpoints
    """,
    install_requires=['requests', 'requests_oauthlib', 'six'],
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    keywords="mkm magickardmarket magiccardmarket sdk",
)
