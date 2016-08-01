from . import IntegrationTest

from mkmsdk.resolvers import SimpleResolver


class ResolversTest(IntegrationTest):
    def setUp(self):
        self.resolver = SimpleResolver(sandbox_mode=True)

    def test_resolve_with_data(self):
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

        response = self.resolver.resolve(api_map=simple_api_map, data=data)

        self.assertEqual(response.status_code, 200)
