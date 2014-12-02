# -*- coding: utf-8 -*-

import os
from .action import ApiAction
from .message import ApiSendAction
from smsapi.responses import ApiResponse

LECTORS = (
   'agnieszka', 
   'ewa', 
   'jacek', 
   'jan',
   'maja'
)

class SendAction(ApiSendAction, ApiAction):

    def set_content(self, content):
        if os.path.isfile(content):
            if 'tts' in self._data:
                del self._data['tts']
            self.proxy.add_file(content)
        else:
            self._data['tts'] = content
                    
        return self
        
    def set_try(self, trials):
        if trials in range(1, 6):
            self._data['try'] = trials
        else:
            raise ValueError("Value is out of range")
        
        return self        
    
    def set_interval(self, interval):
        if 1800 <= interval <= 7200:
            self._data['interval'] = interval
        else:
            raise ValueError("Value is out of range")
        
        return self        
        
    def skip_gsm(self, skip_gsm=True):
        if skip_gsm:
            self._data['skip_gsm'] = True
        else:
            if 'skip_gsm' in self._data: 
                del self._data['skip_gsm']
                
        return self                
    
    def lector(self, lector):
        if lector.lower() in LECTORS:
            self._data['tts_lector'] = lector
        else:
            raise ValueError("lector is not defined")
        
        return self        
            
    def set_notify_url(self, notify_url):
        self._data['notify_url'] = notify_url
            
        return self

    def execute(self):
        api_response = self.proxy.execute(self.uri, self._data)
        return ApiResponse(api_response)


class GetAction(ApiAction):
    
    def set_id(self, message_id):
        self._data['status'] = message_id


class DeleteAction(ApiAction):

    def set_id(self, message_id):
        self._data['sch_del'] = message_id
    
