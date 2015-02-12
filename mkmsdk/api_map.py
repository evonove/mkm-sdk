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
                    'url': '/products/{name}/{game}/{language}/{match}',
                    'method': 'get',
                    'description': 'Returns products specified by their name, game and language'
                },

                'products_paginated': {
                  'url': '/products/{name}/{game}/{language}/{match}/{start}',
                  'method': 'get',
                  'description': 'Returns paginated products specified by their name, game and language'
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
                    'url': '/articles/{product}',
                    'method': 'get',
                    'description': 'Returns Articles entities for available articles specified by their product ID'
                },

                'articles_paginated': {
                    'url': '/articles/{product}/{start}',
                    'method': 'get',
                    'description': 'Returns paginated Article for available articles specified by their product ID'
                },

                'user': {
                    'url': '/user/{user}',
                    'method': 'get',
                    'description': 'Returns the User entity for the user specified by its ID or exact name'
                },

                'articles_user': {
                    'url': '/articles/user/{user}',
                    'method': 'get',
                    'description': 'Returns Article entities for available articles from a specified user ID or name'
                },

                'articles_user_paginated': {
                    'url': '/articles/user/{user}/{start}',
                    'method': 'get',
                    'description': 'Returns paginated Article for available articles from a specified user ID or name'
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
                    'url': '/orders/{actor}/{state}',
                    'method': 'get',
                    'description': 'Returns the complete collection of filtered orders.'
                },

                'orders_paginated': {
                    'url': '/orders/{actor}/{state}/{start}',
                    'method': 'get',
                    'description': 'Returns the paginated complete collection of filtered orders.'
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
                    'description': 'Returns all possible shipping method for the specified reservation'
                },

                'put_shipping_method': {
                    'url': '/shoppingcart/shipping/{method}',
                    'method': 'put',
                    'description': 'Changes the shipping method of a specified reservation'
                }
            },

            'stock_management': {

                'get_stock': {
                    'url': '/stock',
                    'method': 'get',
                    'description': 'Returns the Article entities in the authenticated user`s stock'
                },

                'get_stock_paginated': {
                    'url': '/stock/{start}',
                    'method': 'get',
                    'description': 'Returns the paginated Article entities in the authenticated user`s stock'
                },

                'post_stock': {
                    'url': '/stock',
                    'method': 'post',
                    'description': 'Adds new articles to the user`s stock'
                },

                'put_stock': {
                    'url': '/stock',
                    'method': 'put',
                    'description': 'Changes articles in the user`s stock'
                },

                'delete_stock': {
                    'url': '/stock',
                    'method': 'delete',
                    'description': 'Removes articles from the user`s stock'
                },

                'get_article': {
                    'url': '/stock/article/{article}',
                    'method': 'get',
                    'description': 'Returns a single article in the authenticated user`s stock'
                },

                'get_articles': {
                    'url': '/stock/articles/{name}/{game}',
                    'method': 'get',
                    'description': 'Searches for and returns articles specified by the article`s name and game'
                },

                'increase_stock': {
                    'url': '/stock/increase',
                    'method': 'put',
                    'description': 'Increase quantities for articles in authenticated user`s stock'
                },

                'decrease_stock': {
                    'url': '/stock/decrease',
                    'method': 'put',
                    'description': 'Decrease quantities for articles in authenticated user`s stock'
                }
            },

            'wants_list': {

                'get_wants_list': {
                    'url': '/wantslist',
                    'method': 'get',
                    'description': 'Returns all wants lists for the authenticated user'
                },

                'get_user_wants_list': {
                    'url': '/wantslist/{user}',
                    'method': 'get',
                    'description': 'Returns all wants lists for the specified user'
                },

                'post_wants_list': {
                    'url': '/wantslist/{wants}',
                    'method': 'post',
                    'description': 'Creates a new wants list for the authenticated user'
                },

                'put_wants_list': {
                    'url': '/wantslist/{wants}',
                    'method': 'put',
                    'description': 'Adds, edits, or removes wants to, at, or from a wants list specified by its ID'
                },

                'delete_wants_list': {
                    'url': '/wantslist/{wants}',
                    'method': 'delete',
                    'description': 'Deletes a wants list specified by its ID for the authenticated user'
                }
            }
        }
    }
}
