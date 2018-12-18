from urllib.parse import quote

from .api import Api
from . import exceptions
from .serializer import XMLSerializer


class SimpleResolver:
    """

    """

    def __init__(self, main_endpoint):
        self.url = ""
        self.method = ""
        self.api = Api(main_endpoint)

    def setup(self, api_map=None, **kwargs):
        """
        Set up the url with required parameters and method of the request

        Params:
            `api_map`: Dict with urls and methods for the request
            `kwargs`: Optional additional parameters to be attached to the url
        """

        if api_map is None:
            raise Exception("Resolve must be called with `api_map` argument")
        elif api_map.get("url") is None or api_map.get("method") is None:
            raise Exception("Resolve must be called with a map with `url` and `method`")

        url = api_map["url"]
        method = api_map["method"]

        try:
            url = url.format(**kwargs)
        except KeyError as param:
            raise exceptions.MissingParam(param=param)

        # We percent encode the url so that if any string has spaces,
        # commas or any other special character the url will be correctly formed anyway
        self.url = quote(url)
        self.method = method

    def resolve(self, api_map=None, data=None, params=None, **kwargs):
        """
        Params:
            `api_map`: Dict with urls and methods for the request
            `data`: Data sent to MKM in PUT, POST and DELETE requests
            `kwargs`: Optional additional parameters to be attached to the url

        Return:
            `response`: Returns the response received from the server
        """
        self.setup(api_map=api_map, **kwargs)

        if isinstance(data, dict):
            serializer = XMLSerializer()
            data = serializer.serialize(data=data)

        return self.api.request(url=self.url, method=self.method, data=data, params=params)
