import unittest

from oauthlib.common import Request

from mkmsdk.MKMClient import MKMClient


class ClientTest(unittest.TestCase):

    def test_get_oauth_params(self):
        """
        Tests if oauth_token is added to the list of params when an empty string
        """
        client = MKMClient(client_key='app_token',
                           client_secret='app_secret',
                           resource_owner_key='',
                           resource_owner_secret='',
                           realm='https://sandbox.mkmapi.eu',
                           nonce='0987654321',
                           timestamp='1234567890')

        params = client.get_oauth_params(Request(uri='https://sandbox.mkmapi.eu'))

        self.assertEqual(params[0][0], 'oauth_nonce')
        self.assertEqual(params[0][1], '0987654321')
        self.assertEqual(params[1][0], 'oauth_timestamp')
        self.assertEqual(params[1][1], '1234567890')
        self.assertEqual(params[2][0], 'oauth_version')
        self.assertEqual(params[2][1], '1.0')
        self.assertEqual(params[3][0], 'oauth_signature_method')
        self.assertEqual(params[3][1], 'HMAC-SHA1')
        self.assertEqual(params[4][0], 'oauth_consumer_key')
        self.assertEqual(params[4][1], 'app_token')
        self.assertEqual(params[5][0], 'oauth_token')
        self.assertEqual(params[5][1], '')
