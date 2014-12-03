# -*- coding: utf-8 -*-

import unittest
from tests import SmsApiTestCase
from smsapi.responses import ApiResponse


class ServiceClientTestCase(SmsApiTestCase):
    
    def setUp(self):
        super(ServiceClientTestCase, self).setUp()
        
        self.api.service('client')
        self.subuser_id = None

    def test_add_subuser(self):

        self.api.action('add_subuser', {
             'username': 'test.user.1',
             'password': 'test.user.1'
        })

        response = self.api.execute()

        self.assertIsInstance(response, ApiResponse)
        self.assertEqual(response.username, '%s_test.user.1' % self.api_username)

    def test_edit_subuser(self):
        
        self.api.action('add_subuser', {
             'username': 'test.user.2',
             'password': 'test.user.2' 
        })

        response1 = self.api.execute()
        
        self.api.action('edit_subuser', {
             'username': 'test.user.2',
             'active': 1                                       
        })

        response2 = self.api.execute()

        self.assertIsInstance(response2, ApiResponse)

        self.assertEqual(response1.limit, 0)
        self.assertFalse(response1.active)
        
        self.assertEqual(response2.status_code, 200)
        self.assertTrue(response2.active)

    def test_subuser_details(self):

        month_limit = 20.0000

        self.api.action('add_subuser', {
             'username': 'test.user.3',
             'password': 'test.user.3',
             'month_limit': month_limit
        })

        self.api.execute()

        self.api.action('subuser_details')
        self.api.set_user('test.user.3')

        response = self.api.execute()

        self.assertIsInstance(response, ApiResponse)
        self.assertEqual(0, int(response.active))
        self.assertEqual(month_limit, float(response.month_limit))

    def test_account_details(self):

        response = self.api.action('account_details').execute()

        self.assertTrue(response.points)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ServiceClientTestCase))
    return suite