from mkmsdk.mkm import mkm


def test_simple_call(mocker):
    """Verifies resolver is called when making a call."""
    mock_resolve = mocker.patch('mkmsdk.resolvers.SimpleResolver.resolve')
    mkm.account_management.account()

    mock_resolve.assert_called_once_with(api_map=mkm.api_map['account_management']['account'])
