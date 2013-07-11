# -*- coding: utf-8 -*-

import unittest
from smsapi.client import SmsAPI

# Your API username, and password
API_USERNAME = ''
API_PASSWORD =  ''

class SmsApiTestCase(unittest.TestCase):
        
    def setUp(self):

        self.api_username = API_USERNAME
        self.api_password = API_PASSWORD
        
        self.api = SmsAPI()

        self.api.set_username(self.api_username)
        self.api.set_password(self.api_password)
