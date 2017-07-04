class BaseError(StandardError):
    code = 500
    message = 'An error has occurred'

    def get_body(self, environ=None):
        return dict(
            errno=self.code,
            message=self.message)

    def __str__(self):
        return "BaseError: code=%s, message=%s" % (
            self.code, self.message)


class ForbiddenError(BaseError):
    code = 403
    message = 'You do not have access to that resource'


class UnauthorizedError(BaseError):
    code = 401
    message = 'Authentication is required to complete this request.'


class UnprocessableError(BaseError):
    code = 422
    message = 'Invalid data in this request.'


class BadRequestError(BaseError):
    code = 400
    message = 'Invalid object type in this request.'


class NotFoundError(BaseError):
    code = 404
    message = 'Requested resource could not be found.'


class DatabaseError(BaseError):
    code = 500
    message = 'Something went wrong while saving to the database.'
