from smsapi.client import SmsAPI

api = SmsAPI()

api.set_username('client_username')
api.set_password('client_password')

api.service('phonebook').action('contact_add')

api.set_number('some_phone_number')
api.set_first_name('first_name')
api.set_last_name('last_name')
api.set_email('some@mail.com')
api.set_birthday('01-01-1970')
api.set_city('city')
api.set_groups(['some_existing_group_name'])

result = api.execute()

for r in result:
    print(r.id, r.points, r.status)