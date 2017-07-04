import sys
import json
import logging
import newrelic.agent
import statsdecor
import statsdecor.decorators
from flask_restful
from flask import make_response
from .error import BaseError, NotFoundError
from werkzeug.exceptions import HTTPException
from business_lookup import __version__, PREFIX


log = logging.getLogger(__name__)
JSON_API_MEDIA_TYPE = 'application/vnd.api+json'


@statsdecor.decorators.timed('business_lookup.response.to_json.duration')
def output_json(data, code, headers=None):
    headers = headers or {}
    headers['X-Version'] = __version__

    if not isinstance(data, basestring):
        data = json.dumps(data)
    resp = make_response(data, code)
    resp.headers.extend(headers)
    return resp


class Api(flask_restful.Api):
    def __init__(self, *args, **kwargs):
        super(Api, self).__init__(*args, **kwargs)
        self.default_mediatype = JSON_API_MEDIA_TYPE
        self.prefix = PREFIX
        self.representations = {
            JSON_API_MEDIA_TYPE: output_json,
        }

    def handle_error(self, error):
        if (isinstance(error, HTTPException)
                and not isinstance(error, BaseError)):
            response = {
                'message': str(error),
                'errno': error.code
            }
            return self.create_response(response, error)
        if not isinstance(error, BaseError):
            if getattr(error, 'code', None) == 404:
                error = NotFoundError()
            else:
                error = BaseError()
        return self.create_response(error.get_body(), error)

    def create_response(self, body, error):
        resp = self.make_response(body, error.code)
        if resp.status_code == 401:
            resp.headers['WWW-Authenticate'] = 'Bearer realm="freshbooks"'
        if resp.status_code >= 500:
            log.exception(error)
        return resp
