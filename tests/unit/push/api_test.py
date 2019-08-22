# -*- coding: utf-8 -*-

import unittest

from smsapi.push.models import \
    PushShipment, PushApp, \
    PushShipmentSummary, PushShipmentDispatchDetails, \
    PushShipmentFallback, PushShipmentPayload

from tests import SmsApiTestCase


class PushApiTest(SmsApiTestCase):

    def test_send_push(self):
        app_id = '1'
        alert = 'message'

        args = {'app_id': app_id, 'alert': alert}

        r = self.client.push.send(**args)

        expected_result = create_push_shipment(app_id)
        expected_args = {'app_id': app_id, 'data': {'alert': alert}}

        self.assertEqual(expected_result, r)
        self.assertEqual(expected_args, self.request_fake.data)

    def test_send_push_with_extra_data(self):
        app_id = '1'

        args = {'app_id': app_id, 'alert': '', 'title': '', 'uri': '',
                'content-available': '', 'sound': '', 'badge': '', 'category': ''}

        self.client.push.send(**args)

        expected_args = {'app_id': app_id, 'data': {'alert': '', 'title': '', 'uri': '', 'content-available': '',
                                                    'sound': '', 'badge': '', 'category': ''}}

        self.assertEqual(expected_args, self.request_fake.data)

    def test_send_push_with_sms_fallback(self):
        args = {'app_id': '1', 'fallback_message': '', 'fallback_delay': '', 'fallback_from': ''}

        self.client.push.send(**args)

        expected_args = {'app_id': '1', 'fallback': {'message': '', 'delay': '', 'from': ''}}

        self.assertEqual(expected_args, self.request_fake.data)


def create_push_shipment(app_id):

    app = PushApp(id='1', name='app1')
    summary = PushShipmentSummary(points='0.1', recipients_count=1)
    dispatch_details = PushShipmentDispatchDetails()
    fallback = PushShipmentFallback(message='sms message', from_='default', delay=360)
    payload = PushShipmentPayload(alert='message')

    return PushShipment(id='1', app_id=app_id, app=app, summary=summary, status='QUEUED',
                        date_created='1460969712', scheduled_date='1460969712',
                        dispatch_details=dispatch_details, fallback=fallback,
                        payload=payload)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(PushApiTest))
    return suite
