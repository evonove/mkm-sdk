Magic Kard Market Python SDK
============================

.. image:: https://badge.fury.io/py/mkmsdk.png
    :target: http://badge.fury.io/py/mkmsdk

.. image:: https://readthedocs.org/projects/mkm-sdk/badge/?version=latest
    :target: http://mkm-sdk.readthedocs.org/en/latest/
    
.. image:: https://coveralls.io/repos/evonove/mkm-sdk/badge.svg
  :target: https://coveralls.io/r/evonove/mkm-sdk

.. image:: https://travis-ci.org/evonove/mkm-sdk.svg
    :target: https://travis-ci.org/evonove/mkm-sdk

A simple SDK for dedicated apps working with Magic Kard Market.

Requirements
============

* Python 2.7/3.4
* [Requests](http://docs.python-requests.org/)
* [Requests_OAuthlib](https://github.com/requests/requests-oauthlib)

Setup
=====

From the command line::

    pip install mkmsdk

For the SDK to work properly you need to create four environment variables holding the tokens necessary to create the
authorization to make requests. You can find them in your Magic Kard Market account page under the apps section.

* ``MKM_APP_TOKEN``
* ``MKM_APP_SECRET``
* ``MKM_ACCESS_TOKEN``
* ``MKM_ACCESS_TOKEN_SECRET``


Usage
=====

First thing to do is import `mkm` to work on live servers or `mkm_sandbox` for the sandbox::

    from mkmsdk.mkm import mkm, mkm_sandbox

A request works like this::

    response = mkm.account_management.account()

    response = mkm.market_place.user(user='SampleUser')

This will return a `Response <http://docs.python-requests.org/en/latest/api/?highlight=response#requests.Response/>`_
object that contains the response from the server.

To get a json you can call response.json().
