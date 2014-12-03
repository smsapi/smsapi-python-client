# -*- coding: utf-8 -*-

from hashlib import md5
from .action import ApiAction
from smsapi.responses import ApiResponse

class AddSubuserAction(ApiAction):
    
    def set_username(self, username):
        self._data['add_user'] = username
        
    def set_password(self, password):
        self._data['pass'] = md5(password.encode('utf-8')).hexdigest()
        
    def set_api_password(self, api_password):
        self._data['pass_api'] = md5(api_password.encode('utf-8')).hexdigest()
        
    def set_limit(self, points):
        self._data['limit'] = points
        
    def set_month_limit(self, points):
        self._data['month_limit'] = points
        
    def set_share_sendernames(self, share=True):
        if share:
            self._data['senders'] = 1
        elif share in self._data:
            del self._data['share']

    def set_share_phonebok(self, share=True):
        if share:
            self._data['phonebook'] = 1
        elif share in self._data:
            del self._data['phonebook']
                                        
    def set_active(self, active=True):
        if active:
            self._data['active'] = 1
        elif active in self._data:
            del self._data['active']

    def set_description(self, description):
        self._data['senders'] = description

    def execute(self):
        result = self.proxy.execute(self.uri, self._data)
        return ApiResponse(result)
            

class EditSubuserAction(AddSubuserAction):
    
    def set_username(self, username):
        self._data['set_user'] = username

    def execute(self):
        result = self.proxy.execute(self.uri, self._data)
        return ApiResponse(result)

class SubuserDetailsAction(ApiAction):

    def set_user(self, username):
        self._data['get_user'] = username
        
    def execute(self):
        result = self.proxy.execute(self.uri, self._data)
        return ApiResponse(result)        


class AccountDetailsAction(ApiAction):
        
    def execute(self):
        self._data.update({
           'credits': 1,
           'details': 1
        })
                
        result = self.proxy.execute(self.uri, self._data)
        return ApiResponse(result)        


class ListAction(ApiAction):

    def execute(self):
        self._data['list'] = 1
        
        result = self.proxy.execute(self.uri, self._data)
        return ApiResponse(result)
    
    
