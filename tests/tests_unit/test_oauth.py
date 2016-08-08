from mkmsdk.MKMOAuth1 import MKMOAuth1


def test_header_signature_is_correctly_decoded():
    given_header = {'Authorization': b'oauth_signature="test%20signature"'}
    expected_signature = 'oauth_signature="test signature"'

    decoded_signature = MKMOAuth1.decode_signature(given_header)

    assert decoded_signature == expected_signature
