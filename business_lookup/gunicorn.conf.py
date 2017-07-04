from business_lookup.app import make_app


_config = make_app().config


bind = '%s:%s' % (_config['gunicorn']['host'], _config['gunicorn']['port'])
pidfile = _config['gunicorn']['pidfile']
user = _config['gunicorn']['user']
group = _config['gunicorn']['group']
logconfig = _config['gunicorn']['logconfig']
workers = _config['gunicorn']['workers']
worker_class = _config['gunicorn']['worker_class']
