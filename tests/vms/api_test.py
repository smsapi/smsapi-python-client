# -*- coding: utf-8 -*-

import os
import unittest
from smsapi.exception import EndpointException
from smsapi.models import ResultCollection, RemoveMessageResult
from tests import SmsApiTestCase, create_send_result
from tests.doubles import api_response_fixture


class VmsApiTest(SmsApiTestCase):

    def test_send_vms(self):
        number = '48100200300'
        args = {'to': number}

        result = self.client.vms.send(**args)

        self.assertParamsForwardedToRequestEquals(args)
        self.assertSendResultForNumberEquals(number, result)

    def test_send_vms_from_file(self):

        wave_file_path = os.path.join(os.path.dirname(__file__), 'fixtures/example.wav')

        args = {'to': '48100200300', 'file': wave_file_path}

        self.client.vms.send(**args)

        self.assertEqual(open(wave_file_path, 'rb').read(), self.request_fake.files.get('file').read())

    def test_send_vms_from_remote_file(self):
        args = {'to': '48100200300', 'file': 'http://somedomain.com/somefile.wav'}

        self.client.vms.send(**args)

        self.assertParamsForwardedToRequestEquals(args)

    def test_send_vms_with_own_identifiers(self):
        number = '48100200300'
        args = {'to': number, 'idx': ['id1', 'id2']}

        result = self.client.vms.send(**args)

        self.assertParamsForwardedToRequestEquals(args, {'idx': 'id1|id2'})
        self.assertSendResultForNumberEquals(number, result)

    @api_response_fixture('send')
    def test_send_vms_to_group(self):
        args = {'group': 'any'}

        result = self.client.vms.send_to_group(**args)

        expected_result = ResultCollection(1, [create_send_result('48100200300')])

        self.assertParamsForwardedToRequestEquals(args)
        self.assertEqual(expected_result, result)

    def test_remove_scheduled_vms(self):
        vms_id = '1'
        args = {'id': vms_id}

        result = self.client.vms.remove_scheduled(**args)

        expected_result = ResultCollection(1, [RemoveMessageResult(id=vms_id)])

        self.assertParamsForwardedToRequestEquals(args)
        self.assertEqual(expected_result, result)

    @api_response_fixture('remove_not_exists_vms')
    def test_remove_not_exists_vms(self):
        exception = None

        try:
            self.client.vms.remove_scheduled(id='1')
        except EndpointException as e:
            exception = e

        expected_exception = EndpointException(u'Not exists ID message', 301)

        self.assertEqual(expected_exception, exception)

    def test_send_test_vms(self):
        number = '48100200300'
        args = {'to': number, 'test': '1'}

        self.client.vms.send(**args)

        self.assertParamsForwardedToRequestEquals(args)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(VmsApiTest))
    return suite
