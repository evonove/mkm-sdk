import pytest

from mkmsdk.mkm import Mkm
from mkmsdk.api_map import _API_MAP


@pytest.fixture
def mkm():
    return Mkm(_API_MAP["1.1"]["api"], _API_MAP["1.1"]["api_sandbox_root"])


def test_simple_call(mocker, mkm):
    """Verifies resolver is called when making a call."""
    mock_resolve = mocker.patch("mkmsdk.resolvers.SimpleResolver.resolve")
    mkm.account_management.account()

    mock_resolve.assert_called_once_with(api_map=mkm.api_map["account_management"]["account"])
