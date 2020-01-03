import unittest

from smsapi.blacklist.models import BlacklistPhoneNumber
from smsapi.models import ModelCollection
from tests import SmsApiTestCase
from tests.unit.doubles import api_response_fixture


class BlacklistApiTest(SmsApiTestCase):

    @api_response_fixture("phonenumber", "blacklist")
    def test_add_phone_number_to_blacklist(self):
        phone_number = "654543432"
        expire_at = "2060-01-01T20:00:00Z"

        result = self.client.blacklist.add_phone_number(phone_number=phone_number, expire_at=expire_at)

        expected_result = BlacklistPhoneNumber(
            id="1",
            phone_number="654543432",
            expire_at=expire_at,
            created_at="2017-07-21T17:32:28Z"
        )

        self.assertEqual('POST', self.request_fake.http_method)
        self.assertEqual({"phone_number": phone_number, "expire_at": expire_at}, self.request_fake.data)
        self.assertTrue(self.request_fake.url.endswith('blacklist/phone_numbers'))
        self.assertEqual(expected_result, result)

    def test_delete_phone_number_from_blacklist(self):
        phone_number_blacklist_id = "1"

        self.client.blacklist.delete_phone_number(id=phone_number_blacklist_id)

        self.assertEqual("DELETE", self.request_fake.http_method)
        self.assertTrue(self.request_fake.url.endswith("blacklist/phone_numbers/1"))

    def test_delete_all_phone_numbers_from_blacklist(self):
        self.client.blacklist.delete_all_phone_numbers()

        self.assertEqual("DELETE", self.request_fake.http_method)
        self.assertTrue(self.request_fake.url.endswith("blacklist/phone_numbers"))

    @api_response_fixture("collection", "blacklist")
    def test_get_all_phone_numbers_from_blacklist(self):
        result = self.client.blacklist.list_phone_numbers()

        expected_result = ModelCollection(1, [
            BlacklistPhoneNumber(
                id="1",
                phone_number="654543432",
                expire_at="2060-01-01T20:00:00Z",
                created_at="2017-07-21T17:32:28Z"
            )
        ])

        self.assertEqual(expected_result, result)
        self.assertEqual("GET", self.request_fake.http_method)
        self.assertTrue(self.request_fake.url.endswith("blacklist/phone_numbers"))


def suite():
    s = unittest.TestSuite()
    s.addTest(unittest.makeSuite(BlacklistApiTest))
    return s
