class ConnectionError(Exception):
    """
    Wraps errors related with
    requests to backend
    """

    def __init__(self, response=None, message=None):
        """
        Initializes the exception with the response
        received from the backend

        Params:
            `response`: The response received from backend
            `message`: A custom message

        Return:
            `response`: Returns the response received from the server
        """
        self.response = response
        self.message = message

    def __str__(self):
        """
        Formats the error for the user so that it's
        easier to understand
        """
        message = 'Request failed'
        if hasattr(self.response, 'status_code'):
            message = '{}{}'.format(message, '\nStatus code: %s' % self.response.status_code)
        if hasattr(self.response, 'reason'):
            message = '{}{}'.format(message, '\nResponse message: %s' % self.response.reason)
        if hasattr(self.response, 'content'):
            message = '{}{}'.format(message, '\n%s' % self.response.content)
        if self.message:
            message = '{}{}'.format(message, '\n%s' % self.message)
        return message


class MissingParam(Exception):
    """
    Wraps errors caught when setting up
    the url with its parameters
    """

    def __init__(self, param):
        """
        Initializes the exception with the
        missing parameter name

        `param`: The missing parameter
        """
        self.param = param

    def __str__(self):
        return 'Missing %s parameter' % self.param


class MissingEnvVar(Exception):
    """
    Wraps errors for missing
    environment variables
    """
    def __init__(self, env):
        """
        Initializes the exception with the
        missing variable name

        `env`: The missing environment variable
        """
        self.env = env

    def __str__(self):
        return 'Missing %s environment variable' % self.env


class SerializationException(Exception):
    """Wraps exceptions raised during XML serialization"""
    def __str__(self):
        return 'Serialization exception. %s' % self.args
