
import os

from smsapi.client import SmsApiPlClient


access_token = os.getenv('SMSAPI_ACCESS_TOKEN')


client = SmsApiPlClient(access_token=access_token)


def send_push():
    r = client.push.send(app_id='app id', alert='push notification text')

    print(r.id, r.date_created, r.scheduled_date, r.summary.points, r.summary.recipients_count,
          r.summary.error_code, r.app.name, r.payload.alert)