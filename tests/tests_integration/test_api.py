from mkmsdk.api import Api
from . import IntegrationTest


class ApiTest(IntegrationTest):
    def setUp(self):
        self.new_api = Api(sandbox_mode=True)

    def test_good_request(self):
        response = self.new_api.request('/games', 'get')
        self.assertEqual(response.status_code, 200)
