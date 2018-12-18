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

A simple SDK for dedicated and widget apps working with Magic Kard Market.

Contributing
============

Feel free to contribute! Submit `a PR following the guidelines <https://mkm-sdk.readthedocs.io/en/latest/contributing.html#pull-request-guidelines/>`_ and it will be alright.

Requirements
============

* Python 3.4, 3.5, 3.6, 3.7
* `Requests <http://docs.python-requests.org/>`_
* `Requests_OAuthlib <https://github.com/requests/requests-oauthlib/>`_

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


`MKM_ACCESS_TOKEN` and `MKM_ACCESS_TOKEN_SECRET` need to be set to empty string if you want to use a widget app.

Usage
=====

First thing to do is import the `Mkm` class and the API map::

    from mkmsdk.mkm import Mkm
    from mkmsdk.api_map import _API_MAP

Instance a new instance of Mkm::

    # Using API v1.1
    mkm = Mkm(_API_MAP["1.1"]["api"], _API_MAP["1.1"]["api_root"])
    # Using API v2.0
    mkm = Mkm(_API_MAP["2.0"]["api"], _API_MAP["2.0"]["api_root"])

If you want to test on Magic Card Market's sandbox you must use the sandbox root endpoint::

    mkm_sandbox = Mkm(_API_MAP["2.0"]["api"], _API_MAP["2.0"]["api_sandbox_root"])

To make a request::

    response = mkm.account_management.account()

    # Formats an endpoint
    response = mkm.market_place.user(user='SampleUser')

    # Call endpoint with specified parameters
    response = mkm.account_management.vacation(params={"onVacation": "false"})


This will return a `Response <http://docs.python-requests.org/en/latest/api/?highlight=response#requests.Response/>`_
object that contains the response from the server.

Note that only `market_place` requests work when using a widget app.

To get a json you can call response.json().

Tests
=====

Integration tests will be skipped if the four environment variables are not set.

* ``MKM_APP_TOKEN``
* ``MKM_APP_SECRET``
* ``MKM_ACCESS_TOKEN``
* ``MKM_ACCESS_TOKEN_SECRET``

Note that some tests will be skipped depending if `MKM_ACCESS_TOKEN` and `MKM_ACCESS_TOKEN_SECRET` are empty strings or not.
