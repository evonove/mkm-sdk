import unittest
from unittest import mock


class RequestsTest(unittest.TestCase):
    def setUp(self):
        self.url = '/metaproducts/island/1/1'
        self.method = 'get'

    def test_request_works(self):
        """

        """
        with mock.patch('mkmsdk.api.Api.request') as mock_request:
            mock_request(self.url, self.method)

        mock_request.assert_called_once_with(self.url, self.method)
