import unittest
import os

import requests
from requests_oauthlib import OAuth1

from mkmsdk.MKMOAuth1 import MKMOAuth1
from . import IntegrationTest, skip_account_integration


class OAuthTest(IntegrationTest):
    def setUp(self):
        self.url = 'https://sandbox.mkmapi.eu/ws/v1.1/output.json/account'
        self.app_token = os.environ.get('MKM_APP_TOKEN')
        self.app_secret = os.environ.get('MKM_APP_SECRET')
        self.access_token = os.environ.get('MKM_ACCESS_TOKEN')
        self.access_token_secret = os.environ.get('MKM_ACCESS_TOKEN_SECRET')

        self.auth = MKMOAuth1(self.app_token,
                                 client_secret=self.app_secret,
                                 resource_owner_key=self.access_token,
                                 resource_owner_secret=self.access_token_secret,
                                 realm=self.url)

    def test_oauth_is_received(self):
        """
        Checks if OAuth1 is received
        """
        self.assertTrue(isinstance(self.auth, OAuth1))

    def test_oauth1_is_correct(self):
        """
        Checks if response from server is not negative
        """
        r = requests.get(self.url, auth=self.auth)

        self.assertEqual(r.status_code, 200)

    @unittest.skipIf(skip_account_integration(), "Missing env vars, skipping account integration test")
    def test_account_entity_is_as_expected(self):
        """
        Checks if the account entity received is as expected
        """
        last_name = os.environ['MKM_ACCOUNT_LAST_NAME']
        first_name =  os.environ['MKM_ACCOUNT_FIRST_NAME']

        expected_account_response = {'account':
                                         {
                                             'name':
                                                 {
                                                     'lastName': last_name,
                                                     'firstName': first_name
                                                 }
                                         }
                                    }

        r = requests.get(self.url, auth=self.auth)

        json_response = r.json()

        received_first_name = json_response['account']['name']['firstName']
        received_last_name = json_response['account']['name']['lastName']

        expected_first_name = expected_account_response['account']['name']['firstName']
        expected_last_name = expected_account_response['account']['name']['lastName']

        self.assertEqual(received_first_name, expected_first_name, 'First name received is not as expected')

        self.assertEqual(received_last_name, expected_last_name, 'Last name received is not as expected')
