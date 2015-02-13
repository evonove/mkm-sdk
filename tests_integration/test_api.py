from . import IntegrationTest

from mkmsdk.api import Api


class ApiTest(IntegrationTest):
    def setUp(self):
        self.new_api = Api()

    def test_good_request(self):
        response = self.new_api.request('/account', 'get')
        self.assertEqual(response.status_code, 200)
