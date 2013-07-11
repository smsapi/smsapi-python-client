# -*- coding: utf-8 -*-

class ApiSendAction(object):
    
    def set_content(self, message): 
        raise NotImplementedError    
    
    def set_to(self, recipients):
        if 'group' in self._data:
            del self._data['group']
        if isinstance(recipients, list):
            self._data['to'] = ','.join(recipients)
        else:
            self._data['to'] = recipients
            
        return self
            
    def set_group(self, group):
        try:
            del self._data['to']
        except:
            pass
            
        self._data['group'] = group
        
        return self

    def set_date(self, timestamp):
        self._data['date'] = str(int(timestamp))

        return self
        
    def set_idx(self, idx):
        def check_string(string):
            return (len(string) <= 36 and string.isalnum())
                
        if isinstance(idx, (list, tuple)):
            self._data = "|".join([i for i in idx if check_string(i)])
        elif check_string(idx):
            self._data['idx'] = idx
            
        return self
            
    def set_check_idx(self, check_idx=True):
        if not check_idx:
            try:
                del self._data['check_idx']
            except KeyError: 
                pass            
        else:
            self._data['check_idx'] = 1
            
        return self
        
    def send_test(self, test=True):
        if not test:
            try:
                del self._data['test']
            except KeyError:
                pass
        else:
            self._data['test'] = 1
            
        return self        

    def set_id(self, message_id):
        self._data['sch_del'] = int(message_id)
        return self        
        
    def clear(self):
        self._data.clear()
        