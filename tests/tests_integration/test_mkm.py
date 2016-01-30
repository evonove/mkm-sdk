# -*- coding: utf-8 -*-
from mkmsdk.mkm import mkm_sandbox
from . import IntegrationTest


class MkmTest(IntegrationTest):

    def test_response_is_as_expected(self):
        response = mkm_sandbox.market_place.games()
        json_response = response.json()

        expected_response = {
            'game': [
                {'idGame': 1, 'name': 'Magic the Gathering'},
                {'idGame': 3, 'name': 'Yugioh'},
                {'idGame': 6, 'name': u'Pokémon'},
                {'idGame': 2, 'name': 'World of Warcraft TCG'},
                {'idGame': 5, 'name': 'The Spoils'}
            ]
        }

        first_game_received = json_response['game']

        self.assertEqual(first_game_received, expected_response['game'], 'Game received is not correct')

    def test_sandbox_url(self):
        response = mkm_sandbox.market_place.games()
        self.assertEqual(response.request.url, 'https://sandbox.mkmapi.eu/ws/v1.1/output.json/games')