python-client
=============

Klient napisany w języku Python, pozwalający na wysyłanie wiadomości SMS, MMS, VMS oraz zarządzanie kontem w serwisie SMSAPI.pl

EXAMPLES:

from smsapi.client import SmsAPI
from smsapi.responses import ApiError


api = SmsAPI()

api.set_username('YOUR USERNAME')
api.set_password('YOUR PASSWORD')

#sending SMS
try:
    api.service('sms').action('send')

    api.set_content('Hello [%1%] [%2%]')
    api.set_params('name', 'last name')
    api.set_to('60xxxxxxx')

    result = api.execute()

    for r in result:
        print r.id, r.points, r.status

except ApiError, e:
    print '%s - %s' % (e.code, e.message)