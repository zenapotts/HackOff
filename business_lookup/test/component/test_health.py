from nose.tools import eq_
from test.component import ComponentTest
import json


class TestHealth(ComponentTest):
    def test_one(self):
        rv = self.get("business_lookup/health")
        eq_(rv.status_code, 200)

        data = json.loads(rv.get_data())
        assert 'condition' in data, 'Should expose condition'
