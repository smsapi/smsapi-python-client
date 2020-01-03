import os

from smsapi.client import SmsApiPlClient


access_token = os.getenv('SMSAPI_ACCESS_TOKEN')


client = SmsApiPlClient(access_token=access_token)


def add_phone_number_to_blacklist():
    r = client.blacklist.add_phone_number(phone_number="111222333", expire_at="2099-01-01T01:01:01Z")

    print(r.id, r.phone_number, r.expire_at, r.created_at)


def get_phone_number_from_blacklist():
    r = client.blacklist.add_phone_number(id="1")

    print(r.id, r.phone_number, r.expire_at, r.created_at)


def list_phone_numbers_from_blacklist():
    r = client.blacklist.list_phone_numbers()

    for n in r:
        print(n.id, n.phone_number, n.expire_at, n.created_at)


def delete_phone_number_from_blacklist():
    client.blacklist.delete_phone_number(id="1")


def delete_all_phone_numbers_from_blacklist():
    client.blacklist.delete_all_phone_numbers()
