# -*- coding: utf-8 -*-

import time
import unittest
from tests import SmsApiTestCase, PHONE_NUMBER, SEND_DELAY
from smsapi.responses import ApiResponse


class ServiceSmsTestCase(SmsApiTestCase):
    
    def setUp(self):
        super(ServiceSmsTestCase, self).setUp()
        
        self.api.service('sms')

        self.message_params = {
           'content': 'test message',
           'to': PHONE_NUMBER,
           'date': time.time() + SEND_DELAY
        }

        self.message_id = None

    def test_send(self):
        
        self.api.action('send', self.message_params)

        response = self.api.execute()
        
        self.message_id = response.id        
        
        self.assertIsInstance(response, ApiResponse)
        self.assertIsNotNone(response.id)
                
    def test_delete(self):        
        
        self.api.action('send', self.message_params)
        send_response = self.api.execute()

        self.api.action('delete', {'id': send_response.id})
        delete_response = self.api.execute()
        
        self.assertEqual(send_response.id, delete_response.id)
        self.assertIsInstance(delete_response, ApiResponse)        
        
    def test_get(self):
        
        self.api.action('send', self.message_params)
        
        send_response = self.api.execute()
        
        self.message_id = send_response.id
                
        self.api.action('get', {'id': send_response.id})
        get_response = self.api.execute()
        
        self.assertEqual(send_response.id, get_response.id)
        self.assertIsInstance(get_response, ApiResponse)
        
    def tearDown(self):
        
        if self.message_id:
            self.api.action('delete', {'id': self.message_id})
            self.api.execute()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ServiceSmsTestCase))
    return suite