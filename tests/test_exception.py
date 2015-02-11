from collections import namedtuple
import unittest
from mkmsdk.exceptions import ConnectionError


class TestExceptions(unittest.TestCase):

    def setUp(self):
        self.Response = namedtuple('Response', 'status_code reason')

    def test_connection(self):
        error = ConnectionError({})
        self.assertEqual(str(error), 'Request failed')