=====
Usage
=====

To use the SDK the first thing to do is import `mkm` to work on live servers or `mkm_sandbox` to work on the sandbox::

    from mkmsdk.mkm import mkm

    from mkmsdk.mkm import mkm_sandbox


A request works like this::

    response = mkm.account_management.account()

    response = mkm.market_place.user(user='SampleUser')

This will return a `Response <http://docs.python-requests.org/en/latest/api/?highlight=response#requests.Response/>`_
object that contains the response from the server.

To get a json you can call response.json().