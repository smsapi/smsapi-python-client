import unittest

from smsapi.exception import EndpointException
from smsapi.models import ResultCollection, RemoveMessageResult
from tests import SmsApiTestCase
from tests.unit.doubles import api_response_fixture


class MmsApiTest(SmsApiTestCase):

    def test_send_mms(self):
        number = '48100200300'

        result = self.client.mms.send(to=number, smil='any', subject='any')

        self.assertRequestMethodIsPost()
        self.assertSendResultForNumberEquals(number, result)
        self.assertRequestPayloadContains("to", number)
        self.assertRequestPayloadContains("smil", 'any')
        self.assertRequestPayloadContains("subject", 'any')


    def test_send_personalized_mms(self):
        number = '48100200300'

        self.client.mms.send(to=number, idx= ['id1', 'id2'])

        self.assertRequestMethodIsPost()
        self.assertRequestPayloadContains("idx", "id1|id2")

    @api_response_fixture('send')
    def test_send_mms_to_group(self):
        self.client.mms.send_to_group(group="any")

        self.assertRequestMethodIsPost()
        self.assertRequestPayloadContains("group", "any")

    def test_remove_scheduled_mms(self):
        result = self.client.mms.remove_scheduled(id='1')

        expected_result = ResultCollection(1, [RemoveMessageResult(id='1')])

        self.assertRequestMethodIsPost()
        self.assertEqual(expected_result, result)
        self.assertRequestPayloadContains("sch_del", "1")

    @api_response_fixture('remove_not_exists_mms')
    def test_remove_not_exists_mms(self):
        exception = None

        try:
            self.client.mms.remove_scheduled(id='1')
        except EndpointException as e:
            exception = e

        expected_exception = EndpointException(u'Not exists ID message', 301)

        self.assertEqual(expected_exception, exception)

    def test_send_test_mms(self):
        number = '48100200300'
        args = {'to': number, 'test': '1'}

        self.client.mms.send(**args)

        self.assertRequestMethodIsPost()
        self.assertRequestPayloadContains("test", "1")

def suite():
    s = unittest.TestSuite()
    s.addTest(unittest.makeSuite(MmsApiTest))
    return s
