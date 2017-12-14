
import os

from smsapi.client import SmsApiPlClient


access_token = os.getenv('SMSAPI_ACCESS_TOKEN')


client = SmsApiPlClient(access_token=access_token)


def create_short_url():
    r = client.shorturl.create_short_url(url='http://smsapi.pl/', name='smsapi')

    print(
        r.id, r.name, r.url, r.short_url, r.filename, r.type,
        r.expire, r.hits, r.hits_unique, r.description)


def create_short_url_with_file():
    r = client.shorturl.create_short_url(url='http://smsapi.com', file='path to file', name='smsapi')

    print(r.id, r.name, r.url)


def get_clicks_statistics():
    r = client.shorturl.get_clicks(date_from='2017-12-01', date_to='2017-12-10')

    print(
        r.idzdo_id, r.phone_number, r.date_hit, r.name, r.short_url,
        r.os, r.browser, r.device, r.suffix, r.message)


def get_clicks_statistics_for_link():
    response = client.shorturl.get_clicks(date_from='2017-12-01', date_to='2017-12-10', links=['1'])

    for r in response:
        print(
            r.idzdo_id, r.phone_number, r.date_hit, r.name, r.short_url,
            r.os, r.browser, r.device, r.suffix, r.message)
