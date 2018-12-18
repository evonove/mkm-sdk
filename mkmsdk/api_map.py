# flake8: noqa
_API_MAP = {
    "1.1": {
        "api_root": "https://api.cardmarket.com/ws/v1.1/output.json",
        "api_sandbox_root": "https://sandbox.cardmarket.com/ws/v1.1/output.json",
        "api": {
            "account_management": {
                "account": {
                    "url": "/account",
                    "method": "get",
                    "description": "Get the Account entity of the authenticated user",
                },
                "vacation": {
                    "url": "/account/vacation/{vacation}",
                    "method": "put",
                    "description": "Updates the vacation status of the authenticated user; returns the Account entity",
                },
                "put_language": {
                    "url": "/account/language/{language}",
                    "method": "put",
                    "description": "Updates the display language of the authenticated user; returns the Account entity",
                },
                "get_messages_thread": {
                    "url": "/account/messages",
                    "method": "get",
                    "description": "Get the message thread overview for the authenticated user",
                },
                "get_messages_thread_user": {
                    "url": "/account/messages/{user}",
                    "method": "get",
                    "description": "Get a complete message thread between the authenticated user and another user",
                },
                "send_message": {
                    "url": "/account/messages/{user}",
                    "method": "post",
                    "description": "Write a message to another user",
                },
                "delete_thread": {
                    "url": "/account/messages/{user}",
                    "method": "delete",
                    "description": "Delete all messages between the authenticated and another user",
                },
                "delete_single_message": {
                    "url": "/account/messages/{user}/{message}",
                    "method": "delete",
                    "description": "Delete a single message between the authenticated and another user",
                },
            },
            "market_place": {
                "games": {
                    "url": "/games",
                    "method": "get",
                    "description": "Returns all games supported by MKM and you can sell and buy cards for",
                },
                "metaproduct": {
                    "url": "/metaproduct/{metaproduct}",
                    "method": "get",
                    "description": "Returns the Metaproduct entity for the metaproduct specified by its ID",
                },
                "metaproducts": {
                    "url": "/metaproducts/{name}/{game}/{language}",
                    "method": "get",
                    "description": "Returns a metaproduct specified by its exact name, game and language",
                },
                "product": {
                    "url": "/product/{product}",
                    "method": "get",
                    "description": "Returns a product specified by its ID ",
                },
                "products": {
                    "url": "/products/{name}/{game}/{language}/{match}",
                    "method": "get",
                    "description": "Returns products specified by their name, game and language",
                },
                "products_paginated": {
                    "url": "/products/{name}/{game}/{language}/{match}/{start}",
                    "method": "get",
                    "description": "Returns paginated products specified by their name, game and language",
                },
                "expansion": {
                    "url": "/expansion/{game}",
                    "method": "get",
                    "description": "Returns Expansion entities for all expansions with single cards for a specific game",
                },
                "expansion_singles": {
                    "url": "/expansion/{game}/{name}",
                    "method": "get",
                    "description": "Returns Product entities for all expansions with single cards for a specific game",
                },
                "articles": {
                    "url": "/articles/{product}",
                    "method": "get",
                    "description": "Returns Articles entities for available articles specified by their product ID",
                },
                "articles_paginated": {
                    "url": "/articles/{product}/{start}",
                    "method": "get",
                    "description": "Returns paginated Article for available articles specified by their product ID",
                },
                "user": {
                    "url": "/user/{user}",
                    "method": "get",
                    "description": "Returns the User entity for the user specified by its ID or exact name",
                },
                "articles_user": {
                    "url": "/articles/user/{user}",
                    "method": "get",
                    "description": "Returns Article entities for available articles from a specified user ID or name",
                },
                "articles_user_paginated": {
                    "url": "/articles/user/{user}/{start}",
                    "method": "get",
                    "description": "Returns paginated Article for available articles from a specified user ID or name",
                },
            },
            "order_management": {
                "get_order": {
                    "url": "/order/{order}",
                    "method": "get",
                    "description": "Returns the Order entity specified by its ID",
                },
                "put_order": {
                    "url": "/order/{order}",
                    "method": "put",
                    "description": "Changes the state of an order specified by its ID",
                },
                "order_eval": {
                    "url": "/order/{order}/evaluation",
                    "method": "post",
                    "description": "Evaluates an order specified by its ID",
                },
                "orders": {
                    "url": "/orders/{actor}/{state}",
                    "method": "get",
                    "description": "Returns the complete collection of filtered orders.",
                },
                "orders_paginated": {
                    "url": "/orders/{actor}/{state}/{start}",
                    "method": "get",
                    "description": "Returns the paginated complete collection of filtered orders.",
                },
            },
            "shopping_cart": {
                "get_shopping_cart": {
                    "url": "/shoppingcart",
                    "method": "get",
                    "description": "Returns the shopping cart entity for the authenticated user",
                },
                "put_shopping_cart": {
                    "url": "/shoppingcart",
                    "method": "put",
                    "description": "Adds or removes article(s) to or from the authenticated user`s shopping cart",
                },
                "delete_shopping_cart": {
                    "url": "/shoppingcart",
                    "method": "delete",
                    "description": "Empties the authenticated user`s shopping cart",
                },
                "checkout": {
                    "url": "/shoppingcart/checkout",
                    "method": "put",
                    "description": "Checks out the authenticated user`s shopping cart and creates the respective orders",
                },
                "shipping_address": {
                    "url": "/shoppingcart/shippingaddress",
                    "method": "put",
                    "description": "Changes the user`s shipping address for all reservations in the shopping cart",
                },
                "get_shipping_method": {
                    "url": "/shoppingcart/shippingmethod/{method}",
                    "method": "get",
                    "description": "Returns all possible shipping method for the specified reservation",
                },
                "put_shipping_method": {
                    "url": "/shoppingcart/shipping/{method}",
                    "method": "put",
                    "description": "Changes the shipping method of a specified reservation",
                },
            },
            "stock_management": {
                "get_stock": {
                    "url": "/stock",
                    "method": "get",
                    "description": "Returns the Article entities in the authenticated user`s stock",
                },
                "get_stock_paginated": {
                    "url": "/stock/{start}",
                    "method": "get",
                    "description": "Returns the paginated Article entities in the authenticated user`s stock",
                },
                "post_stock": {
                    "url": "/stock",
                    "method": "post",
                    "description": "Adds new articles to the user`s stock",
                },
                "put_stock": {"url": "/stock", "method": "put", "description": "Changes articles in the user`s stock"},
                "delete_stock": {
                    "url": "/stock",
                    "method": "delete",
                    "description": "Removes articles from the user`s stock",
                },
                "get_article": {
                    "url": "/stock/article/{article}",
                    "method": "get",
                    "description": "Returns a single article in the authenticated user`s stock",
                },
                "get_articles": {
                    "url": "/stock/articles/{name}/{game}",
                    "method": "get",
                    "description": "Searches for and returns articles specified by the article`s name and game",
                },
                "increase_stock": {
                    "url": "/stock/increase",
                    "method": "put",
                    "description": "Increase quantities for articles in authenticated user`s stock",
                },
                "decrease_stock": {
                    "url": "/stock/decrease",
                    "method": "put",
                    "description": "Decrease quantities for articles in authenticated user`s stock",
                },
            },
            "wants_list": {
                "get_wants_list": {
                    "url": "/wantslist",
                    "method": "get",
                    "description": "Returns all wants lists for the authenticated user",
                },
                "get_user_wants_list": {
                    "url": "/wantslist/{user}",
                    "method": "get",
                    "description": "Returns all wants lists for the specified user",
                },
                "post_wants_list": {
                    "url": "/wantslist/{wants}",
                    "method": "post",
                    "description": "Creates a new wants list for the authenticated user",
                },
                "put_wants_list": {
                    "url": "/wantslist/{wants}",
                    "method": "put",
                    "description": "Adds, edits, or removes wants to, at, or from a wants list specified by its ID",
                },
                "delete_wants_list": {
                    "url": "/wantslist/{wants}",
                    "method": "delete",
                    "description": "Deletes a wants list specified by its ID for the authenticated user",
                },
            },
        },
    },
    "2.0": {
        "api_root": "https://api.cardmarket.com/ws/v2.0/output.json",
        "api_sandbox_root": "https://sandbox.cardmarket.com/ws/v2.0/output.json",
        "api": {
            "account_management": {
                "account": {
                    "url": "/account",
                    "method": "get",
                    "description": "Get the Account entity of the authenticated user",
                },
                "vacation": {
                    "url": "/account/vacation",
                    "method": "put",
                    "description": "Updates the vacation status of the authenticated user; returns the Account entity",
                },
                "set_language": {
                    "url": "/account/language",
                    "method": "put",
                    "description": "Updates the display language of the authenticated user; returns the Account entity",
                },
                "get_all_threads": {
                    "url": "/account/messages",
                    "method": "get",
                    "description": "Gets message thread overview for the authenticated user",
                },
                "get_thread": {
                    "url": "/account/messages/{user}",
                    "method": "get",
                    "description": "Gets complete message thread between authenticated user and other user",
                },
                "write_message": {
                    "url": "/account/messages/{user}",
                    "method": "post",
                    "description": "Writes a new message to other user",
                },
                "delete_message": {
                    "url": "/account/messages/{user}/{message}",
                    "method": "delete",
                    "description": "Deletes a message sent to other user",
                },
                "delete_thread": {
                    "url": "/account/messages/{user}",
                    "method": "delete",
                    "description": "Deletes all messages sent to other user",
                },
                "find_messages": {
                    "url": "/account/messages/find",
                    "method": "get",
                    "description": "Find messages received by the authenticated user",
                },
                "redeem_coupons": {
                    "url": "/account/messages/coupon",
                    "method": "post",
                    "description": "Redeem one or more coupons for the authenticated user",
                },
                "request_seller_activation": {
                    "url": "/account/selleractivation",
                    "method": "post",
                    "description": "Requests seller activation of authenticated user",
                },
                "complete_seller_activation": {
                    "url": "/account/selleractivation",
                    "method": "put",
                    "description": "Completes seller activation of authenticated user",
                },
            },
            "market_place": {
                "games": {
                    "url": "/games",
                    "method": "get",
                    "description": "Returns all games supported by MKM and you can sell and buy products for",
                },
                "expansions": {
                    "url": "/games/{game}/expansions",
                    "method": "get",
                    "description": "Returns all expansions with single cards for the specified game",
                },
                "expansion_singles": {
                    "url": "/expansions/{expansion}/singles",
                    "method": "get",
                    "description": "Returns all single cards for the specified expansion.",
                },
                "product": {
                    "url": "/products/{product}",
                    "method": "get",
                    "description": "Returns a product specified by its ID",
                },
                "product_list": {
                    "url": "/productslist",
                    "method": "get",
                    "description": "Returns a gzipped CSV file with all relevant products available",
                },
                "price_guide": {
                    "url": "/priceguide",
                    "method": "get",
                    "description": "Returns a gzipped CSV file with relevant price guides for all MtG cards or specified param",
                },
                "find_product": {
                    "url": "/products/find",
                    "method": "get",
                    "description": "Searches for products by a given search string",
                },
                "articles": {
                    "url": "/articles/{product}",
                    "method": "get",
                    "description": "Returns all available articles for a specified product. You can specify parameters for start and maximum results returned",
                },
                "metaproduct": {
                    "url": "/metaproducts/{metaproduct}",
                    "method": "get",
                    "description": "Returns the metaproduct specified by its ID",
                },
                "find_metaproduct": {
                    "url": "/metaproducts/find",
                    "method": "get",
                    "description": "Searches for a metaproduct",
                },
                "user": {
                    "url": "/users/{user}",
                    "method": "get",
                    "description": "Returns the user specified either by its ID, or its exact name",
                },
                "find_user": {
                    "url": "/users/find",
                    "method": "get",
                    "description": "Searches users matching the given search string",
                },
                "user_articles": {
                    "url": "/users/{user}/articles",
                    "method": "get",
                    "description": "Returns all available articles for the specified user",
                },
            },
            "order_management": {
                "get_order": {
                    "url": "/order/{order}",
                    "method": "get",
                    "description": "Returns an order specified by its ID",
                },
                "update_order": {
                    "url": "/order/{order}",
                    "method": "put",
                    "description": "Changes the state of an order specified by its ID",
                },
                "set_tracking_number": {
                    "url": "/order/{order}/tracking",
                    "method": "put",
                    "description": "Provides a tracking number to an order",
                },
                "evaluate_order": {
                    "url": "/order/{order}/evaluation",
                    "method": "post",
                    "description": "Evaluates an order specified by its ID",
                },
                "filter_order": {
                    "url": "/orders/{actor}/{state}",
                    "method": "get",
                    "description": "Returns a collection of orders for the authenticated user",
                },
                "filter_order_paginated": {
                    "url": "/orders/{actor}/{state}/{start}",
                    "method": "get",
                    "description": "Returns a paginated collection of orders for the authenticated user",
                },
            },
            "shopping_cart": {
                "get_cart": {
                    "url": "/shoppingcart",
                    "method": "get",
                    "description": "Gets the authenticated user's shopping cart",
                },
                "update_cart": {
                    "url": "/shoppingcart",
                    "method": "put",
                    "description": "Updates the authenticated user's shopping cart",
                },
                "empty_cart": {
                    "url": "/shoppingcart",
                    "method": "delete",
                    "description": "Empties the authenticated user's shopping cart",
                },
                "checkout": {
                    "url": "/shoppingcart/checkout",
                    "method": "put",
                    "description": "Checks out the authenticated user's shopping cart and creates the respective orders",
                },
                "set_shipping_address": {
                    "url": "/shoppingcart/shippingaddress",
                    "method": "put",
                    "description": "Changes the authenticated user's shipping address for all reservations in the shopping cart",
                },
                "get_shipping_method": {
                    "url": "/shoppingcart/shippingmethod/{reservation}",
                    "method": "get",
                    "description": "Returns the all possible shipping method entities for the specified reservation within the authenticated user's shopping cart",
                },
                "change_shipping_method": {
                    "url": "/shoppingcart/shippingmethod/{reservation}",
                    "method": "put",
                    "description": "Changes the shipping method of a specified reservation in the authenticated user's shopping cart",
                },
            },
            "stock_management": {
                "get_stock": {
                    "url": "/stock",
                    "method": "get",
                    "description": "Returns the Article entities in the authenticated user`s stock",
                },
                "get_stock_file": {
                    "url": "/stock/file",
                    "method": "get",
                    "description": "Returns a gzipped CSV file with all articles in the authenticated user's stock",
                },
                "get_stock_paginated": {
                    "url": "/stock/{start}",
                    "method": "get",
                    "description": "Returns the paginated Article entities in the authenticated user`s stock",
                },
                "add_articles": {
                    "url": "/stock",
                    "method": "post",
                    "description": "Add an article in the authenticated user's stock",
                },
                "change_articles": {
                    "url": "/stock",
                    "method": "put",
                    "description": "Change articles in the authenticated user's stock",
                },
                "delete_articles": {
                    "url": "/stock",
                    "method": "delete",
                    "description": "Delete articles in the authenticated user's stock",
                },
                "get_stock_in_cart": {
                    "url": "/shoppingcart-articles",
                    "method": "get",
                    "description": "Returns the articles of the authenticated user's stock that are currently in other user's shopping carts",
                },
                "get_stock_article": {
                    "url": "/stock/article/{article}",
                    "method": "get",
                    "description": "Returns a single article in the authenticated user's stock",
                },
                "find_stock_articles": {
                    "url": "/stock/articles/{name}/{game}",
                    "method": "get",
                    "description": "Searches for articles in the authenticated user's stock",
                },
                "increase_stock_articles_quantity": {
                    "url": "/stock/increase",
                    "method": "put",
                    "description": "Increase articles' quantities in authenticated user's stock",
                },
                "decrease_stock_articles_quantity": {
                    "url": "/stock/decrease",
                    "method": "put",
                    "description": "Decrease articles' quantities in authenticated user's stock",
                },
            },
            "wants_list": {
                "get_wants_list": {
                    "url": "/wantslist",
                    "method": "get",
                    "description": "Returns wants list of the authenticated user",
                },
                "create_wants_list": {
                    "url": "/wantslist",
                    "method": "post",
                    "description": "Creates a new wants list for the authenticated user",
                },
                "get_wants_list": {
                    "url": "/wantslist/{wants}",
                    "method": "get",
                    "description": "Returns the single specified wants list with its details and items"
                },
                "edit_wants_list": {
                    "url": "/wantslist/{wants}",
                    "method": "put",
                    "description": "Changes details of the specified wants list or manages its items"
                },
                "delete_wants_list": {
                    "url": "/wantslist/{wants}",
                    "method": "delete",
                    "description": "Deletes the specified wants list and all items in it"
                }
            },
        },
    },
}
