from business_lookup.app import make_app
from business_lookup.database import db


class ComponentTest(object):

    def setUp(self):
        self.app = make_app(config_file='./test.ini')
        self.app.config['TESTING'] = True

        self._ctx = self.app.test_request_context()
        self._ctx.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        if hasattr(self, '_ctx'):
            self._ctx.pop()
            del self._ctx
        if hasattr(self, 'app'):
            del self.app

    def get(self, *args, **kwargs):
        with self.app.test_client() as c:
            res = c.get(*args, **kwargs)
        return res

    def post(self, *args, **kwargs):
        with self.app.test_client() as c:
            res = c.post(*args, **kwargs)
        return res
