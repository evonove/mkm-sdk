from oauthlib.common import Request

from mkmsdk.MKMClient import MKMClient


def test_get_oauth_params():
    """Verifies oauth_token is added to the list of params when an empty string."""

    client = MKMClient(client_key='app_token',
                       client_secret='app_secret',
                       resource_owner_key='',
                       resource_owner_secret='',
                       realm='https://sandbox.mkmapi.eu',
                       nonce='0987654321',
                       timestamp='1234567890')

    params = client.get_oauth_params(Request(uri='https://sandbox.mkmapi.eu'))

    assert params[0][0] == 'oauth_nonce'
    assert params[0][1] == '0987654321'
    assert params[1][0] == 'oauth_timestamp'
    assert params[1][1] == '1234567890'
    assert params[2][0] == 'oauth_version'
    assert params[2][1] == '1.0'
    assert params[3][0] == 'oauth_signature_method'
    assert params[3][1] == 'HMAC-SHA1'
    assert params[4][0] == 'oauth_consumer_key'
    assert params[4][1] == 'app_token'
    assert params[5][0] == 'oauth_token'
    assert params[5][1] == ''
