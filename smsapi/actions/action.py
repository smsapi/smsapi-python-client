# -*- coding: utf-8 -*-

from smsapi.responses import ApiResponse

class ApiAction(object):
    
    def __init__(self, proxy, uri):        
        
        self.proxy = proxy

        self.uri = uri

        self._data = {}

    def data(self, data):
        if isinstance(data, dict):
            for key, value in data.items():
                func = 'set_%s' % key
                if hasattr(self, func):
                    getattr(self, func)(value)
    
    def clear(self):
        self._data.clear()
    
    def execute(self):
        api_response = self.proxy.execute(self.uri, self._data)
        return ApiResponse(api_response)