from flask_restful import Resource


class HealthResource(Resource):
    def get(self):
        """
        Should return healthcheck information. This can include, but is not
        limited to:

        * Can the app reach its dependencies (MySQl, RabbitMQ, 3rd parties)
        * Have any circuit breakers for dependencies failed recently?

        You should return a 200 if things are ok, and 503 if things are
        not good.
        """
        return {'condition': 'not-implemented'}, 200
        # In the case where health is poor,
        # return {'condition': 'poor'}, 503
