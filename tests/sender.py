# -*- coding: utf-8 -*-

import unittest
from tests import SmsApiTestCase
from smsapi.responses import ApiResponse


class ServiceSenderTestCase(SmsApiTestCase):

    def setUp(self):
        super(ServiceSenderTestCase, self).setUp()
                
        self.api.service('sender')
        self.sender = None

    def test_add_sendername(self):
        
        response = self.api.action('add', {'name': 'test1'}).execute()

        self.assertIsInstance(response, ApiResponse)
        
        self.sender = 'test1'

    def test_sendername_status(self):
        
        self.api.action('add', {'name': 'test2'}).execute()
        response = self.api.action('status', {'name': 'test2'}).execute()
        
        self.assertIsInstance(response, ApiResponse)
        self.assertTrue(response.status)
        
        self.sender = 'test2'

    def test_sendername_delete(self):
        
        self.api.action('add', {'name': 'test3'}).execute()
        
        response = self.api.action('delete', {'name': 'test3'}).execute()
        
        self.assertIsInstance(response, ApiResponse)
        
    def test_sendername_list(self):
        
        response = self.api.action('list').execute()
        
        self.assertIsInstance(response, ApiResponse)

    def tearDown(self):

        if self.sender:
            self.api.action('delete', {'name': self.sender}).execute()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ServiceSenderTestCase))
    return suite

