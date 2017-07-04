import os
import json


def get_fixture(filename):
    path = os.path.dirname(os.path.dirname(__file__))

    with open(path + '/fixtures/{}.json'.format(filename)) as json_file:
        data = json.load(json_file)

    return data
