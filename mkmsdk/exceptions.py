class ConnectionError(Exception):
    def __init__(self, response, content=None, message=None):
        self.response = response
        self.content = content
        self.message = message

    def __str__(self):
        message = 'Request failed.'
        if hasattr(self.response, 'status_code'):
            message = '{}{}'.format(message, ' Status code: %s.' % self.response.status_code)
        if hasattr(self.response, 'reason'):
            message = '{}{}'.format(message, ' Response message: %s.' % self.response.reason)
        if self.content:
            message = '{}{}'.format(message, ' Error message: %s' % str(self.content))
        return message

class Redirection(ConnectionError):
    """
    3xx
    """
    def __str__(self):
        message = super(Redirection, self).__str__()
        if self.response.get('Location'):
            message = "{} => {}" .format(message, self.response.get('Location'))
        return message

class MissingParam(TypeError):
    pass

class MissingConfig(Exception):
    pass

class ClientError(ConnectionError):
    """
    4xx Client Error
    """
    pass

class BadRequest(ClientError):
    """
    400 Bad Request
    """
    pass

class UnauthorizedAccess(ClientError):
    """
    401 Unauthorized
    """
    pass

class ForbiddenAccess(ClientError):
    """
    403 Forbidden
    """

class ResourceNotFound(ClientError):
    """
    404 Not Found
    """
    pass

class ResourceConflict(ClientError):
    """
    409 Conflict
    """
    pass

class ResourceGone(ClientError):
    """
    410 Gone
    """
    pass

class ResourceInvalid(ClientError):
    """
    422 Invalid
    """
    pass

class ServerError(ConnectionError):
    """
    5xx Server Error
    """
    pass

class MethodNotAllowed(ClientError):
    """
    405 Method Not Allowed
    """

    def allowed_methods(self):
        return self.response['Allow']
