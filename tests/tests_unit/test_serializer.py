import pytest

from mkmsdk.serializer import XMLSerializer
from mkmsdk.exceptions import SerializationException


def test_xml_serializer():
    """Verifies that data is correctly serialized to XML"""
    data = {'action': 'add', 'article': [{'idArticle': 666, 'amount': 2}, {'idArticle': 101, 'amount': 5}]}

    serializer = XMLSerializer()
    serialized_data = serializer.serialize(data=data)

    assert '<?xml version="1.0" encoding="utf-8"?>\n<request>' in serialized_data
    assert '<amount>2</amount>' in serialized_data
    assert '<idArticle>666</idArticle>' in serialized_data
    assert '<amount>5</amount>' in serialized_data
    assert '<idArticle>101</idArticle>' in serialized_data
    assert '<action>add</action>' in serialized_data
    assert '</request>' in serialized_data


def test_exception_raised_if_bad_data():
    """Verifies SerializationException is raised when trying to serialize bad data"""

    data = "We can't serialize this"

    serializer = XMLSerializer()

    with pytest.raises(SerializationException):
        serializer.serialize(data=data)
