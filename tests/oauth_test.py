import http
import unittest
import requests
from requests_oauthlib import OAuth1
from mkmsdk.MKMOAuth1 import BuggedOAuth1


class OAuthTest(unittest.TestCase):
    def setUp(self):
        self.url = 'https://www.mkmapi.eu/ws/v1.1/output.json/account'
        self.app_token = 'Xv48wJ1XwyaQFOcI'
        self.app_secret = 'fTvgiZYyly6OHYDExKuaFhwTwTsdJslv'
        self.access_token = '81Q5MJKgNe9Lh3m7bGH2li8R8ycaGvtI'
        self.access_token_secret = 'uq4GN4Yn5pAZBrsZ7PZKHFSYguquGUbC'

        self.auth = BuggedOAuth1(self.app_token,
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

        self.assertEqual(r.status_code, http.client.OK)

    def test_account_entity_is_as_expected(self):
        """
        Checks if the account entity received is as expected
        """

        expected_account_response = {'account':
                                         {
                                             'accountBalance': 0,
                                             'onVacation': False,
                                             'idDisplayLanguage': 1,
                                             'articlesInShoppingCart': 0,
                                             'isCommercial': 0,
                                             'name':
                                                 {
                                                     'lastName': 'Cerza',
                                                     'firstName': 'Silvano'
                                                 },
                                             'country': 'IT',
                                             'sellCount': 0,
                                             'shipsFast': 0,
                                             'reputation': 0,
                                             'username': 'Alien1993',
                                             'unreadMessages': 0,
                                             'bankRecharge': 0,
                                             'idUser': 882784,
                                             'address':
                                                 {
                                                     'street': 'Via Padre Camillo Torres 25',
                                                     'zip': '06063',
                                                     'city': 'Magione',
                                                     'name': 'Silvano Cerza',
                                                     'country': 'IT',
                                                     'extra': ''
                                                 },
                                             'paypalRecharge': 0,
                                             'riskGroup': 1
                                         }
                                    }

        r = requests.get(self.url, auth=self.auth)

        json_response = r.json()

        self.assertEqual(json_response, expected_account_response, 'Response received is not as expected')


if __name__ == '__main__':
    unittest.main()
