# -*- coding: utf-8 -*-

import unittest
from . import SmsApiTestCase
from smsapi.proxy import ApiHttpProxy, ApiProxyError

class ApiProxyTestCase(SmsApiTestCase):

    def setUp(self):
        
        self.proxy = ApiHttpProxy('https://ssl.smsapi.pl/')

    def test_connection(self):
        result = self.proxy.execute()
        
        self.assertTrue(result.read)
        self.assertTrue(result.getcode)
        self.assertTrue(result.geturl)

    def test_invalid_multiple_hosts_connection(self):

        self.proxy.set_hostname(('host1', 'host2', 'host3'))

        self.assertRaises(ApiProxyError, self.proxy.execute, '')

    def test_invalid_host_connection(self):
    
        self.proxy.set_hostname('host')

        self.assertRaises(ApiProxyError, self.proxy.execute, '')

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ApiProxyTestCase))
    return suite
    

