
import os

from smsapi.client import SmsApiPlClient


access_token = os.getenv('SMSAPI_ACCESS_TOKEN')


client = SmsApiPlClient(access_token=access_token)


def add_sender_name():
    r = client.sender.add(name='DarthVader')

    print(r.name, r.status, r.default)


def check_sender_name():
    r = client.sender.check(name='DarthVader')

    print(r.name, r.status, r.default)


def remove_sender_name():
    r = client.sender.remove(name='DarthVader')

    print(r.count)


def make_sender_name_default():
    r = client.sender.default(name='DarthVader')

    print(r.name, r.status, r.default)


def list_sender_names():
    r = client.sender.list()

    for sn in r:
        print(sn.name, sn.status, sn.default)