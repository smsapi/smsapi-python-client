from smsapi.client import SmsAPI

api = SmsAPI()

api.set_username('client_username')
api.set_password('client_password')

api.service('sms').action('send')

api.set_content('sample message')
api.set_to('some_phone_number')

result = api.execute()

for r in result:
    print(r.id, r.points, r.status)