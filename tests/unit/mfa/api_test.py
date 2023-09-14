import unittest

from tests import SmsApiTestCase


class MfaApiTest(SmsApiTestCase):

    def test_send_mfa(self):
        number = '48100200300'

        self.client.mfa.send_mfa(phone_number=number)

        self.assertEqual('POST', self.request_fake.http_method)
        self.assertParamsForwardedToRequestEquals({
            "phone_number": number
        })

    def test_verify_mfa(self):
        code = 123
        number = '48100200300'

        self.client.mfa.verify_mfa(phone_number=number, code=code)

        self.assertEqual('POST', self.request_fake.http_method)
        self.assertParamsForwardedToRequestEquals({
            "phone_number": number,
            "code": "123"
        })


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(MfaApiTest))
    return suite
