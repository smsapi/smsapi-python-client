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
             'user': 'test.user.1',
             'password': 'test.user.1' 
        })

        response = self.api.execute()

        self.assertIsInstance(response, ApiResponse)
        self.assertEqual(response.username, '%s_test.user.1' % self.api_username)

    def test_edit_subuser(self):
        
        self.api.action('add_subuser', {
             'user': 'test.user.2',
             'password': 'test.user.2' 
        })

        response1 = self.api.execute()
        
        self.api.action('edit_subuser', {
             'user': 'test.user.2',
             'limit': 100,
             'active': 1                                       
        })

        response2 = self.api.execute()

        self.assertIsInstance(response2, ApiResponse)

        self.assertEqual(response1.limit, 0)
        self.assertFalse(response1.active)
        
        self.assertEqual(response2.status_code, 200)
        self.assertEqual(response2.limit, 100)
        self.assertTrue(response2.active)

    def test_subuser_details(self):
        
        self.api.action('add_subuser', {
             'user': 'test.user.3',
             'password': 'test.user.3',
             'limit': 50,
             'month_limit': 20 
        })
        
        self.api.execute()
        
        self.api.action('subuser_details')
        self.api.set_user('%s_test.user.3' % self.api_username)
        
        response = self.api.execute()

        self.assertIsInstance(response, ApiResponse)
        self.assertFalse(response.active)
        self.assertEqual(response.limit, 50)
        self.assertEqual(response.month_limit, 20)

    def test_account_details(self):
        
        response = self.api.action('account_details').execute()
        
        self.assertTrue(response.points)

    def test_subuser_list(self):
        
        response = self.api.action('list_subuser').execute()
        
        self.assertIsInstance(response, ApiResponse)
        
        for u in list:
            print u.username


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ServiceClientTestCase))
    return suite
    

