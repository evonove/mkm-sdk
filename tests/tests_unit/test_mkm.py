import unittest
from mkmsdk.mkm import mkm

from ..compat import mock

class MkmTest(unittest.TestCase):

    def test_simple_call(self):
        with mock.patch('mkmsdk.resolvers.SimpleResolver.resolve') as mock_resolve:
            mkm.account_management.account()

            mock_resolve.assert_called_once_with(api_map=mkm.api_map['account_management']['account'])
