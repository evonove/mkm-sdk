import unittest
import requests
from requests_oauthlib import OAuth1
from unittest import mock
from mkmsdk.authorization import oauth

class OAuthTest(unittest.TestCase):

	def setUp(self):
		self.auth = oauth

	def test_server_response_is_correct(self):
		"""
		Test response from server
		"""

		"""
		First check if OAuth1 is received
		"""

		self.assertTrue(isinstance(self.auth.create_auth(), OAuth1))
		"""
		Check if OAuth1 is correct
		"""

		"""
		Check if response from server is not negative
		"""
		
if __name__ == '__main__':
	unittest.main()