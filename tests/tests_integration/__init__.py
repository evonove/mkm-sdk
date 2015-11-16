import unittest

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

@unittest.skipIf(skip_integration(), "Missing env vars, skipping integration test")
class IntegrationTest(unittest.TestCase):
    pass
