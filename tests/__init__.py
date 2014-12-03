# -*- coding: utf-8 -*-

import sys
import unittest
import pkgutil

from smsapi.client import SmsAPI

API_USERNAME = ''
API_PASSWORD = ''

PHONE_NUMBER = ''
SEND_DELAY = 360


class SmsApiTestCase(unittest.TestCase):
        
    def setUp(self):

        self.api_username = API_USERNAME
        self.api_password = API_PASSWORD
        
        self.api = SmsAPI()

        self.api.set_username(self.api_username)
        self.api.set_password(self.api_password)

    if sys.version_info[:2] == (2, 6):
        def assertIsInstance(self, x, y):
            assert isinstance(x, y), "%r is not instance of %r" % (x, y)

        def assertIsNotNone(self, x):
            assert x is not None, "%x is None" % x


def import_from_string(name):

    if '.' in name:
        module, pkg = name.rsplit(".", 1)
    else:
        return __import__(name)

    return getattr(__import__(module, None, None, [pkg]), pkg)


def app_test_suites():

    module = import_from_string(__name__)

    path = getattr(module, '__path__', None)

    if not path:
        raise ValueError('%s is not a package' % module)

    basename = module.__name__ + '.'

    for importer, module_name, is_pkg in pkgutil.iter_modules(path):
        mod = basename + module_name

        module = import_from_string(mod)

        if hasattr(module, 'suite'):
            yield module.suite()


def suite():

    suite = unittest.TestSuite()

    for _suite in app_test_suites():
        suite.addTest(_suite)

    return suite


def run_tests():
    try:
        unittest.TextTestRunner(verbosity=2).run(suite())
    except Exception as e:
        print('Error: %s' % e)


if __name__ == '__main__':
    run_tests()