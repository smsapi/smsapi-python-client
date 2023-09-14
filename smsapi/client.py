from requests.auth import HTTPBasicAuth

from smsapi.account.api import Account
from smsapi.auth import BearerAuth
from smsapi.blacklist.api import Blacklist
from smsapi.contacts.api import Contacts
from smsapi.exception import ClientException
from smsapi.hrl.api import Hlr
from smsapi.mfa.api import Mfa
from smsapi.mms.api import Mms
from smsapi.sender.api import Sender
from smsapi.short_url.api import ShortUrl
from smsapi.sms.api import Sms
from smsapi.vms.api import Vms


class Client(object):

    def __init__(self, domain, access_token=None, **kwargs):
        super(Client, self).__init__()

        self.domain = domain

        username = kwargs.get('username')
        password = kwargs.get('password')

        if not any((access_token, username, password)):
            raise ClientException('Credentials are required.')

        self.auth = BearerAuth(access_token) if access_token else HTTPBasicAuth(username, password)

        self.sms = Sms(self)
        self.mfa = Mfa(self)
        self.account = Account(self)
        self.contacts = Contacts(self)
        self.sender = Sender(self)
        self.shorturl = ShortUrl(self)
        self.hlr = Hlr(self)
        self.blacklist = Blacklist(self)


class SmsApiPlClient(Client):

    def __init__(self, **kwargs):
        super(SmsApiPlClient, self).__init__('https://api.smsapi.pl/', **kwargs)

        self.mms = Mms(self)
        self.vms = Vms(self)


class SmsApiComClient(Client):

    def __init__(self, **kwargs):
        super(SmsApiComClient, self).__init__('https://api.smsapi.com/', **kwargs)


class SmsApiBgClient(Client):

    def __init__(self, **kwargs):
        super(SmsApiBgClient, self).__init__('https://api.smsapi.bg/', **kwargs)
        
        
class SmsApiSwedenClient(Client):

    def __init__(self, **kwargs):
        super(SmsApiSwedenClient, self).__init__('https://api.smsapi.se/', **kwargs)        
