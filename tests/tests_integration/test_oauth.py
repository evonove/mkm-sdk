import unittest
import os

import requests
from requests_oauthlib import OAuth1

from mkmsdk.MKMOAuth1 import MKMOAuth1
from mkmsdk.MKMClient import MKMClient
from . import IntegrationTest, skip_account_integration, skip_dedicated_app_integration


class OAuthTest(IntegrationTest):

    def test_oauth_is_received(self):
        """
        Checks if OAuth1 is received
        """
        url = 'https://sandbox.mkmapi.eu/ws/v1.1/output.json/games'
        auth = MKMOAuth1(os.environ.get('MKM_APP_TOKEN'),
                         client_secret=os.environ.get('MKM_APP_SECRET'),
                         resource_owner_key=os.environ.get('MKM_ACCESS_TOKEN'),
                         resource_owner_secret=os.environ.get('MKM_ACCESS_TOKEN_SECRET'),
                         realm=url)

        self.assertTrue(isinstance(auth, OAuth1))

    @unittest.skipIf(not skip_dedicated_app_integration(), 'Access Token and Access Token Secret are not empty')
    def test_widget_app_oauth1_is_correct(self):
        """
        Checks if response from server is positive
        """
        url = 'https://sandbox.mkmapi.eu/ws/v1.1/output.json/games'
        auth = MKMOAuth1(os.environ.get('MKM_APP_TOKEN'),
                         client_secret=os.environ.get('MKM_APP_SECRET'),
                         resource_owner_key=os.environ.get('MKM_ACCESS_TOKEN'),
                         resource_owner_secret=os.environ.get('MKM_ACCESS_TOKEN_SECRET'),
                         realm=url,
                         client_class=MKMClient)

        r = requests.get(url, auth=auth)

        self.assertEqual(r.status_code, 200)

    @unittest.skipIf(skip_dedicated_app_integration(), 'Access Token and Access Token Secret are empty')
    def test_dedicated_app_oauth1_is_correct(self):
        """
        Checks if response from server is positive
        """
        url = 'https://sandbox.mkmapi.eu/ws/v1.1/output.json/games'
        auth = MKMOAuth1(os.environ.get('MKM_APP_TOKEN'),
                         client_secret=os.environ.get('MKM_APP_SECRET'),
                         resource_owner_key=os.environ.get('MKM_ACCESS_TOKEN'),
                         resource_owner_secret=os.environ.get('MKM_ACCESS_TOKEN_SECRET'),
                         realm=url)

        r = requests.get(url, auth=auth)

        self.assertEqual(r.status_code, 200)

    @unittest.skipIf(skip_account_integration(), 'Missing env vars')
    @unittest.skipIf(skip_dedicated_app_integration(), 'Access Token and Access Token Secret are empty')
    def test_account_entity_is_as_expected(self):
        """
        Checks if the account entity received is as expected
        """
        url = 'https://sandbox.mkmapi.eu/ws/v1.1/output.json/account'
        auth = MKMOAuth1(os.environ.get('MKM_APP_TOKEN'),
                         client_secret=os.environ.get('MKM_APP_SECRET'),
                         resource_owner_key=os.environ.get('MKM_ACCESS_TOKEN'),
                         resource_owner_secret=os.environ.get('MKM_ACCESS_TOKEN_SECRET'),
                         realm=url)

        last_name = os.environ['MKM_ACCOUNT_LAST_NAME']
        first_name = os.environ['MKM_ACCOUNT_FIRST_NAME']

        expected_account_response = \
            {
                'account':
                    {
                        'name':
                            {
                                'lastName': last_name,
                                'firstName': first_name
                            }
                    }
            }

        r = requests.get(url, auth=auth)

        json_response = r.json()

        received_first_name = json_response['account']['name']['firstName']
        received_last_name = json_response['account']['name']['lastName']

        expected_first_name = expected_account_response['account']['name']['firstName']
        expected_last_name = expected_account_response['account']['name']['lastName']

        self.assertEqual(received_first_name, expected_first_name, 'First name received is not as expected')

        self.assertEqual(received_last_name, expected_last_name, 'Last name received is not as expected')
