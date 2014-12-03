# -*- coding: utf-8 -*-

import unittest
from tests import SmsApiTestCase, PHONE_NUMBER
from smsapi.responses import ApiResponse


class ServicePhonebookTestCase(SmsApiTestCase):
    
    def setUp(self):
        super(ServicePhonebookTestCase, self).setUp()
        
        self.api.service('phonebook')

        self.group_name = None
        self.contact_number = None

    def test_group_add(self):

        self.api.action('group_add', {
             'name': 'test_group_1'
        })

        response = self.api.execute()
        
        self.group_name = 'test_group_1'        

        self.assertIsInstance(response, ApiResponse)
        self.assertEqual(response.name, 'test_group_1')

    def test_group_edit(self):
        
        self.api.action('group_add', {'name': 'test_group_2'})
        result1 = self.api.execute()
        
        self.api.action('group_edit', {
            'name': 'test_group_2',
            'new_name': 'new_test_group_2'
        })

        result2 = self.api.execute()
        
        self.group_name = 'new_test_group_2'
        
        self.assertIsInstance(result2, ApiResponse)
        self.assertNotEqual(result1.name, result2.name)

    def test_group_details(self):

        self.api.action('group_add', {'name': 'test_group_3'}).execute()

        response = self.api.action('group_details', {'name': 'test_group_3'}).execute()
        
        self.group_name = response.name
        
        self.assertIsInstance(response, ApiResponse)
        self.assertEqual(response.name, 'test_group_3')

    def test_contact_add(self):
        
        self.api.action('group_add', {'name': 'test_group_3'}).execute()
        
        self.group_name = 'test_group_3'         
        
        contact_data = {
            'number': PHONE_NUMBER,
            'first_name': 'test_firstname',
            'last_name': 'test_lastname',
            'info': 'test_info',
            'email': 'test@localhost.com',
            'birthday': '01-01-1970',
            'gender': 'male',
            'groups': ['test_group_3']
        }        
        
        result = self.api.action('contact_add', contact_data).execute()

        self.contact_number = result.number

        self.assertIsInstance(result, ApiResponse)
        self.assertTrue(result.number)
        self.assertTrue(result.first_name)
        self.assertTrue(result.last_name)
            
    def test_contact_delete(self):

        self.api.action('contact_add', {
            'number': PHONE_NUMBER,
            'first_name': 'test_firstname',
        })
        
        result = self.api.execute()
        
        result = self.api.action('contact_delete', {'number': result.number}).execute()
        
        self.assertTrue(result.deleted)

    def tearDown(self):
        if self.group_name:
            self.api.action('group_delete', {'name': self.group_name}).execute()
            
        if self.contact_number:
            self.api.action('contact_delete', {'number': self.contact_number}).execute()            


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ServicePhonebookTestCase))
    return suite