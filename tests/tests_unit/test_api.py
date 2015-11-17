import unittest
from ..compat import mock

from mkmsdk.api import Api
from mkmsdk import exceptions
from mkmsdk import get_mkm_app_secret


class ApiTest(unittest.TestCase):

    def setUp(self):
        self.api = Api()
        self.response = mock.Mock()
        self.response.content = {}

    def test_missing_env_var_raise_exception_correctly(self):
        with mock.patch('mkmsdk.os') as os_mocked:
            os_mocked.environ = {}
            self.assertRaises(exceptions.MissingConfig, get_mkm_app_secret)

    def test_endpoint(self):
        expected_live_base_endpoint = 'https://www.mkmapi.eu/ws/v1.1/output.json'

        self.assertEqual(self.api.base_endpoint, expected_live_base_endpoint)

    def test_sandbox_mode(self):
        sandbox_api = Api(sandbox_mode=True)
        expected_sandbox_base_endpoint = 'https://sandbox.mkmapi.eu/ws/v1.1/output.json'
        
        self.assertEqual(sandbox_api.base_endpoint, expected_sandbox_base_endpoint)

    def test_redirection(self):
        self.response.status_code = 301
        self.assertRaises(exceptions.Redirection,
                          self.api.handle_response, self.response, self.response.content)

        self.response.status_code = 302
        self.assertRaises(exceptions.Redirection,
                          self.api.handle_response, self.response, self.response.content)

        self.response.status_code = 303
        self.assertRaises(exceptions.Redirection,
                          self.api.handle_response, self.response, self.response.content)

        self.response.status_code = 307
        self.assertRaises(exceptions.Redirection,
                          self.api.handle_response, self.response, self.response.content)

    def test_bad_request(self):
        self.response.status_code = 400
        self.assertRaises(exceptions.BadRequest,
                          self.api.handle_response, self.response, self.response.content)

    def test_unauthorized_access(self):
        self.response.status_code = 401
        self.assertRaises(exceptions.UnauthorizedAccess,
                          self.api.handle_response, self.response, self.response.content)

    def test_forbidden_access(self):
        self.response.status_code = 403
        self.assertRaises(exceptions.ForbiddenAccess,
                          self.api.handle_response, self.response, self.response.content)

    def test_resource_not_found(self):
        self.response.status_code = 404
        self.assertRaises(exceptions.ResourceNotFound,
                          self.api.handle_response, self.response, self.response.content)

    def test_method_not_allowed(self):
        self.response.status_code = 405
        self.assertRaises(exceptions.MethodNotAllowed,
                          self.api.handle_response, self.response, self.response.content)

    def test_resource_conflict(self):
        self.response.status_code = 409
        self.assertRaises(exceptions.ResourceConflict,
                          self.api.handle_response, self.response, self.response.content)

    def test_resource_gone(self):
        self.response.status_code = 410
        self.assertRaises(exceptions.ResourceGone,
                          self.api.handle_response, self.response, self.response.content)

    def test_resource_invalid(self):
        self.response.status_code = 422
        self.assertRaises(exceptions.ResourceInvalid,
                          self.api.handle_response, self.response, self.response.content)

    def test_client_error(self):
        self.response.status_code = 480
        self.assertRaises(exceptions.ClientError,
                          self.api.handle_response, self.response, self.response.content)

    def test_server_error(self):
        self.response.status_code = 545
        self.assertRaises(exceptions.ServerError,
                          self.api.handle_response, self.response, self.response.content)

    def test_unknown_error(self):
        self.response.status_code = 1001
        self.assertRaises(exceptions.ConnectionError,
                          self.api.handle_response, self.response, self.response.content)
