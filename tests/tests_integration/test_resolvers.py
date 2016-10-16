from . import missing_app_tokens
from mkmsdk.resolvers import SimpleResolver


@missing_app_tokens
def test_resolve_with_xml_data():
    """Verifies posting xml data to backend returns a positive response."""
    resolver = SimpleResolver(sandbox_mode=True)

    simple_api_map = {'url': '/stock',
                      'method': 'post'}

    # Data posted to MKM, we post an XML because the API
    # doesn't accept anything else
    data = """<?xml version="1.0" encoding="UTF-8" ?>
                <request>
                    <article>
                        <idProduct>100569</idProduct>
                        <idLanguage>1</idLanguage>
                        <comments>Inserted through the API</comments>
                        <count>1</count>
                        <price>4</price>
                        <condition>EX</condition>
                        <isFoil>true</isFoil>
                        <isSigned>false</isSigned>
                        <isPlayset>false</isPlayset>
                    </article>
                </request>"""

    response = resolver.resolve(api_map=simple_api_map, data=data)

    assert response.status_code == 200


@missing_app_tokens
def test_resolve_with_data():
    """
    Verifies calling resolve with some data serializes it
    correctly if necessary before sending it to the backend
    so that it returns a positive response
    """
    resolver = SimpleResolver(sandbox_mode=True)

    simple_api_map = {'url': '/stock',
                      'method': 'post'}

    # Data posted to MKM, this will be serialized to XML
    # before being sent, otherwise the backend won't accept it
    data = {'article': [
                {
                 'idProduct': 100569,
                 'idLanguage': 1,
                 'comments': 'Inserted through the API',
                 'count': 1,
                 'price': 4,
                 'condition': 'EX',
                 'isFoil': True,
                 'isSigned': False,
                 'isPlayset': False
                }
              ]
            }

    response = resolver.resolve(api_map=simple_api_map, data=data)

    assert response.status_code == 200
