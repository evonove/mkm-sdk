from . import resolvers


class Mkm:
    def __init__(self, api_map, root_endpoint):
        """
        Initializes the api_map and eventual sandbox mode

        Params:
            `api_map`: Dict with urls and methods for the request
            `root_endpoint`: Api root endpoint
        """
        self.api_map = api_map
        self.root_endpoint = root_endpoint
        self.resolver = resolvers.SimpleResolver(self.root_endpoint)

    def __getattr__(self, name):
        """
        Used to get inside the api_map

        Params:
            `name`: api_map entry to get

        Returns:
            `instance`: Return an instance of Mkm with updated api_map
        """

        instance = Mkm(api_map=self.api_map[name], root_endpoint=self.root_endpoint)
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

        return self.resolver.resolve(api_map=self.api_map, **kwargs)
