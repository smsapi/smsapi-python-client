# -*- coding: utf-8 -*-

import os
import unittest

from smsapi.models import ModelCollection
from smsapi.short_url.models import ShortUrlClick, ShortUrlClickMessage, ShortUrlClickByMobileDevice, ShortUrl
from smsapi.utils import dict_replace
from tests import SmsApiTestCase
from tests.doubles import api_response_fixture


def create_short_url_click():

    message = ShortUrlClickMessage(id='1', idx='1', recipient="100200300")

    return ShortUrlClick(
        idzdo_id="1",
        phone_number="100200300",
        date_hit="2015-09-20T17:00:00+0200",
        name="name1",
        short_url="http:/idz.do/name1",
        os="Windows",
        browser="Firefox",
        device="PC",
        suffix="test1",
        message=message)


def create_short_url_click_by_mobile_device():

    return ShortUrlClickByMobileDevice(link_id=1, android=0, ios=0, wp=0, other=1, sum=1)


def create_short_url_link():

    return ShortUrl(
        id="1",
        name="test1",
        url="http://invoid.pl",
        short_url="http://idz.do/test1",
        type="URL",
        expire="2037-12-02T15:14:36+00:00",
        hits=0,
        hits_unique=0,
        description="test1")


def create_collection(data):
    return ModelCollection(len(data), data)


class ShortUrlApiTest(SmsApiTestCase):

    def test_get_clicks(self):
        args = {'date_from': 'some date', 'date_to': 'another date', 'links': ['1', '2']}

        r = self.client.shorturl.get_clicks(**args)

        expected_result = create_collection([create_short_url_click()])
        expected_args = dict_replace(args, 'links', {'links[]': ['1', '2']})

        self.assertEqual(expected_result, r)
        self.assertEqual(expected_args, self.request_fake.params)

    def test_get_clicks_by_mobile_device(self):
        args = {'links': ['1']}

        r = self.client.shorturl.get_clicks_by_mobile_device(**args)

        expected_result = create_collection([create_short_url_click_by_mobile_device()])

        self.assertEqual(expected_result, r)
        self.assertEqual(dict_replace(args, 'links', {'links[]': ['1']}), self.request_fake.params)

    def test_list_short_urls(self):
        r = self.client.shorturl.list_short_urls()

        expected_result = create_collection([create_short_url_link()])

        self.assertEqual(expected_result, r)

    @api_response_fixture('short_url')
    def test_create_short_url(self):

        args = {'url': 'some url', 'name': 'name', 'expire': 'some expiration datetime', 'description': 'description'}

        r = self.client.shorturl.create_short_url(**args)

        expected_result = create_short_url_link()

        self.assertEqual(expected_result, r)

    @api_response_fixture('short_url')
    def test_create_short_url_with_file(self):
        path = os.path.join(os.path.dirname(__file__), 'fixtures/some_file')

        args = {'url': 'some url', 'file': path, 'name': 'name'}

        self.client.shorturl.create_short_url(**args)

        self.assertEqual(open(args.get('file'), 'rb').read(), self.request_fake.files.get('file').read())

    @api_response_fixture('short_url')
    def test_get_short_url(self):
        id = '1'

        r = self.client.shorturl.get_short_url(id=id)

        expected_result = create_short_url_link()

        self.assertEqual(expected_result, r)
        self.assertTrue(self.request_fake.url.endswith('short_url/links/%s' % id))

    @api_response_fixture('short_url')
    def test_update_short_url(self):
        id = '1'

        args = {'id': id, 'url': 'some url', 'name': 'name'}

        r = self.client.shorturl.update_short_url(**args)

        expected_result = create_short_url_link()

        self.assertEqual(expected_result, r)
        self.assertEqual('PUT', self.request_fake.http_method)
        self.assertTrue(self.request_fake.url.endswith('short_url/links/%s' % id))

    def test_remove_short_url(self):
        id = '1'

        self.client.shorturl.remove_short_url(id=id)

        self.assertEqual('DELETE', self.request_fake.http_method)
        self.assertTrue(self.request_fake.url.endswith('short_url/links/%s' % id))


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ShortUrlApiTest))
    return suite
