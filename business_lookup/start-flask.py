from business_lookup.app import make_app
import logging

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# For development use only.
app = make_app()
app.debug = True
config = app.config['gunicorn']
app.run(host=config['host'], port=int(config['port']))
