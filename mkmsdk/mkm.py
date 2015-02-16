from . import api_map
from . import resolvers

default_api_map = api_map._API_MAP['current']['api']


class Mkm:

    def __init__(self, api_map=None, **kwargs):
        """
        Initializes the api_map and eventual sandbox mode

        Params:
            `api_map`: Dict with urls and methods for the request
            `kwargs`: Custom arguments that may specify if sandbox should be used

        """
        self.api_map = api_map
        self.sandbox_mode = kwargs.get('sandbox_mode')

    def __getattr__(self, name):
        """
        Used to get inside the api_map

        Params:
            `name`: api_map entry to get

        Returns:
            `instance`: Return an instance of Mkm with updated api_map
        """

        instance = Mkm(api_map=self.api_map[name], sandbox_mode=self.sandbox_mode)
        setattr(self, name, instance)
        return instance

    def __call__(self, *args, **kwargs):
        """
        Here is where the request happens

        Params:
            `kwargs`: May contain eventual parameters for the request

        Returns:
            `response`: Returns the response from the server
        """

        resolver = resolvers.SimpleResolver(self.sandbox_mode)
        return resolver.resolve(api_map=self.api_map, **kwargs)

mkm = Mkm(api_map=default_api_map)
mkm_sandbox = Mkm(api_map=default_api_map, sandbox_mode=True)
