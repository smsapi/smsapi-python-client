# -*- coding: utf-8 -*-

from .action import ApiAction
from .message import ApiSendAction

CHARSETS= (
    'iso-8859-1'
    'iso-8859-2'
    'iso-8859-3'
    'iso-8859-4'
    'iso-8859-5'
    'iso-8859-7'
    'windows-1250'
    'windows-1251'
    'utf-8'
)

class SendAction(ApiSendAction, ApiAction):
    
    def __init__(self, proxy, uri):
        super(SendAction, self).__init__(proxy, uri)
    
        self.wap_push = False

    def set_from(self, sender_name):
        self._data['from'] = sender_name
        return self        

    def set_content(self, message):
        if self.wap_push:
            msg = message.encode('hex')
        else:
            msg = message.encode('utf-8')

        self._data['message'] = msg
        
        return self
        
    def set_encoding(self, encoding):
        if encoding not in CHARSETS:
            raise ValueError('Encoding not defined')
        self._data['encoding'] = encoding
        
        return self        
        
    def set_details(self, details=True):   
        if not details:
            try: 
                del self._data['details']
            except KeyError:
                pass                 
        else:
            self._data['details'] = 1
                        
        return self
                                                  
    def set_date_validate(self, date_validate=True):   
        if not date_validate:   
            try: 
                del self._data['date_validate']
            except KeyError:
                pass            
        else:
            self._data['date_validate'] = 1
            
        return self
            
    def set_eco(self, eco=True):   
        if not eco:
            try: 
                del self._data['eco']
            except KeyError:
                pass
        else:
            self._data['eco'] = 1
            
        return self
        
    def set_nounicode(self, nounicode=True):   
        if not nounicode:   
            try:
                del self._data['nounicode']
            except KeyError:
                pass            
        else:
            self._data['nounicode'] = 1
            
        return self            
        
    def set_normalize(self, normalize=True):
        if not normalize:
            try:
                del self._data['normalize']
            except KeyError:
                pass
        else:
            self._data['normalize'] = 1
            
        return self
        
    def set_fast(self, fast=True):   
        if not fast:
            try:
                del self._data['fast']
            except KeyError:
                pass
        else:
            self._data['fast'] = 1
            
        return self
        
    def set_partner(self, partner):   
        self._data['partner_id'] = partner
        return self        
        
    def set_max_parts(self, max_parts):   
        self._data['max_parts'] = int(max_parts)
        return self        
        
    def set_expiration_date(self, expiration_date):
        self._data['expiration_date'] = int(expiration_date)
        return self        
        
    def set_params(self, *args):
            
        index = 1
        
        params = None
        
        for arg in args:
            if isinstance(arg, (tuple, list)):
                params = '|'.join(arg)
                
            self._data['param' + str(index)] = params or str(arg)                
                
            index += 1
            
        return self
    
    def send_flash(self):
        self._data['flash'] = 1
        return self


class GetAction(ApiAction):
    
    def set_id(self, message_id):
        self._data['status'] = message_id
        return self
    

class DeleteAction(ApiAction):
    
    def set_id(self, message_id):
        self._data['sch_del'] = message_id
        return self
    
