from requests import request
from oauthlib.oauth1.rfc5849 import Client

from .MKMClient import MKMClient
from . import exceptions
from .utils import get_mkm_app_token, get_mkm_app_secret, get_mkm_access_token, get_mkm_access_token_secret
from .MKMOAuth1 import MKMOAuth1
from .api_map import _API_MAP


class Api:

    def __init__(self, sandbox_mode=False):
        """
        Initializes the endpoint used for requests

        Params:
            `sandbox_mode`: Specifies if sending request to sandbox or live server
        """
        if sandbox_mode:
            self.base_endpoint = _API_MAP['current']['api_sandbox_root']
        else:
            self.base_endpoint = _API_MAP['current']['api_root']

    def request(self, url, method, **kwargs):
        """
        Sends requests to the server with parameters passed

        Params:
            `url`: URL where request is submitted
            `method`: Method used for the requests
            `kwargs`: Optional additional parameters used for the request

        Return:
            `response`: Returns the response received from the server
        """

        complete_url = '{}{}'.format(self.base_endpoint, url)

        auth = self.create_auth(complete_url)

        response = request(method=method, url=complete_url, auth=auth, **kwargs)
        return self.handle_response(response)

    def create_auth(self, url,
                    app_token=None,
                    app_secret=None,
                    access_token=None,
                    access_token_secret=None):
        """
        Create authorization with MKMOAuth1, if Access Token and Access Token Secret
        are not found a custom Client is used.
        This is done because MKM expects an authorization header with certain parameters
        even if they're empty strings.

        Params:
            `url`: URL where request is submitted
            `app_token`: use this app token instead of the one in env vars
            `app_secret`: use this app secret instead of the one in env vars
            `access_token`: use this access token instead of the one in env vars
            `access_token_secret`: use this access token secret instead of the one in env vars

        Return:
            `auth`: Returns an instance of `MKMOAuth1` with `url` as realm
        """

        app_token = app_token if app_token is not None else get_mkm_app_token()
        app_secret = app_secret if app_secret is not None else get_mkm_app_secret()
        access_token = access_token if access_token is not None else get_mkm_access_token()
        access_token_secret = access_token_secret if access_token_secret is not None else get_mkm_access_token_secret()

        # If access_token and access_token_secret are empty strings a personalized OAuth1 Client is used.
        # This is done because that would mean the user is using a Widget Application and having empty strings
        # as tokens causes issues with the default Client
        if not access_token and not access_token_secret:
            client = MKMClient
        else:
            client = Client

        return MKMOAuth1(app_token,
                         client_secret=app_secret,
                         resource_owner_key=access_token,
                         resource_owner_secret=access_token_secret,
                         client_class=client,
                         realm=url)

    def handle_response(self, response):
        """
        Check the HTTP response

        Params:
            `response`: Response received from the server
        Return:
            `response`: Returns the response received if positive or raise exception if negative
        """

        status = response.status_code
        if 200 <= status <= 299:
            return response
        else:
            raise exceptions.ConnectionError(response)
