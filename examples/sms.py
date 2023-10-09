import os

from smsapi.client import SmsApiPlClient


access_token = os.getenv('SMSAPI_ACCESS_TOKEN')

client = SmsApiPlClient(access_token=access_token)

# send single sms
results = client.sms.send(to='some-number', message='some text message')

for result in results:
    print(result.id, result.points, result.error)

# send sms to many numbers
results = client.sms.send(to=['123-123-123', '321-321-321'], message='some text message')

for result in results:
    print(result.id, result.points, result.error)

# send sms to contacts group
client.sms.send_to_group(group='some-group', message='some text message')

# send flash sms
client.sms.send_flash(to='some-number', message='some text message')

# send sms fast
client.sms.send_fast(to='some-number', message='some text message')

# remove_scheduled_sms
client.sms.remove_scheduled(id='scheduled-sms-id')

# send parametrized sms to many numbers
client.sms.send(to=['number1', 'number2'], message='some text [%1%]', param1=['1', '2'])

# send_sms_with_custom_sender_name
client.sms.send(to='some-number', message='some text message', from_='your-custom-sender-name')
