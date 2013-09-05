# -*- coding: utf-8 -*-

import os
import time
import unittest
from tests import SmsApiTestCase
from smsapi.responses import ApiResponse, ApiError


class ServiceVmsTestCase(SmsApiTestCase):
    
    def setUp(self):
        super(ServiceVmsTestCase, self).setUp()

        self.api.service('vms')

        dir_path = os.path.dirname(__file__)

        self.message_params = {
           'to': '111222333',
           'content': '%s%s' % (dir_path, '/static/audio2.wav'),
           'date': time.time() + 360
        }

        self.message_id = None

    def test_send(self):
        
        self.api.action('send', self.message_params)
        
        try:
            response = self.api.execute()

            self.message_id = response.id        
            
            self.assertIsInstance(response, ApiResponse)
            self.assertIsNotNone(response.id)            
        except (ApiError) as e:
            print(e.code)

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
    suite.addTest(unittest.makeSuite(ServiceVmsTestCase))
    return suite