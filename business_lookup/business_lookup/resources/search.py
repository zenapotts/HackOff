from copy import deepcopy
import flask
from flask_restful import Resource
from business_lookup.database import search_database
from business_lookup.config import read_config

settings = read_config()


class SearchResource(Resource):

    def get(self, city, country, profession):
        result = search_database(city, country, profession)
        return result
