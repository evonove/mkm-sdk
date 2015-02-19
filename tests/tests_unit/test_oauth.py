import unittest
from mkmsdk.MKMOAuth1 import MKMOAuth1


class OAuthTest(unittest.TestCase):
    def setUp(self):
        self.given_header = {'Authorization': b'oauth_signature="test%20signature"'}
        self.expected_signature = 'oauth_signature="test signature"'

    def test_header_signature_is_correctly_decoded(self):
        decoded_signature = MKMOAuth1.decode_signature(self.given_header)
        self.assertEqual(decoded_signature, self.expected_signature)

