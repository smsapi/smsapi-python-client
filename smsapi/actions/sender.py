# -*- coding: utf-8 -*-

from .action import ApiAction
from smsapi.responses import ApiResponse

class AddAction(ApiAction):
    
    def set_name(self, name):
        self._data['add'] = name
        
    def execute(self):
        result = self.proxy.execute(self.uri, self._data)
        return ApiResponse(result)        

class StatusAction(ApiAction):
    
    def set_name(self, name):
        self._data['status'] = name
        
    def execute(self):
        result = self.proxy.execute(self.uri, self._data)
        return ApiResponse(result)
             
class DeleteAction(ApiAction):

    def set_name(self, name):
        self._data['delete'] = name
        
    def execute(self):
        result = self.proxy.execute(self.uri, self._data)
        return ApiResponse(result)     

class ListAction(ApiAction):
        
    def execute(self):
        self._data['list'] = 1
        
        result = self.proxy.execute(self.uri, self._data)
        return ApiResponse(result)     

class SetDefaultAction(ApiAction):

    def set_name(self, name):
        self._data['default'] = name
        
    def execute(self):
        result = self.proxy.execute(self.uri, self._data)
        return ApiResponse(result)
        
