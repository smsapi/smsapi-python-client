# -*- coding: utf-8 -*-

import unittest

from smsapi.models import ResultCollection
from smsapi.sender.models import SenderNameResult, SenderNameSuccessResult
from tests import SmsApiTestCase
from tests.doubles import api_response_fixture


class SenderApiTest(SmsApiTestCase):

    @api_response_fixture('success_response')
    def test_add_sender_name(self):
        name = 'any'
        result = self.client.sender.add(name=name)

        expected_result = SenderNameSuccessResult(1)

        self.assertEqual(expected_result, result)
        self.assertParamsForwardedToRequestEquals({'add': name})

    @api_response_fixture('check_sender_name')
    def test_check_sender_name(self):
        name = 'any'
        result = self.client.sender.check(name=name)

        expected_result = create_sender_name_result(name)

        self.assertEqual(expected_result, result)
        self.assertParamsForwardedToRequestEquals({'status': name})

    @api_response_fixture('success_response')
    def test_remove_sender_name(self):
        name = 'any'

        result = self.client.sender.remove(name=name)

        expected_result = SenderNameSuccessResult(1)

        self.assertEqual(expected_result, result)
        self.assertParamsForwardedToRequestEquals({'delete': name})

    def test_list_sender_names(self):
        result = self.client.sender.list()

        expected_result = ResultCollection(2, [
            create_sender_name_result('any'),
            create_sender_name_result('some'),
        ])

        self.assertEqual(expected_result, result)
        self.assertParamsForwardedToRequestEquals({'list': True})

    @api_response_fixture('success_response')
    def test_set_default_sender_name(self):
        name = 'any'

        result = self.client.sender.default(name=name)

        expected_result = SenderNameSuccessResult(1)

        self.assertEqual(expected_result, result)
        self.assertParamsForwardedToRequestEquals({'default': name})


def create_sender_name_result(name):
    return SenderNameResult(name, 'ACTIVE', False)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(SenderApiTest))
    return suite
