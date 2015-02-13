from . import IntegrationTest

from mkmsdk.mkm import mkm, mkm_sandbox


class MkmTest(IntegrationTest):
    def setUp(self):
        self.expected_response = {
            'game': [
                {'idGame': 1, 'name': 'Magic the Gathering'},
                {'idGame': 3, 'name': 'Yugioh'},
                {'idGame': 2, 'name': 'World of Warcraft TCG'},
                {'idGame': 5, 'name': 'The Spoils'}
            ]
        }

    def test_response_is_as_expected(self):
        response = mkm.market_place.games()
        json_response = response.json()

        first_game_received = json_response['game']

        self.assertEqual(first_game_received, self.expected_response['game'], 'Game received is not correct')

    def test_sandbox_url(self):
        response = mkm_sandbox.account_management.account()
        self.assertEqual(response.request.url, 'https://sandbox.mkmapi.eu/ws/v1.1/output.json')