# Getting started

To use the SDK the first thing to do is import the `Mkm` class and the API map:

    from mkmsdk.mkm import Mkm
    from mkmsdk.api_map import _API_MAP

Create a new instance:

    # Using API v1.1
    mkm = Mkm(_API_MAP["1.1"]["api"], _API_MAP["1.1"]["api_root"])
    # Using API v2.0
    mkm = Mkm(_API_MAP["2.0"]["api"], _API_MAP["2.0"]["api_root"])

If you want to test on Magic Card Market's sandbox you must use the sandbox root endpoint:

    mkm_sandbox = Mkm(_API_MAP["2.0"]["api"], _API_MAP["2.0"]["api_sandbox_root"])

Now you're ready to send requests.

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

This would format the url `https://api.cardmarket.com/ws/v1.1/output.json/user/{user}` into `https://api.cardmarket.com/ws/v1.1/output.json/user/SampleUser` and send a request.

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

This is the same format used by Magic Card Market's backend for their JSON responses.

That `data` can be sent over with your request by passing it as an argument:

    mkm.shopping_cart.update_cart(data=data)


Some requests have also custom parameters that must be passed as argument to send the request successfully.

    mkm.account_management.vacation(params={"onVacation": "false"})

This call will be formatted as such `https://api.cardmarket.com/ws/v2.0/account/vacation?onVacation=false`.

To request the export of Article entities from a specific user specified by its ID:

    r = mkm.market_place.create_export_user_offers(user_id=SampleUser)

The response 202 indicates the request has been accepted and the export will be available for download in a few minutes.

To get details for a requested export of Article entities from a specific user specified by its ID.

    r = mkm.market_place.get_export_user_offers(user_id=SampleUser)

The download `url` will be available if `r.json()['userOffersRequests']['status']` is `finished`:

        r.json()['userOffersRequests']['url']
    
[1]: http://docs.python-requests.org/en/latest/api/?highlight=response#requests.Response
