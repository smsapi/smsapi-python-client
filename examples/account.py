import os
from hashlib import md5

from smsapi.client import SmsApiPlClient


access_token = os.getenv('SMSAPI_ACCESS_TOKEN')


client = SmsApiPlClient(access_token=access_token)


def get_account_balance():
    r = client.account.balance()

    print(r.points, r.pro_count, r.eco_count, r.mms_count, r.vms_gsm_count, r.vms_land_count)


def create_user():
    r = client.account.create_user(
        name='some_user',
        password='d03444aa8b114fa3d1b8a3a2593c848a',
        api_password='67e8a30195188587421ba43fb8d9f20f',
        limit=1000,
        month_limit=100,
        senders=0,
        phonebook=0,
        active=1,
        info='some description',
        without_prefix=1)

    print(r.username, r.limit, r.month_limit, r.senders, r.phonebook, r.active, r.info)


def get_user():
    r = client.account.user(name='some_user', without_prefix=1)

    print(r.username, r.limit, r.month_limit, r.senders, r.phonebook, r.active, r.info)


def update_user():
    new_password = md5("new-password".encode("utf-8")).hexdigest()

    r = client.account.update_user(name='some_user', password=new_password, without_prefix=1)

    print(r.username, r.limit, r.month_limit, r.senders, r.phonebook, r.active, r.info)


def list_users():
    r = client.account.list_users()

    for u in r:
        print(u.username, u.limit, u.month_limit, u.senders, u.phonebook, u.active, u.info)
