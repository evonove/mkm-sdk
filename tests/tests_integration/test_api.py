from . import missing_app_tokens
from mkmsdk.api import Api


@missing_app_tokens
def test_good_request():
    new_api = Api(sandbox_mode=True)
    response = new_api.request('/games', 'get')

    assert response.status_code == 200
