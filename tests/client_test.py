# -*- coding: utf-8 -*-

import unittest
from requests.auth import HTTPBasicAuth

from smsapi import lib_info
from smsapi.auth import BearerAuth
from smsapi.client import Client
from smsapi.compat import py_version
from smsapi.exception import ClientException
from tests import SmsApiTestCase


class ClientTest(SmsApiTestCase):

    def test_use_bearer_auth_when_access_token_provided(self):
        token = 'some-token'

        client = Client('some-domain', access_token=token)

        self.assertEqual(BearerAuth(access_token=token), client.auth)

    def test_use_basic_auth_when_credentials_provided(self):
        username = 'some-username'
        password = 'some-password'

        client = Client('some-domain', None, username=username, password=password)

        self.assertIsInstance(client.auth, HTTPBasicAuth)
        self.assertEqual(username, client.auth.username)
        self.assertEqual(password, client.auth.password)


    def test_error_when_create_client_without_any_credentials(self):
        self.assertRaises(ClientException, Client, 'some-domain')

    def test_add_request_id_for_http_requests(self):
        self.make_any_client_call()

        self.assertTrue('X-Request-Id' in self.request_fake.headers)

    def test_add_request_header_with_library_and_python_version(self):
        self.make_any_client_call()

        expected_user_agent_header = {'User-Agent': '%s (Python%s)' % (lib_info, py_version)}

        self.assertDictContainsSubset(expected_user_agent_header, self.request_fake.headers)

    def make_any_client_call(self):
        self.client.sms.send()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ClientTest))
    return suite