# -*- coding: utf-8 -*-

import unittest

from smsapi.exception import EndpointException, SendException
from smsapi.models import ResultCollection, RemoveMessageResult, InvalidNumber
from smsapi.sms.api import flash_force_params, fast_force_params
from tests import SmsApiTestCase
from tests.doubles import api_response_fixture


class SmsApiTest(SmsApiTestCase):

    def test_send_sms(self):
        number = '48100200300'
        args = {'to': number}

        result = self.client.sms.send(**args)

        self.assertSendResultForNumberEquals(number, result)
        self.assertParamsForwardedToRequestEquals(args)

    @api_response_fixture('send')
    def test_send_sms_with_custom_sender(self):
        number = '48100200300'
        any_sender_name = 'any-sender-name'

        result = self.client.sms.send(to=number, from_=any_sender_name)

        self.assertSendResultForNumberEquals(number, result)
        self.assertParamsForwardedToRequestEquals({'to': number, 'from': any_sender_name})

    @api_response_fixture('send_to_many_recipients')
    def test_send_sms_to_many_numbers(self):
        number_1, number_2 = '48100200300', '48100200301'

        result = self.client.sms.send(to=[number_1, number_2])

        self.assertSendResultForNumberEquals([number_1, number_2], result)
        self.assertParamsForwardedToRequestEquals({'to': '%s,%s' % (number_1, number_2)})

    @api_response_fixture('send_to_invalid_number')
    def test_send_sms_to_invalid_number(self):

        invalid_number = '48100200300'
        exception = None

        try:
            self.client.sms.send(to=invalid_number)
        except SendException as e:
            exception = e

        expected_exception = create_sms_exception_for_number(invalid_number)

        self.assertEqual(expected_exception, exception)

    def test_send_fast(self):
        number = '48100200300'
        args = {'to': number}

        result = self.client.sms.send_fast(**args)

        self.assertSendResultForNumberEquals(number, result)
        self.assertParamsForwardedToRequestEquals(args, fast_force_params)

    def test_send_flash(self):
        number = '48100200300'
        args = {'to': number}

        result = self.client.sms.send_flash(**args)

        self.assertSendResultForNumberEquals(number, result)
        self.assertParamsForwardedToRequestEquals(args, flash_force_params)

    def test_remove_scheduled_sms(self):
        sms_id = '1'
        args = {'id': sms_id}

        result = self.client.sms.remove_scheduled(id=sms_id)

        expected_result = ResultCollection(1, [RemoveMessageResult(id='1')])

        self.assertParamsForwardedToRequestEquals(args)
        self.assertEqual(expected_result, result)

    @api_response_fixture('remove_not_exists_sms')
    def test_remove_not_exists_sms(self):
        exception = None

        try:
            self.client.sms.remove_scheduled(id='1')
        except EndpointException as e:
            exception = e

        expected_exception = EndpointException(u'Not exists ID message', 301)

        self.assertEqual(expected_exception, exception)

    @api_response_fixture('send')
    def test_send_personalized_sms(self):
        args = {'to': '48100200300', 'message': 'some message [%1]', 'param1': ['p1', 'p2']}

        self.client.sms.send(**args)

        self.assertParamsForwardedToRequestEquals(args, {'param1': 'p1|p2'})

    @api_response_fixture('send')
    def test_send_sms_with_own_identifier(self):
        args = {'to': '48100200300', 'idx': ['id1', 'id2']}

        self.client.sms.send(**args)

        self.assertParamsForwardedToRequestEquals(args, {'idx': 'id1|id2'})

    @api_response_fixture('send')
    def test_send_sms_to_group(self):
        self.client.sms.send_to_group(group='any')

        self.assertParamsForwardedToRequestEquals({'group': 'any'})

    def test_send_sms_as_utf8(self):
        number = '48100200300'
        args = {'to': number, 'encoding': 'utf-8'}

        result = self.client.sms.send(**args)

        self.assertSendResultForNumberEquals(number, result)
        self.assertParamsForwardedToRequestEquals(args)

    def test_send_test_sms(self):
        number = '48100200300'
        args = {'to': number, 'test': '1'}

        self.client.sms.send(**args)

        self.assertParamsForwardedToRequestEquals(args)


def create_sms_exception_for_number(number):
    e = SendException(u'No correct phone numbers', 13)
    e.add_invalid_number(InvalidNumber(number, number, u'Invalid phone number'))
    return e


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(SmsApiTest))
    return suite
