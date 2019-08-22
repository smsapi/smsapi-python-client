# -*- coding: utf-8 -*-

import unittest

from smsapi.hrl.api import HlrResult
from tests import SmsApiTestCase


class HrlApiTest(SmsApiTestCase):

    def test_check_number(self):
        number = '48100200300'

        result = self.client.hlr.check_number(number=number, idx=['id1', 'id2'])

        expected_result = HlrResult(status='OK', number=number, id='1a2', price=0.1)

        self.assertEqual(expected_result, result)
        self.assertParamsForwardedToRequestEquals({'number': number, 'idx': 'id1|id2'})


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(HrlApiTest))
    return suite
