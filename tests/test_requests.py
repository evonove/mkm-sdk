import unittest
from mkmsdk.api import Api


class RequestsTest(unittest.TestCase):
    def setUp(self):
        self.url = '/metaproducts/island/1/1'
        self.method = 'get'

    def test_request_works(self):
        api = Api()
        response = api.request(self.url, self.method)

        self.assertEqual(response.status_code, 200)
