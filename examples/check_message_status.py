from smsapi.client import SmsAPI

api = SmsAPI()

api.set_username('client_username')
api.set_password('client_password')

api.service('sms').action('get')
api.set_id('sms_id')

response = api.execute()

print(response.status, response.points, response.number)