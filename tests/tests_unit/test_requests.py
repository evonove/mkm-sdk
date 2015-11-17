import unittest
from ..compat import mock


class RequestsTest(unittest.TestCase):

    def test_request_works(self):
        url = '/metaproducts/island/1/1'
        method = 'get'

        with mock.patch('mkmsdk.api.Api.request') as mock_request:
            mock_request(url, method)

        mock_request.assert_called_once_with(url, method)
