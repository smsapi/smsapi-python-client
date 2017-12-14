
import os

from smsapi.client import SmsApiPlClient


access_token = os.getenv('SMSAPI_ACCESS_TOKEN')


client = SmsApiPlClient(access_token=access_token)


def get_account_balance():
    r = client.account.balance()

    print(r.points, r.pro_count, r.eco_count, r.mms_count, r.vms_gsm_count, r.vms_land_count)


def create_user():
    r = client.account.create_user(
        name='some username',
        password='password',
        api_password='api password',
        limit=1000,
        month_limit=100,
        senders=False,
        phonebook=False,
        active=True,
        info='some description',
        without_prefix=True)

    print(r.username, r.limit, r.month_limit, r.senders, r.phonebook, r.active, r.info)


def get_user():
    r = client.account.create_user(name='some username')

    print(r.username, r.limit, r.month_limit, r.senders, r.phonebook, r.active, r.info)


def update_user():
    r = client.account.create_user(name='some username', password='password')

    print(r.username, r.limit, r.month_limit, r.senders, r.phonebook, r.active, r.info)


def list_users():
    r = client.account.list_users()

    for u in r:
        print(r.username, r.limit, r.month_limit, r.senders, r.phonebook, r.active, r.info)
