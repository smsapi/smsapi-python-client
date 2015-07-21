# -*- coding: utf-8 -*-

import json
import unittest
from tests import SmsApiTestCase
from smsapi.responses import ApiResponse, ApiError


class ApiResponseTestCase(SmsApiTestCase):

    def setUp(self):
        super(ApiResponseTestCase, self).setUp()

        class HttpResponse(object):
            
            def __init__(self):
                self.data = None
                
            def read(self):
                return self.data
            
            def getcode(self):
                return 200
            
            def geturl(self):
                return 'https://api.smsapi.pl/'
            
        self.response_obj = HttpResponse()
        
    def test_single_response(self):
        
        data = {'k1': 'v1', 'k2': 'v2'}
    
        self.response_obj.data = json.dumps(data)
        
        result = ApiResponse(self.response_obj)
        
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.k1, 'v1')
        self.assertEqual(result.k1, 'v1')

    def test_list_response(self):
        
        data = [
            {'k1': 'v1', 'k2': 'v2'}, 
            {'k1': 'v1', 'k2': 'v2'}, 
            {'k1': 'v1', 'k2': 'v2'},
        ]

        self.response_obj.data = json.dumps(data)

        result = ApiResponse(self.response_obj)
        
        self.assertEqual(result.status_code, 200)

        self.assertEqual(result.k1, 'v1')
        self.assertEqual(result.k2, 'v2')
        
        for r in result:
            self.assertEqual(r.k1, 'v1')
            self.assertEqual(r.k2, 'v2')
        
    def test_response_with_list(self):
        
        data = {'list': [
             {'k1': 'v1', 'k2': 'v2'}, 
             {'k1': 'v1', 'k2': 'v2'}, 
             {'k1': 'v1', 'k2': 'v2'},
        ]}

        self.response_obj.data = json.dumps(data)

        result = ApiResponse(self.response_obj)

        self.assertEqual(result.status_code, 200)

        self.assertEqual(result.k1, 'v1')
        self.assertEqual(result.k2, 'v2')

        for r in result:
            self.assertEqual(r.k1, 'v1')
            self.assertEqual(r.k2, 'v2')

    def test_responses_empty_list(self):

        data = {'count': 1, 'list': []}

        self.response_obj.data = json.dumps(data)

        result = ApiResponse(self.response_obj)

        self.assertEqual(result.count, 1)

    def test_error_response(self):
    
        data = {'error': 'some error message'}
        
        self.response_obj.data = json.dumps(data)

        self.assertRaises(ApiError, ApiResponse, self.response_obj)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ApiResponseTestCase))
    return suite
