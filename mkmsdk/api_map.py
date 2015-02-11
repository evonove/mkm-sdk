_API_MAP = {
    'current': {
        'api_root': 'https://www.mkmapi.eu/ws/v1.1/output.json',
        'api_sandbox_root': 'https://sandbox.mkmapi.eu/ws/v1.1/output.json',
        'api': {

            'account_management': {

                'account': {
                    'url': '/account',
                    'method': 'get',
                    'description': 'Get the Account entity of the authenticated user'
                },

                'vacation': {
                    'url': '/account/vacation/{vacation}',
                    'method': 'put',
                    'description': 'Updates the vacation status of the authenticated user; returns the Account entity'
                },

                'put_language': {
                    'url': '/account/language/{language}',
                    'method': 'put',
                    'description': 'Updates the display language of the authenticated user; returns the Account entity'
                },

                'get_messages_thread': {
                    'url': '/account/messages',
                    'method': 'get',
                    'description': 'Get the message thread overview for the authenticated user'
                },

                'get_messages_thread_user': {
                    'url': '/account/messages/{user}',
                    'method': 'get',
                    'description': 'Get a complete message thread between the authenticated user and another user'
                },

                'send_message': {
                    'url': '/account/messages/{user}',
                    'method': 'post',
                    'description': 'Write a message to another user'
                },

                'delete_thread': {
                    'url': '/account/messages/{user}',
                    'method': 'delete',
                    'description': 'Delete all messages between the authenticated and another user'
                },

                'delete_single_message': {
                    'url': '/account/messages/{user}/{message}',
                    'method': 'delete',
                    'description': 'Delete a single message between the authenticated and another user'
                }
            },

            'market_place': {

                'games': {
                    'url': '/games',
                    'method': 'get',
                    'description': 'Returns all games supported by MKM and you can sell and buy cards for'
                },

                'metaproduct': {
                    'url': '/metaproduct/{metaproduct}',
                    'method': 'get',
                    'description': 'Returns the Metaproduct entity for the metaproduct specified by its ID'
                },

                'metaproducts': {
                    'url': '/metaproducts/{name}/{game}/{language}',
                    'method': 'get',
                    'description': 'Returns a metaproduct specified by its exact name, game and language'
                },

                'product': {
                    'url': '/product/{product}',
                    'method': 'get',
                    'description': 'Returns a product specified by its ID '
                },

                'products': {
                    'url': '/products/{name}/{game}/{language}/{match}', #An optional parameter can be inserted for pagination
                    'method': 'get',
                    'description': 'Returns products specified by their name, game and language'
                },

                'expansion': {
                    'url': '/expansion/{game}',
                    'method': 'get',
                    'description': 'Returns Expansion entities for all expansions with single cards for a specific game'
                },

                'expansion_singles': {
                    'url': '/expansion/{game}/{name}',
                    'method': 'get',
                    'description': 'Returns Product entities for all expansions with single cards for a specific game'
                },

                'articles': {
                    'url': '/articles/{product}', #An optional parameter can be inserted for pagination
                    'method': 'get',
                    'description': 'Returns Article entities for available articles specified by their product ID'
                },

                'user': {
                    'url': '/user/{user}',
                    'method': 'get',
                    'description': 'Returns the User entity for the user specified by its ID or exact name'
                },

                'articles_user': {
                    'url': '/articles/user/{user}', #An optional parameter can be inserted for pagination
                    'method': 'get',
                    'description': 'Returns Article entities for available articles from a specified user by ID or name'
                }
            },

            'order_management': {

                'get_order': {
                    'url': '/order/{order}',
                    'method': 'get',
                    'description': 'Returns the Order entity specified by its ID'
                },

                'put_order': {
                    'url': '/order/{order}',
                    'method': 'put',
                    'description': 'Changes the state of an order specified by its ID'
                },

                'order_eval': {
                    'url': '/order/{order}/evaluation',
                    'method': 'post',
                    'description': 'Evaluates an order specified by its ID'
                },

                'orders': {
                    'url': '/orders/{actor}/{state}', #An optional parameter can be inserted for pagination
                    'method': 'get',
                    'description': 'Returns the complete collection of filtered orders.'
                }
            },

            'shopping_cart': {

                'get_shopping_cart': {
                    'url': '/shoppingcart',
                    'method': 'get',
                    'description': 'Returns the shopping cart entity for the authenticated user'
                },

                'put_shopping_cart': {
                    'url': '/shoppingcart',
                    'method': 'put',
                    'description': 'Adds or removes article(s) to or from the authenticated user`s shopping cart'
                },

                'delete_shopping_cart': {
                    'url': '/shoppingcart',
                    'method': 'delete',
                    'description': 'Empties the authenticated user`s shopping cart'
                },

                'checkout': {
                    'url': '/shoppingcart/checkout',
                    'method': 'put',
                    'description': 'Checks out the authenticated user`s shopping cart and creates the respective orders'
                },

                'shipping_address': {
                    'url': '/shoppingcart/shippingaddress',
                    'method': 'put',
                    'description': 'Changes the user`s shipping address for all reservations in the shopping cart'
                },

                'get_shipping_method': {
                    'url': '/shoppingcart/shippingmethod/{method}',
                    'method': 'get',
                    'description': ''
                }
            }

        }
    }
}