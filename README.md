smsapi-python
=============

[![Build Status](https://travis-ci.org/smsapi/smsapi-python-client.svg?branch=master)](https://travis-ci.org/smsapi/smsapi-python-client)
[![PyPI](https://img.shields.io/pypi/v/smsapi-client.svg)](https://pypi.python.org/pypi/smsapi-client)

Client for SMSAPI.

## COMPATIBILITY:
Compatible with Python 2.7+, 3.+.

## REQUIREMENTS:
requests

## INSTALLATION:
If You have pip installed:

    sudo pip install smsapi-client

else You can install manually:

    git clone https://github.com/smsapi/smsapi-python-client.git

    cd smsapi-python

    python setup.py install

## Client instance:

If You are smsapi.pl customer You should import
```python
    from smsapi.client import SmsApiPlClient
```

else You need to use client for smsapi.com
```python
    from smsapi.client import SmsApiComClient
```

## Credentials

- Access Token
```python
    client = SmsApiPlClient(access_token='your-access-token')
```

## Examples

- Send SMS
```python
    from smsapi.client import SmsApiPlClient
    
    client = SmsApiPlClient(access_token='your access token')
    
    send_results = client.sms.send(to='phone number', message='text message')

    for result in send_results:
        print(result.id, result.points, result.error)
```

- **You can find more examples in "examples" directory in project files.**


## Error handling

```python
    from smsapi.exception import SmsApiException

    try:
        contact = client.sms.send(to='123123')
    except SmsApiException as e:
        print(e.message, e.code)
```

## LICENSE
[Apache 2.0 License](https://github.com/smsapi/smsapi-python-client/blob/master/LICENSE)
