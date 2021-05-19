# -*- coding: utf-8 -*-

import os
import json
import unittest
import pkgutil
import requests

from smsapi.api import Api
from smsapi.client import SmsApiPlClient
from smsapi.models import ResultCollection
from smsapi.sms import response_format_param
from smsapi.sms.model import SmsSendResult

from tests.unit.doubles import ApiSpy, request_fake
from tests.unit.fixtures import create_send_result

requests.request = request_fake


class SmsApiTestCase(unittest.TestCase):

    def setUp(self):
        self.request_fake = request_fake

        self.client = SmsApiPlClient(access_token='some-access-token')

        spy_endpoints(self.client)

    def load_fixture(self, dir, fixture):
        with open(os.path.abspath(os.path.dirname(__file__)) + '/%s/fixtures/%s.json' % (dir, fixture)) as f:
            data = f .read()

        return json.loads(data)

    def assertParamsForwardedToRequestEquals(self, params, *args):
        for d in args:
            params.update(d or {})

        params.update(response_format_param)

        self.assertEqual(params, self.request_fake.payload)

    def assertRequestPayloadContains(self, key, value):
        self.assertIn(key, self.request_fake.payload.keys())
        self.assertIn(value, self.request_fake.payload.values())

    def assertSendResultForNumberEquals(self, number, result, result_class=ResultCollection):
        numbers = number if isinstance(number, list) else [number]

        expected_result = result_class(len(numbers), [create_send_result(n) for n in numbers])

        self.assertEqual(expected_result, result)

    def assertSmsSendResultForNumberEquals(self, number, result):
        self.assertSendResultForNumberEquals(number, result, result_class=SmsSendResult)


def spy_endpoints(client):

    for attr in client.__dict__:
        if isinstance(client.__dict__[attr], Api):
            client.__dict__[attr] = ApiSpy(client.__dict__[attr])


def import_from_string(name):

    if '.' in name:
        module, pkg = name.rsplit(".", 1)
    else:
        return __import__(name)

    return getattr(__import__(module, None, None, [pkg]), pkg)


def app_test_suites(module_name):

    module = import_from_string(module_name)

    path = getattr(module, '__path__', None)

    if not path:
        raise ValueError('%s is not a package' % module)

    basename = module.__name__ + '.'

    for importer, module_name, is_pkg in pkgutil.iter_modules(path):
        module_name = basename + module_name

        if is_pkg:
            for suite in app_test_suites(module_name):
                yield suite

        module = import_from_string(module_name)

        if hasattr(module, 'suite'):
            yield module.suite()


def suite():
    suite = unittest.TestSuite()
    for _suite in app_test_suites(__name__):
        suite.addTest(_suite)
    return suite


def run_tests():
    try:
        unittest.TextTestRunner(verbosity=2).run(suite())
    except Exception as e:
        print('Error: %s' % e)


if __name__ == '__main__':
    run_tests()