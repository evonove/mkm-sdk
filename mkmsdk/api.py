import os
from .api_map import _API_MAP
from . import exceptions
from requests import request
from .MKMOAuth1 import MKMOAuth1


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

        try:
            response = request(method=method, url=complete_url, auth=auth, **kwargs)
            return self.handle_response(response, response.content)
        except exceptions.BadRequest as error:
            return {'error': error.content}

    def create_auth(self, url):
        """
        Create authorization with MKMOAuth1

        Params:
            `url`: URL where request is submitted

        Return:
            `auth`: Returns an instance of `MKMOAuth1` with `url` as realm
        """


        try:
            auth = MKMOAuth1(os.environ['MKM_APP_TOKEN'],
                                client_secret=os.environ['MKM_APP_SECRET'],
                                resource_owner_key=os.environ['MKM_ACCESS_TOKEN'],
                                resource_owner_secret=os.environ['MKM_ACCESS_TOKEN_SECRET'],
                                realm=url)
        except KeyError:
            raise exceptions.MissingConfig('You have to set MKM env vars')
        return auth

    def handle_response(self, response, content):
        """
        Check the HTTP response

        Params:
            `response`: Response received from the server
            `content`: Content of the response received
        Return:
            `response`: Returns the response received if positive or raise exception if negative
        """

        status = response.status_code
        if status in (301, 302, 303, 307):
            raise exceptions.Redirection(response, content)
        elif 200 <= status <= 299:
            return response
        elif status == 400:
            raise exceptions.BadRequest(response, content)
        elif status == 401:
            raise exceptions.UnauthorizedAccess(response, content)
        elif status == 403:
            raise exceptions.ForbiddenAccess(response, content)
        elif status == 404:
            raise exceptions.ResourceNotFound(response, content)
        elif status == 405:
            raise exceptions.MethodNotAllowed(response, content)
        elif status == 409:
            raise exceptions.ResourceConflict(response, content)
        elif status == 410:
            raise exceptions.ResourceGone(response, content)
        elif status == 422:
            raise exceptions.ResourceInvalid(response, content)
        elif 401 <= status <= 499:
            raise exceptions.ClientError(response, content)
        elif 500 <= status <= 599:
            raise exceptions.ServerError(response, content)
        else:
            raise exceptions.ConnectionError(response, content, "Unknown response code: #{response.code}")
