python-client
=============

Klient napisany w języku Python, pozwalający na wysyłanie wiadomości SMS, MMS, VMS oraz zarządzanie kontem w serwisie SMSAPI.pl

EXAMPLES:
```python
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
		api.set_from('Info') #Pole nadawcy lub typ wiadomość 'ECO', '2Way'
    
        result = api.execute()
    
        for r in result:
            print r.id, r.points, r.status
    
    except ApiError, e:
        print '%s - %s' % (e.code, e.message)
```

## LICENSE
[Apache 2.0 License](https://github.com/smsapi/smsapi-python-client/blob/master/LICENSE)