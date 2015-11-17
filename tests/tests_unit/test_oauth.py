import unittest

from mkmsdk.MKMOAuth1 import MKMOAuth1


class OAuthTest(unittest.TestCase):

    def test_header_signature_is_correctly_decoded(self):
        given_header = {'Authorization': b'oauth_signature="test%20signature"'}
        expected_signature = 'oauth_signature="test signature"'


        decoded_signature = MKMOAuth1.decode_signature(given_header)
        self.assertEqual(decoded_signature, expected_signature)

