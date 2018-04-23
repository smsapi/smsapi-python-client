
import os

from smsapi.client import SmsApiPlClient


access_token = os.getenv('SMSAPI_ACCESS_TOKEN')


client = SmsApiPlClient(access_token=access_token)


def basic_send_sms():
    client.sms.send(to='some-number', message='some text message')


def send_flash_sms():
    client.sms.send_flash(to='some-number', message='some text message')


def send_sms_fast():
    client.sms.send_fast(to='some-number', message='some text message')


def send_sms_to_contacts_group():
    client.sms.send_to_group(group='some-group', message='some text message')


def remove_scheduled_sms():
    client.sms.remove_scheduled(id='scheduled-sms-id')


def send_parametrized_sms_to_many_numbers():
    client.sms.send(to=['number1', 'number2'], message='some text [%1%]', param1=['1', '2'])


def send_sms_with_custom_sender_name():
    client.sms.send(to='some-number', message='some text message', from_='your-custom-sender-name')