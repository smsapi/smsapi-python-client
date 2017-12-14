
import os

from smsapi.client import SmsApiPlClient


access_token = os.getenv('SMSAPI_ACCESS_TOKEN')


client = SmsApiPlClient(access_token=access_token)


def basic_send_vms():
    client.vms.send(to='some-number', tts='some text message')


def send_vms_from_file():
    client.vms.send_flash(to='some-number', file='/path/to/vms/file')


def send_vms_to_contacts_group():
    client.vms.send_to_group(group='some-group', tts='some text message')


def send_vms_using_another_lector():
    client.vms.send(to='some-number', tts='some text message', tts_lector='maja')


def remove_scheduled_vms():
    client.vms.remove_scheduled(id='scheduled-vms-id')
