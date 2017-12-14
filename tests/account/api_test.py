# -*- coding: utf-8 -*-

import unittest
from smsapi.account.models import AccountBalanceResult, UserResult
from smsapi.models import ResultCollection

from tests import SmsApiTestCase
from tests.doubles import api_response_fixture


class AccountApiTest(SmsApiTestCase):

    @api_response_fixture('balance', 'account')
    def test_account_balance(self):
        result = self.client.account.balance()

        expected_result = AccountBalanceResult(
            points = 100.00,
            pro_count = 606,
            eco_count = 1428,
            mms_count = 333,
            vms_gsm_count = 476,
            vms_land_count = 714
        )

        self.assertParamsForwardedToRequestEquals({'credits': 1, 'details': 1})
        self.assertEqual(expected_result, result)

    @api_response_fixture('user', 'account')
    def test_create_user(self):
        name, password, api_password = 'some', 'some-password', 'some-api-password'

        result = self.client.account.create_user(name=name, password=password, api_password=api_password)

        expected_result = create_user_result()

        self.assertEqual(expected_result, result)
        self.assertParamsForwardedToRequestEquals({'add_user': name, 'pass': password, 'pass_api': api_password})

    @api_response_fixture('user', 'account')
    def test_update_user(self):
        name, password = 'some', 'some-password'

        result = self.client.account.update_user(name=name, password=password)

        expected_result = create_user_result()

        self.assertEqual(expected_result, result)
        self.assertParamsForwardedToRequestEquals({'set_user': name, 'pass': password})

    @api_response_fixture('user', 'account')
    def test_get_user(self):
        name = 'some'

        result = self.client.account.user(name=name)

        expected_result = create_user_result()

        self.assertEqual(expected_result, result)
        self.assertParamsForwardedToRequestEquals({'get_user': name})

    @api_response_fixture('users_list', 'account')
    def test_list_users(self):

        result = self.client.account.list_users()

        expected_result = ResultCollection(2, [
            create_user_result(name='some'),
            create_user_result(name='any'),
        ])

        self.assertEqual(expected_result, result)
        self.assertParamsForwardedToRequestEquals({'list': 1})


def create_user_result(name='some'):
    return UserResult(username=name, limit=0, month_limit=0,
                      senders=0, phonebook=0, active=False, info="some")


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(AccountApiTest))
    return suite