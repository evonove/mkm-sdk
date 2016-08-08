import pytest


@pytest.fixture
def mocked_response(mocker):
    response = mocker.Mock()
    response.content = {}
    return response
