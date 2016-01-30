import unittest
import os

import mkmsdk


def skip_integration():
    try:
        mkmsdk.get_mkm_app_token()
        mkmsdk.get_mkm_app_secret()
        mkmsdk.get_mkm_access_token()
        mkmsdk.get_mkm_access_token_secret()
        return False
    except mkmsdk.exceptions.MissingConfig:
        return True

def skip_account_integration():
    try:
        os.environ['MKM_ACCOUNT_LAST_NAME']
        os.environ['MKM_ACCOUNT_FIRST_NAME']
        return False
    except KeyError:
        return True

def skip_dedicated_app_integration():
    try:
        os.environ['MKM_ACCESS_TOKEN'] == ''
        os.environ['MKM_ACCESS_TOKEN_SECRET'] == ''
        return False
    except KeyError:
        return True

@unittest.skipIf(skip_integration(), 'Missing env vars, skipping integration test')
class IntegrationTest(unittest.TestCase):
    pass
