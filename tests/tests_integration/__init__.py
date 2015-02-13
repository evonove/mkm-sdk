import unittest


def skip_integration():
    return True


@unittest.skipIf(skip_integration(), "Missing env vars, skipping integration test")
class IntegrationTest(unittest.TestCase):
    pass
