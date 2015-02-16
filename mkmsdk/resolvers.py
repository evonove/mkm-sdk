from .api import Api
from . import exceptions


class SimpleResolver:
    """

    """

    def __init__(self, sandbox_mode):
        self.url = ''
        self.method = ''
        self.api = Api(sandbox_mode=sandbox_mode)

    def setup(self, api_map=None, **kwargs):
        """
        Set up the url with required parameters and method of the request

        Params:
            `api_map`: Dict with urls and methods for the request
            `kwargs`: Optional additional parameters to be attached to the url
        """

        url, method = api_map['url'], api_map['method']

        url_entry = {}
        for key in kwargs:
            url_entry[str(key)] = kwargs.get(key)

        try:
            url = url.format(**url_entry)
        except KeyError as ke:
            raise exceptions.MissingParam('Missing url sdk parameter: %s' % str(ke))
        self.url = url
        self.method = method

    def resolve(self, api_map=None, **kwargs):
        """

        Params:
            `api_map`: Dict with urls and methods for the request
            `kwargs`: Optional additional parameters to be attached to the url

        Return:
            `response`: Returns the response received from the server

        """
        self.setup(api_map=api_map, **kwargs)

        return self.api.request(url=self.url, method=self.method)
