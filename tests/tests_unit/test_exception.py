from collections import namedtuple

from mkmsdk.exceptions import ConnectionError, Redirection, ResourceNotFound, UnauthorizedAccess, MissingParam


def test_connection():
    error = ConnectionError({})

    assert str(error) == 'Request failed.'


def test_redirect():
    error = Redirection({'Location': 'https://example.com'})

    assert str(error) == 'Request failed. => https://example.com'


def test_not_found():
    Response = namedtuple('Response', 'status_code reason')
    response = Response(status_code='404', reason='Not found')
    error = ResourceNotFound(response)

    assert str(error) == 'Request failed. Status code: 404. Response message: Not found.'


def test_unauthorized_access():
    Response = namedtuple('Response', 'status_code reason')
    response = Response(status_code='401', reason='Unauthorized')
    error = UnauthorizedAccess(response)

    assert str(error) == 'Request failed. Status code: 401. Response message: Unauthorized.'


def test_missing_param():
    error = MissingParam('Missing Payment Id')

    assert str(error) == 'Missing Payment Id'


def test_missing_config():
    error = MissingParam('Missing client_id')

    assert str(error) == 'Missing client_id'
