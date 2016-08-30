import os
from . import missing_app_tokens, missing_widget_tokens

import requests
from requests_oauthlib import OAuth1

from mkmsdk.MKMOAuth1 import MKMOAuth1
from mkmsdk.MKMClient import MKMClient


@missing_app_tokens
def test_oauth_is_received():
    """Verifies if OAuth1 is received."""
    url = 'https://sandbox.mkmapi.eu/ws/v1.1/output.json/games'
    auth = MKMOAuth1(os.environ.get('MKM_APP_TOKEN'),
                     client_secret=os.environ.get('MKM_APP_SECRET'),
                     resource_owner_key=os.environ.get('MKM_ACCESS_TOKEN'),
                     resource_owner_secret=os.environ.get('MKM_ACCESS_TOKEN_SECRET'),
                     realm=url)

    assert isinstance(auth, OAuth1)


@missing_app_tokens
def test_widget_app_oauth1_is_correct():
    """Verifies if response from backend is positive using custom Client."""
    url = 'https://sandbox.mkmapi.eu/ws/v1.1/output.json/games'
    auth = MKMOAuth1(os.environ.get('MKM_APP_TOKEN'),
                     client_secret=os.environ.get('MKM_APP_SECRET'),
                     resource_owner_key=os.environ.get('MKM_ACCESS_TOKEN'),
                     resource_owner_secret=os.environ.get('MKM_ACCESS_TOKEN_SECRET'),
                     realm=url,
                     client_class=MKMClient)

    r = requests.get(url, auth=auth)

    assert r.status_code == 200


@missing_app_tokens
@missing_widget_tokens
def test_dedicated_app_oauth1_is_correct():
    """Verifies if response from backend is positive using custom OAuth header."""
    url = 'https://sandbox.mkmapi.eu/ws/v1.1/output.json/games'
    auth = MKMOAuth1(os.environ.get('MKM_APP_TOKEN'),
                     client_secret=os.environ.get('MKM_APP_SECRET'),
                     resource_owner_key=os.environ.get('MKM_ACCESS_TOKEN'),
                     resource_owner_secret=os.environ.get('MKM_ACCESS_TOKEN_SECRET'),
                     realm=url)

    r = requests.get(url, auth=auth)

    assert r.status_code == 200


@missing_app_tokens
@missing_widget_tokens
def test_account_entity_is_as_expected():
    """Verifies the account entity received is as expected."""
    url = 'https://sandbox.mkmapi.eu/ws/v1.1/output.json/account'
    auth = MKMOAuth1(os.environ.get('MKM_APP_TOKEN'),
                     client_secret=os.environ.get('MKM_APP_SECRET'),
                     resource_owner_key=os.environ.get('MKM_ACCESS_TOKEN'),
                     resource_owner_secret=os.environ.get('MKM_ACCESS_TOKEN_SECRET'),
                     realm=url)

    r = requests.get(url, auth=auth)

    json_response = r.json()

    received_first_name = json_response['account']['name']['firstName']
    received_last_name = json_response['account']['name']['lastName']

    assert r.status_code == 200
    assert received_first_name
    assert received_last_name
