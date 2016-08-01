=====
Usage
=====

To use the SDK the first thing to do is import `mkm` to work on live servers or `mkm_sandbox` to work on the sandbox::

    from mkmsdk.mkm import mkm

    from mkmsdk.mkm import mkm_sandbox


For example to obtain informations about the authenticated account you can make a request like this::

    response = mkm.account_management.account()

This will return a `Response <http://docs.python-requests.org/en/latest/api/?highlight=response#requests.Response/>`_
object that contains the response from the server.

If you want get the content of the response you call the `json` method on the `response` object::

    response.json()

    {'account': {'name': {'firstName': 'Luke' 'lastName': 'Skywalker'},
      'country': 'DE',
      'isCommercial': 0,
      'riskGroup': 1,
      'bankRecharge': 0,
      'idUser': 123456,
      'sellCount': 0,
      'paypalRecharge': 0,
      'shipsFast': 0,
      'unreadMessages': 0,
      'username': 'SkyWalker',
      'onVacation': False,
      'reputation': 0,
      'articlesInShoppingCart': 0,
      'address': {'name': 'Luke Skywalker',
       'extra': '',
       'country': 'DE',
       'zip': '12345',
       'street': 'Tatooine',
       'city': 'Tatooine'},
      'idDisplayLanguage': 5,
      'accountBalance': 0}}

Similarly to obtain informations about a specific user you can make a request like this::

    response = mkm.market_place.user(user='SampleUser')

Note that if you need to send data to MKM backend it has to be XML or it will return a 400 Bad Request.