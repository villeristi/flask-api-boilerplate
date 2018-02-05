from os import getenv
from werkzeug.exceptions import HTTPException, Unauthorized, default_exceptions, BadRequest

from util.helpers import respond_with


class Configure(object):
    def __init__(self, app, auth):
        self.app = app
        self.auth = auth

        if self.app is not None:
            self.register_handlers()

        if self.auth is not None:
            self.auth.verify_token_callback = self._verify_token
            self.auth.auth_error_callback = self._auth_error

    def register_handlers(self):
        """
        Hook error-handler to exceptions
        :return:
        """
        for exception in default_exceptions:
            self.app.register_error_handler(exception, self._handle_exception)

    def _handle_exception(self, exception):
        """
        Global error handler
        :param exception: Exception
        :return:
        """
        http_code = 500
        if isinstance(exception, HTTPException):
            http_code = exception.code

        return respond_with({
            'code': http_code,
            'error': exception.description
        }, http_code)

    def _auth_error(self):
        """
        Raise auth-exception
        :return:
        """
        return self._handle_exception(Unauthorized())

    def _verify_token(self, token):
        """
        Check if Authorization header Token is valid
        :param token:
        :return: boolean
        """
        env_token = getenv('TOKEN', False)

        # If there's no TOKEN defined => Don't require Authorization-header
        if not env_token:
            return True

        if token == env_token:
            return True
        return False
