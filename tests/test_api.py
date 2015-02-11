import unittest
from unittest import mock
from mkmsdk.api import Api


class ApiTest(unittest.TestCase):

    def setUp(self):
        self.base_endpoint = 'https://www.mkmapi.eu/ws/v1.1/output.json'
        self.new_api = Api()
        self.new_api.request = mock.Mock()

    def test_endpoint(self):
        self.assertEqual(self.new_api.base_endpoint, self.base_endpoint)

    def test_get(self):
        self.new_api.request('/account', 'get')
        self.new_api.request.assert_called_once_with('/account', 'get')
