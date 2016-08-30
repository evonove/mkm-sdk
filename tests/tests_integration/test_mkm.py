# -*- coding: utf-8 -*-
from . import missing_app_tokens
from mkmsdk.mkm import mkm_sandbox


@missing_app_tokens
def test_response_is_as_expected():
    """Verifies the list of games returned from backend is as expected."""
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

    received_games = json_response['game']

    assert response.status_code == 200
    assert received_games == expected_response['game']


@missing_app_tokens
def test_sandbox_url():
    """Verifies that mkm_sandbox sends its requests to sandbox backend."""
    response = mkm_sandbox.market_place.games()

    assert response.status_code == 200
    assert response.request.url == 'https://sandbox.mkmapi.eu/ws/v1.1/output.json/games'


@missing_app_tokens
def test_card_search():
    """Verifies the search for a product with special chars in its names works correctly."""
    response = mkm_sandbox.market_place.products(name='Jace, the Mind Sculptor', game=1, language=1, match=False)

    assert response.status_code == 200
