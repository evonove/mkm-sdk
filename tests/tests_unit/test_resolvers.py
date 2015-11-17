import unittest

from mkmsdk import exceptions
from mkmsdk.resolvers import SimpleResolver


class ResolversTest(unittest.TestCase):
    def setUp(self):
        self.live_resolver = SimpleResolver(sandbox_mode=False)

    def test_if_bad_api_map_is_handled_correctly(self):
        empty_api_map = {}

        self.assertRaises(Exception, self.live_resolver.setup)

        self.assertRaises(Exception, self.live_resolver.setup, empty_api_map)

    def test_if_setup_works_correctly(self):
        simple_api_map = {'url': '/account', 'method': 'get'}
        expected_url = '/account'
        expected_url_with_parameters = '/user/SimpleUser'
        expected_method = 'get'
        simple_api_map_with_parameters = {'url': '/user/{user}', 'method': 'get'}

        self.live_resolver.setup(simple_api_map)

        self.assertEqual(self.live_resolver.url, expected_url)
        self.assertEqual(self.live_resolver.method, expected_method)

        self.live_resolver.setup(simple_api_map_with_parameters, user='SimpleUser')

        self.assertEqual(self.live_resolver.url, expected_url_with_parameters)
        self.assertEqual(self.live_resolver.method, expected_method)

    def test_if_bad_parameters_are_handled_correctly(self):
        simple_api_map_with_parameters = {'url': '/user/{user}', 'method': 'get'}

        self.assertRaises(exceptions.MissingParam, self.live_resolver.setup,
                          simple_api_map_with_parameters)

        self.assertRaises(exceptions.MissingParam, self.live_resolver.setup,
                          simple_api_map_with_parameters, bad_param='Worst parameter ever')
