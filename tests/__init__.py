# -*- coding: utf-8 -*-

import sys
import unittest
from smsapi.client import SmsAPI

# Your API username, and password
API_USERNAME = ''
API_PASSWORD = ''


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