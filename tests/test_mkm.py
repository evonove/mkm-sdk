import unittest
from unittest import mock
from mkmsdk.mkm import mkm, mkm_sandbox


class MkmTest(unittest.TestCase):

    def setUp(self):
        self.expected_response = {
            'game': [
                {'idGame': 1, 'name': 'Magic the Gathering'},
                {'idGame': 3, 'name': 'Yugioh'},
                {'idGame': 2, 'name': 'World of Warcraft TCG'},
                {'idGame': 5, 'name': 'The Spoils'}
            ]
        }

    def test_simple_call(self):
        with mock.patch('mkmsdk.resolvers.SimpleResolver.resolve') as mock_resolve:
            mkm.account_management.account()

            mock_resolve.assert_called_once_with(api_map=mkm.api_map['account_management']['account'])

    def test_response_is_as_expected(self):
        response = mkm.market_place.games()
        json_response = response.json()

        first_game_received = json_response['game']

        self.assertEqual(first_game_received, self.expected_response['game'], 'Game received is not correct')

    def test_sandbox_url(self):
        response = mkm_sandbox.account_management.account()
        self.assertEqual(response.request.url, 'https://sandbox.mkmapi.eu/ws/v1.1/output.json')
