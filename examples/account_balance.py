from smsapi.client import SmsAPI

api = SmsAPI()

api.set_username('client_username')
api.set_password('client_password')

api.service('client').action('account_details')

response = api.execute()

print(response.points)