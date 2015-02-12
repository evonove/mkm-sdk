from .api import Api
from . import exceptions


class SimpleResolver:
    def __init__(self, sandbox_mode):
        self.url = ''
        self.method = ''
        self.api = Api(sandbox_mode=sandbox_mode)

    def setup(self, api_map=None, url_entry=None):

        url, method = api_map['url'], api_map['method']
        url_entry = url_entry or {}

        try:
            url = url.format(**url_entry)
        except KeyError as ke:
            raise exceptions.MissingParam('Missing url sdk parameter: %s' % str(ke))
        self.url = url
        self.method = method

    def resolve(self, api_map=None, url_entry=None, **kwargs):
        self.setup(api_map=api_map, url_entry=url_entry)

        return self.api.request(url=self.url, method=self.method, **kwargs)
