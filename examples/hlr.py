
import os

from smsapi.client import SmsApiPlClient


access_token = os.getenv('SMSAPI_ACCESS_TOKEN')


client = SmsApiPlClient(access_token=access_token)


def check_number():
    r = client.hlr.check_number(number='some-number')

    print(r.status, r.number, r.id, r.price)