# -*- coding: utf-8 -*-

import unittest

from smsapi.models import ResultCollection, SendResult
from tests import SmsApiTestCase


class ModelTest(SmsApiTestCase):

    def test_iterate_over_results(self):
        model1 = SendResult(id=1, points=0.1)
        model2 = SendResult(id=2, points=0.2)

        r = ResultCollection(2, [model1, model2])

        self.assertEqual(model1, r.next())
        self.assertEqual(model2, r.next())


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ModelTest))
    return suite