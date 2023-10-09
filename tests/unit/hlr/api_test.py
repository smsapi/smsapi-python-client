import unittest

from smsapi.hlr.api import HlrResult
from tests import SmsApiTestCase


class HrlApiTest(SmsApiTestCase):

    def test_check_number(self):
        number = '48100200300'

        result = self.client.hlr.check_number(number=number, idx=['id1', 'id2'])

        expected_result = HlrResult(status='OK', number=number, id='1a2', price=0.1)

        self.assertRequestMethodIsPost()
        self.assertEqual(expected_result, result)
        self.assertRequestPayloadContains('number', number)
        self.assertRequestPayloadContains('idx', 'id1|id2')


def suite():
    s = unittest.TestSuite()
    s.addTest(unittest.makeSuite(HrlApiTest))
    return s
