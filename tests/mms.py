# -*- coding: utf-8 -*-

import os
import time
import unittest
from tests import SmsApiTestCase, PHONE_NUMBER, SEND_DELAY
from smsapi.responses import ApiResponse


class ServiceMmsTestCase(SmsApiTestCase):
    
    def setUp(self):
        super(ServiceMmsTestCase, self).setUp()
        
        self.api.service('mms')

        self.message_params = {
           'to': PHONE_NUMBER,
           'subject': 'subject',
           'date': time.time() + SEND_DELAY
        }

        dir_path = os.path.dirname(__file__)

        self.message_content = 'test message'
        self.image_file = "%s%s" % (dir_path, '/static/image.jpg')
        self.video_file = "%s%s" % (dir_path, '/static/video.mp4')

        self.message_id = None

    def test_send(self):

        self.api.action('send', self.message_params)
        
        self.api.add_text(self.message_content)
        self.api.add_image(self.image_file)
        self.api.add_video(self.video_file)

        response = self.api.execute()
        self.message_id = response.id

        self.assertIsInstance(response, ApiResponse)
        self.assertIsNotNone(response.id)
                
    def test_delete(self):        
        
        self.api.action('send', self.message_params)
        self.api.add_text(self.message_content)
        
        send_response = self.api.execute()

        self.api.action('delete', {'id': send_response.id})
        delete_response = self.api.execute()
        
        self.assertEqual(send_response.id, delete_response.id)
        self.assertIsInstance(delete_response, ApiResponse)
        
    def test_get(self):
        
        self.api.action('send', self.message_params)
        self.api.add_text(self.message_content)
        
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
    suite.addTest(unittest.makeSuite(ServiceMmsTestCase))
    return suite