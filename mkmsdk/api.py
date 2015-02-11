import os
from requests import request
from mkmsdk.MKMOAuth1 import BuggedOAuth1


class Api:

    def __init__(self):
        self.base_endpoint = 'https://www.mkmapi.eu/ws/v1.1/output.json'

    def request(self, url, method, **kwargs):

        complete_url = '{}{}'.format(self.base_endpoint, url)

        auth = self.create_auth(complete_url)

        response = request(method=method, url=complete_url, auth=auth, **kwargs)
        return response

    def create_auth(self, url):
        auth = BuggedOAuth1(os.environ.get('MKM_APP_TOKEN'),
                            client_secret=os.environ.get('MKM_APP_SECRET'),
                            resource_owner_key=os.environ.get('MKM_ACCESS_TOKEN'),
                            resource_owner_secret=os.environ.get('MKM_ACCESS_TOKEN_SECRET'),
                            realm=url)
        return auth
