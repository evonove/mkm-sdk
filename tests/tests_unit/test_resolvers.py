import pytest

from mkmsdk import exceptions
from mkmsdk.resolvers import SimpleResolver


def test_if_bad_api_map_is_handled_correctly():
    """Verifies setup throws an exception if api map used is empty."""

    live_resolver = SimpleResolver(sandbox_mode=False)
    empty_api_map = {}

    with pytest.raises(Exception):
        live_resolver.setup()

    with pytest.raises(Exception):
        live_resolver.setup(empty_api_map)


def test_if_setup_works_correctly():
    """Verifies setup correctly formats the url."""

    live_resolver = SimpleResolver(sandbox_mode=False)
    simple_api_map = {'url': '/account', 'method': 'get'}
    expected_url = '/account'
    expected_url_with_parameters = '/user/SimpleUser'
    expected_method = 'get'
    simple_api_map_with_parameters = {'url': '/user/{user}', 'method': 'get'}

    live_resolver.setup(simple_api_map)

    assert live_resolver.url == expected_url
    assert live_resolver.method == expected_method

    live_resolver.setup(simple_api_map_with_parameters, user='SimpleUser')

    assert live_resolver.url == expected_url_with_parameters
    assert live_resolver.method == expected_method


def test_if_bad_parameters_are_handled_correctly():
    """Verifies exception is thrown when user passes an unexisting parameter."""
    live_resolver = SimpleResolver(sandbox_mode=False)
    simple_api_map_with_parameters = {'url': '/user/{user}', 'method': 'get'}

    with pytest.raises(exceptions.MissingParam):
        live_resolver.setup(simple_api_map_with_parameters)

    with pytest.raises(exceptions.MissingParam):
        live_resolver.setup(simple_api_map_with_parameters, bad_param='Worst parameter ever')


def test_setup_escapes_additional_parameters():
    """Verifies setup escapes parameters containing spaces or special chars."""
    live_resolver = SimpleResolver(sandbox_mode=False)
    simple_api_map = {'url': '/products/{name}/{game}/{language}/{match}', 'method': 'get'}
    expected_url = '/products/Jace%2C%20the%20Mind%20Sculptor/1/1/False'

    live_resolver.setup(simple_api_map, name='Jace, the Mind Sculptor', game=1, language=1, match=False)

    assert live_resolver.url == expected_url
