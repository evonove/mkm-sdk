def test_request_works(mocker):
    url = '/metaproducts/island/1/1'
    method = 'get'

    mock_request = mocker.patch('mkmsdk.api.Api.request')

    mock_request(url, method)
    mock_request.assert_called_once_with(url, method)
