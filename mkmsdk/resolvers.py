from six.moves import urllib_parse

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

        if api_map is None:
            raise Exception('Resolve must be called with `api_map` argument')
        elif api_map.get('url') is None or api_map.get('method') is None:
            raise Exception('Resolve must be called with a map with `url` and `method`')

        url = api_map['url']
        method = api_map['method']

        try:
            url = url.format(**kwargs)
        except KeyError as ke:
            raise exceptions.MissingParam('Missing url sdk parameter: %s' % str(ke))

        # We percent encode the url so that if any string has spaces,
        # commas or any other special character the url will be correctly formed anyway
        self.url = urllib_parse.quote(url)
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
