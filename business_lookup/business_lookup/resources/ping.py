from flask_restful import Resource
from business_lookup import __version__


class PingResource(Resource):
    def get(self):
        return {'version': __version__}
