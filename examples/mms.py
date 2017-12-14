
import os

from smsapi.client import SmsApiPlClient


access_token = os.getenv('SMSAPI_ACCESS_TOKEN')


client = SmsApiPlClient(access_token=access_token)


def basic_send_mms():
    client.mms.send(to='some-number', subject='some-subject', smil='SMIL formatted message')


def send_mms_to_contacts_group():
    client.mms.send_to_group(group='some-group', subject='some-subject', smil='SMIL formatted message')


def remove_scheduled_mms():
    client.mms.remove_scheduled(id='scheduled-mms-id')
