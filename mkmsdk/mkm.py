from mkmsdk import api_map
from mkmsdk import resolvers

default_api_map = api_map._API_MAP['current']['api']


class Mkm:

    def __init__(self, api_map=None, **kwargs):
        self.api_map = api_map

    def __getattr__(self, name):

        instance = Mkm(api_map=self.api_map[name])
        setattr(self, name, instance)
        return instance

    def __call__(self, *args, **kwargs):
        return self.get_resolver().resolve(api_map=self.api_map, **kwargs)

    def get_resolver(self):
        resolver = resolvers.SimpleResolver()
        return resolver

mkm = Mkm(api_map=default_api_map)
