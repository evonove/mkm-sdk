from . import missing_app_tokens
from mkmsdk.resolvers import SimpleResolver


@missing_app_tokens
def test_resolve_with_data():
    """Verifies posting data to backend returns a positive response."""
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
