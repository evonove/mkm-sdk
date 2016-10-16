# Getting started

To use the SDK the first thing to do is import `mkm` to work on live servers or `mkm_sandbox` to work on the sandbox:

    from mkmsdk.mkm import mkm

    from mkmsdk.mkm import mkm_sandbox


For example to obtain informations about the authenticated account you can make a request like this:

    response = mkm.account_management.account()

This will return a [Response][1] object that contains the response from the server.

If you want get the content of the response you call the `json` method on the `response` object:

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

Similarly to obtain informations about a specific user you can make a request like this:

    response = mkm.market_place.user(user='SampleUser')

Data can be posted directly as an XML string or formatted in a way that the XMLSerializer can parse it to correctly generate an XML string.

For example this:

      data = {
        'action': 'add',
        'article': [
          {'idArticle': 666, 'amount': 2},
          {'idArticle': 101, 'amount': 5}
        ]
      }

serializes to:

      """
      <?xml version="1.0" encoding="utf-8"?>
        <request>
          <action>add</action>
          <article>
            <idArticle>666</idArticle>
            <amount>2</amount>
          </article>
          <article>
            <idArticle>101</idArticle>
            <amount>5</amount>
          </article>
        </request>
      """

It's important that dictionaries are always inside a list or they won't be serialized correctly, so if you have only one article to serialize you format it like this:

    data = {
      'article': [
        {'idArticle': 101, 'amount': 10}
      ]
    }

This is the same format used by the MKM backend for their JSON responses.

[1]: http://docs.python-requests.org/en/latest/api/?highlight=response#requests.Response
