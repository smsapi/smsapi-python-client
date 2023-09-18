import os

from smsapi.client import SmsApiPlClient


access_token = os.getenv('SMSAPI_ACCESS_TOKEN')

client = SmsApiPlClient(access_token=access_token)

client.mfa.send_mfa(phone_number='some-number', content='Your code: [%code%]', fast=0)

client.mfa.verify_mfa(phone_number="", code="")
