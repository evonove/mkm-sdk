from collections import namedtuple

from mkmsdk.exceptions import ConnectionError, MissingParam, MissingEnvVar, SerializationException


def test_connection_error_with_no_args():
    """
    Test error string is formatted correctly
    when exception is initialized without arguments
    """
    error = ConnectionError()

    assert str(error) == 'Request failed'


def test_connection_error_with_response():
    """
    Test error string is formatted correctly
    when exception is initialized with response
    """
    Response = namedtuple('Response', 'status_code reason content')
    response = Response(status_code='404', reason='Not found', content='Here some content')
    error = ConnectionError(response)

    assert str(error) == 'Request failed\nStatus code: 404\nResponse message: Not found\nHere some content'


def test_connection_error_with_empty_response():
    """
    Test error string is formatted correctly
    when exception is initialized with empty response
    """
    error = ConnectionError({})

    assert str(error) == 'Request failed'


def test_connection_error_with_message():
    """
    Test error string is formatted correctly
    when exception is initialized with a message
    """
    error = ConnectionError(message='This is a message')

    assert str(error) == 'Request failed\nThis is a message'


def test_missing_param():
    """Test error string is formatted correctly"""
    error = MissingParam('payment_id')

    assert str(error) == 'Missing payment_id parameter'


def test_missing_config():
    """Test error string is formatted correctly"""
    error = MissingEnvVar('client_id')

    assert str(error) == 'Missing client_id environment variable'


def test_serialization_exception():
    """Test error string is formatted correctly"""
    error = SerializationException('Something wrong with serialization')

    assert str(error) == 'Serialization exception. Something wrong with serialization'
