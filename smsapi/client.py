# -*- coding: utf-8 -*-

import hashlib
from . import services
from .proxy import ApiHttpProxy


class SmsAPI(object):
    
    def __init__(self, username=None, password=None, **kwargs):
        super(SmsAPI, self).__init__()

        self.api_url = 'https://api.smsapi.pl/'

        self.response_format = 'json'

        self.username = username
        
        self.password = password
        
        self.auth_token = kwargs.get('auth_token')

        self._service = None

        self._action = None
        
        self._reset = True

        self._proxy = ApiHttpProxy(self.api_url)
    
    def service(self, name):
        service_name = 'Service%s' % name.title()

        try:
            self._service = getattr(services, service_name)(self._proxy)
        except AttributeError:
            raise AttributeError('Unrecognized service name %s' % service_name)
        
        return self
    
    def action(self, action=None, data=None):
        if not self._service:
            raise RuntimeError('Choose service first.')

        action_name = 'action_%s' % action.lower()

        if hasattr(self._service, action_name):
            self._action = getattr(self._service, action_name)()

            if data:
                self._action.data(data)
        else:
            raise ValueError('Action not exist.')
        
        return self

    def set_hostname(self, hostname):
        self._proxy.set_hostname(hostname)
        return self
    
    def set_username(self, username):
        self.username = username
        return self

    def set_password(self, password, encode=True):
        if encode:
            self.password = self.hash(password)
        else:
            self.password = password

        return self

    def set_proxy(self, proxy):
        if not isinstance(proxy, proxy.ApiProxy):
            raise TypeError('Invalid type.')
        self._proxy = proxy

        return self

    def hash(self, string):
        string = string.encode('utf-8')
        return hashlib.md5(string).hexdigest()

    def reset(self, reset=True):
        self._reset = reset
        return self

    def execute(self):
        if self.auth_token:
            self._proxy.auth = self.auth_token
        else:
            self._proxy.auth = (self.username, self.password)

        self._proxy.data.update({
            'format': self.response_format
        })
        
        result = self._action.execute()

        if self._reset:
            self._action.clear()
            self._proxy.data.clear()

        self._reset = True

        return result

    def __getattr__(self, name):
        if self._action and hasattr(self._action, name):
            return getattr(self._action, name)
        else:
            raise AttributeError(name)

