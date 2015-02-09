import http
import unittest
import requests
from requests_oauthlib import OAuth1
from mkmsdk.MKMOAuth1 import BuggedOAuth1


class OAuthTest(unittest.TestCase):
    def setUp(self):
        self.url = 'https://www.mkmapi.eu/ws/v1.1/account'
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
        Check if response from server is not negative
        """

        r = requests.get(self.url, auth=self.auth)

        self.assertEqual(r.status_code, http.client.OK)


if __name__ == '__main__':
    unittest.main()
