# -*- coding: utf-8 -*-
#!/usr/bin/env python
from distutils.core import setup
setup(
    name='mkmsdk',
    version='0.1.0',
    author='Evonove',
    author_email='dev@evonove.it',
    packages=['mkmsdk', 'tests'],
    scripts=[],
    url='https://evonove.it',
    license='MIT',
    description='MagicKardMarket base sdk.',
    long_description="""
    MagicKardMarket sdk with use of some endpoints.
    """,
    install_requires=['requests', 'requests_oauthlib'],
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    keywords="mkm magickardmarket magiccardmarket sdk",
)
