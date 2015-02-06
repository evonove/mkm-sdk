import requests
from requests_oauthlib import OAuth1

class OAuthorization:
	def __init__(self):
		self.url = 'https://sandbox.mkmapi.eu/ws/v1.1/accounts'
		self.app_token = 'app_token'
		self.app_secret = 'app_secret'
		self.access_token = 'access_token'
		self.access_token_secret = 'access_token_secret'

	def create_auth(self):
		oauth1 = OAuth1(self.app_token, 
						callback_uri = self.url, 
						resource_owner_key = self.access_token, 
						client_secret = self.app_secret, 
						resource_owner_secret = self.access_token_secret)

		return oauth1

oauth = OAuthorization()