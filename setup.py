# -*- coding: utf-8 -*-
#!/usr/bin/env python
import sys
import os

version = '0.1.0'  # When changing this, please take a moment for doing the same in docs/conf.py
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

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')


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
    install_requires=['requests', 'requests_oauthlib'],
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
