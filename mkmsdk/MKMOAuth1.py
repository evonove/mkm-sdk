from requests_oauthlib import OAuth1
from requests.utils import to_native_string
from six.moves.urllib.parse import unquote


class MKMOAuth1(OAuth1):
    """

    """

    def __call__(self, r):
        r = super(MKMOAuth1, self).__call__(r)

        r.prepare_headers(r.headers)

        correct_signature = self.decode_signature(r.headers)

        r.headers.__setitem__('Authorization', correct_signature)
        r.url = to_native_string(r.url)
        return r

    @staticmethod
    def decode_signature(given_header):
        """
        Decodes the signature given an header. This is done because MKM
        expects an authorization header with different parameters encoding
        specified in section 3.6 of OAuth 1 specification (RFC5849).

        Parameters:
            `given_header`: Authorization header

        Return:
            `authorization_string`: Returns a string of the decoded signature
        """

        authorization_byte = given_header['Authorization']
        authorization_string = authorization_byte.decode()
        signature_position = authorization_string.find('oauth_signature="') + len('oauth_signature="')
        sub_string_signature = authorization_string[signature_position:]

        decoded_sub_string_signature = unquote(sub_string_signature)
        authorization_string = authorization_string[:signature_position]
        authorization_string = "{}{}".format(authorization_string, decoded_sub_string_signature)

        return authorization_string
