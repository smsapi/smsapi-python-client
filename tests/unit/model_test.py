# -*- coding: utf-8 -*-

import unittest

from smsapi.models import InvalidNumber, ResultCollection, SendResult
from tests import SmsApiTestCase


class ModelTest(SmsApiTestCase):

    def test_iterate_over_results(self):
        model1 = SendResult(id=1, points=0.1)
        model2 = SendResult(id=2, points=0.2)

        r = ResultCollection(2, [model1, model2])

        self.assertEqual(model1, r.next())
        self.assertEqual(model2, r.next())


class InvalidNumberTest(SmsApiTestCase):

    def setUp(self):
        self.invalid_number = InvalidNumber('123', '123', 'Invalid phone number')
        self.matching_dict = {'number': '123', 'submitted_number': '123', 'reason': 'Invalid phone number'}

    def test_equals_instance(self):
        other = InvalidNumber('123', '123', 'Invalid phone number')

        self.assertEqual(self.invalid_number, other)

    def test_equals_matching_dict(self):
        self.assertEqual(self.invalid_number, self.matching_dict)

    def test_not_equals_mismatched_dict(self):
        self.assertNotEqual(self.invalid_number, {'number': '999', 'submitted_number': '999', 'reason': 'Invalid phone number'})

    def test_not_equals_none(self):
        self.assertNotEqual(self.invalid_number, None)

    def test_not_equals_unrelated_type(self):
        self.assertNotEqual(self.invalid_number, '123')


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ModelTest))
    suite.addTest(unittest.makeSuite(InvalidNumberTest))
    return suite
