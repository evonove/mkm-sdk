from requests import request
from oauthlib.oauth1.rfc5849 import Client

from .MKMClient import MKMClient
from . import exceptions
from .utils import get_mkm_app_token, get_mkm_app_secret, get_mkm_access_token, get_mkm_access_token_secret
from .MKMOAuth1 import MKMOAuth1


class Api:
    def __init__(self, base_endpoint):
        """
        Initializes the endpoint used for requests
        """
        self.base_endpoint = base_endpoint

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

        complete_url = "{}{}".format(self.base_endpoint, url)

        auth = self.create_auth(complete_url)

        # Some MKM endpoints might return a 3xx status code but they're not meant to be followed
        # so disable auto follow of redirections.
        # For more info see the official MKM documentation:
        # https://www.mkmapi.eu/ws/documentation/API_1.1:Main_Page#307_Temporary_Redirect
        response = request(method=method, url=complete_url, auth=auth, allow_redirects=False, **kwargs)
        return self.handle_response(response)

    def create_auth(self, url, app_token=None, app_secret=None, access_token=None, access_token_secret=None):
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

        return MKMOAuth1(
            app_token,
            client_secret=app_secret,
            resource_owner_key=access_token,
            resource_owner_secret=access_token_secret,
            client_class=client,
            realm=url,
        )

    def handle_response(self, response):
        """
        Check the HTTP response

        Params:
            `response`: Response received from the server
        Return:
            `response`: Returns the response received if positive or raise exception if negative
        """

        # We don't automatically follow redirects so accept those responses
        if 200 <= response.status_code <= 399:
            return response
        else:
            raise exceptions.ConnectionError(response)
