# -*- coding: utf-8 -*-
import pytest

from mkmsdk.mkm import Mkm
from mkmsdk.api_map import _API_MAP
from mkmsdk import exceptions

from . import missing_app_tokens


@pytest.fixture
def mkm_sandbox(scope="module"):
    return Mkm(_API_MAP["1.1"]["api"], _API_MAP["1.1"]["api_sandbox_root"])


@pytest.fixture
def mkm_sandbox20(scope="module"):
    return Mkm(_API_MAP["2.0"]["api"], _API_MAP["2.0"]["api_sandbox_root"])


@missing_app_tokens
def test_response_is_as_expected(mkm_sandbox):
    """Verifies the list of games returned from backend is as expected."""
    response = mkm_sandbox.market_place.games()
    json_response = response.json()

    expected_response = {
        "game": [
            {"idGame": 1, "name": "Magic the Gathering"},
            {"idGame": 3, "name": "Yugioh"},
            {"idGame": 6, "name": "Pokémon"},
            {"idGame": 13, "name": "Dragon Ball Super"},
            {"idGame": 9, "name": "Final Fantasy"},
            {"idGame": 7, "name": "Force of Will"},
            {"idGame": 8, "name": "Cardfight!! Vanguard"},
            {"idGame": 2, "name": "World of Warcraft TCG"},
            {"idGame": 15, "name": "Star Wars: Destiny"},
            {"idGame": 10, "name": "Weiß Schwarz"},
            {"idGame": 11, "name": "Dragoborne"},
            {"idGame": 12, "name": "My Little Pony"},
            {"idGame": 5, "name": "The Spoils"},
        ]
    }

    received_games = json_response["game"]

    assert response.status_code == 200
    assert received_games == expected_response["game"]


@missing_app_tokens
def test_sandbox_url(mkm_sandbox):
    """Verifies that mkm_sandbox sends its requests to sandbox backend."""
    response = mkm_sandbox.market_place.games()

    assert response.status_code == 200
    assert response.request.url == "https://sandbox.cardmarket.com/ws/v1.1/output.json/games"


@missing_app_tokens
def test_card_search(mkm_sandbox):
    """Verifies the search for a product with special chars in its names works correctly."""
    response = mkm_sandbox.market_place.products(name="Jace, the Mind Sculptor", game=1, language=1, match=False)

    assert response.status_code == 200


@pytest.fixture
def create_stock_data(request, mkm_sandbox):
    """Creates some articles in the stock and deletes them on teardown"""
    test_articles = {"article": []}
    for i in range(1, 1001):
        test_articles["article"].append(
            {"idProduct": i, "idLanguage": 1, "comments": "test product", "count": 1, "price": 4, "condition": "EX"}
        )
    r = mkm_sandbox.stock_management.post_stock(data=test_articles)

    def teardown():
        articles_to_delete = {"article": []}
        for a in r.json()["inserted"]:
            articles_to_delete["article"].append(
                {"idArticle": a["idArticle"]["idArticle"], "count": a["idArticle"]["count"]}
            )
        mkm_sandbox.stock_management.delete_stock(data=articles_to_delete)

    request.addfinalizer(teardown)

    return


@missing_app_tokens
def test_stock_requests(create_stock_data, mkm_sandbox):
    """Verifies stock requests are handled correctly and return expected status code"""

    # Gets whole stock
    r = mkm_sandbox.stock_management.get_stock()
    assert r.status_code == 307

    # Gets first stock page
    r = mkm_sandbox.stock_management.get_stock_paginated(start=1)
    assert r.status_code == 206

    # Gets non existing stock page
    # Note: MKM API's Documentations says that specifying a start parameter greater than the number of
    # existing entities their backend returns a 204, No Content, but that seems to be wrong since
    # a 206, Partial Content, is still returned.
    r = mkm_sandbox.stock_management.get_stock_paginated(start=10000)
    assert r.status_code == 206


@missing_app_tokens
def test_request_with_params(mkm_sandbox20):
    """Verifies request to an endpoint that has mandatory parameters"""

    r = mkm_sandbox20.account_management.vacation(params={"onVacation": "false"})
    assert r.status_code == 200

    with pytest.raises(exceptions.ConnectionError) as e:
        mkm_sandbox20.account_management.vacation()
    assert e.value.response.status_code == 400
