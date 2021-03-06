import statsdecor
import newrelic.agent
from business_lookup.api import Api
from business_lookup.config import read_config
from flask import Flask
from FreshUtils.logger import set_version
from business_lookup.database import commit_request_transaction
from business_lookup.database import db
from flask.ext.cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route("/")
@cross_origin()
def helloWorld():
  return "Hello, cross-origin-world!"
  
def make_api():
    from business_lookup.resources.ping import PingResource
    from business_lookup.resources.health import HealthResource
    from business_lookup.resources.search import SearchResource

    api = Api(catch_all_404s=True)

    # Monitoring
    api.add_resource(PingResource, '/ping')
    api.add_resource(HealthResource, '/health')
    api.add_resource(SearchResource, '/<city>/<country>/<profession>')

    return api


def make_app(config_file='./development.ini'):
    set_version('business_lookup')

    app = Flask("business_lookup")
    app.config.update(read_config(config_file=config_file))
    app.config.update(app.config['flask'])

    statsdecor.configure(app.config['statsd_client'])

    api = make_api()
    api.init_app(app)
    app.after_request(commit_request_transaction)
    db.init_app(app)

    # Top level wrapping should be newrelic
    # so we catch exceptions/errors there
    app = newrelic.agent.WSGIApplicationWrapper(app)
    return app
