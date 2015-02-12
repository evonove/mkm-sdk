from . import api_map
from . import resolvers

default_api_map = api_map._API_MAP['current']['api']


class Mkm:

    def __init__(self, api_map=None, **kwargs):
        self.api_map = api_map
        self.sandbox_mode = kwargs.get('sandbox_mode')

    def __getattr__(self, name):

        instance = Mkm(api_map=self.api_map[name], sandbox_mode=self.sandbox_mode)
        setattr(self, name, instance)
        return instance

    def __call__(self, *args, **kwargs):
        resolver = resolvers.SimpleResolver(self.sandbox_mode)
        return resolver.resolve(api_map=self.api_map, **kwargs)

mkm = Mkm(api_map=default_api_map)
mkm_sandbox = Mkm(api_map=default_api_map, sandbox_mode=True)
