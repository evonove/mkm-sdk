from xml.sax.saxutils import XMLGenerator
from six import StringIO

from .exceptions import SerializationException


class XMLSerializer:
    """Serializes data to XML"""
    def __init__(self):
        self.generator = None

    def serialize(self, data):
        """
        Serializes data to XML so that it can be
        sent to backend, if data is not a dictionary
        raises a SerializationException

        Params:
            `data`: A dictionary containing the data to serialize

        Return:
            `xml`: Returns a string containing data serialized to XML
        """

        if not isinstance(data, dict):
            raise SerializationException("Can't serialize data, must be a dictionary.")

        stream = StringIO()
        self.generator = XMLGenerator(stream, 'utf-8')

        self.generator.startDocument()
        self.generator.startElement('request', {})

        self._parse(data)

        self.generator.endElement('request')
        self.generator.endDocument()

        return stream.getvalue()

    def _parse(self, data, previous_element_tag=None):
        """
        Parses data and creates the relative elements

        Params:
            `data`: Data to parse
            `previous_element_tag`: When parsing a list we pass the previous element tag
        """
        if isinstance(data, dict):
            for key in data:
                value = data[key]
                self._parse(value, key)

        elif isinstance(data, (list, tuple)):
            for item in data:
                self.generator.startElement(previous_element_tag, {})
                self._parse(item, previous_element_tag)
                self.generator.endElement(previous_element_tag)

        else:
            self.generator.startElement(previous_element_tag, {})
            self.generator.characters('%s' % data)
            self.generator.endElement(previous_element_tag)
