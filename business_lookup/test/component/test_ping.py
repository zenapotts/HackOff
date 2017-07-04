from nose.tools import eq_
from business_lookup import __version__
from test.component import ComponentTest


class TestPing(ComponentTest):
    def test_one(self):
        rv = self.get("business_lookup/ping")
        eq_(rv.status_code, 200)
        expected = '{{"version": "{}"}}'.format(__version__)
        eq_(rv.get_data(), expected)

    def test_404_handling(self):
        rv = self.get("business_lookup/total_garbage")
        eq_(rv.status_code, 404)
        expected = '{"errno": 404, "message": "404: Not Found"}'
        eq_(rv.get_data(), expected)
