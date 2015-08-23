# -*- coding: utf-8 -*-

from .action import ApiAction
from smsapi.responses import ApiResponse
from smsapi.decorators import deprecated

GENDERS = ('unknown', 'female', 'male')


class GroupDetailsAction(ApiAction):
    
    def set_name(self, group_name):
        self._data['get_group'] = group_name

    @deprecated()
    def execute(self):
        result = self.proxy.execute(self.uri, self._data)
        return ApiResponse(result)


class GroupListAction(ApiAction):

    @deprecated()
    def execute(self):
        self._data['list_groups'] = 1
        result = self.proxy.execute(self.uri, self._data)
        return ApiResponse(result)
    
    
class GroupAddAction(ApiAction):
    
    def set_name(self, group_name):
        self._data['add_group'] = group_name

    def set_info(self, info):
        self._data['info'] = info

    @deprecated()
    def execute(self):
        result = self.proxy.execute(self.uri, self._data)
        return ApiResponse(result)    


class GroupEditAction(ApiAction):
    
    def set_name(self, group_name):
        self._data['edit_group'] = group_name
        
    def set_new_name(self, group_name):
        self._data['name'] = group_name

    def set_info(self, info):
        self._data['info'] = info

    @deprecated()
    def execute(self):
        result = self.proxy.execute(self.uri, self._data)
        return ApiResponse(result)


class GroupDeleteAction(ApiAction):
    
    def set_name(self, group):
        self._data['delete_group'] = group

    def set_remove_contacts(self, remove=True):
        if remove:
            self._data['remove_contacts'] = 1
        elif 'remove_contacts' in self._data:
            del self._data['remove_contacts']

    @deprecated()
    def execute(self):
        result = self.proxy.execute(self.uri, self._data)
        return ApiResponse(result)   


class ContactDetailsAction(ApiAction):
    
    def set_number(self, number):
        self._data['get_contact'] = number

    @deprecated()
    def execute(self):
        result = self.proxy.execute(self.uri, self._data)
        return ApiResponse(result)
    
    
class ContactListAction(ApiAction):
    
    def __init__(self, proxy, uri):
        super(ContactListAction, self).__init__(proxy, uri)
    
        self.ordered_fields = ('first_name', 'last_name')

        self.order_directions = ('asc', 'desc')
    
    def set_groups(self, groups):
        if isinstance(groups, (list, tuple)):
            groups = ','.join(groups)
        
        self._data['groups'] = groups

    def set_text_search(self, text):
        self._data['text_search'] = text
        
    def set_gender(self, gender):
        if gender in GENDERS:
            self._data['gender'] = gender
        else:
            raise ValueError("value must be one of: %s" % 
                             ', '.join('%s - %s' % (k, v) for k, v in enumerate(GENDERS)))

    def set_number(self, number):
        self._data['get_contact'] = number
        
    def set_order(self, order):
        if order in self.ordered_fields:
            self._data['order_by'] = order
        else:
            raise ValueError("Value must be one of: %s" % ", ".join(self.ordered_fields))

    def set_order_direction(self, direction):
        if direction in self.order_directions:
            self._data['order_dir'] = direction
        else:
            raise ValueError("Value must be one of: %s" % ", ".join(self.order_directions))
        
    def set_limit(self, limit):
        self._data['limit'] = limit
        
    def set_offset(self, offset):
        self._data['offset'] = offset

    @deprecated()
    def execute(self):
        self._data['list_contacts'] = 1
        
        result = self.proxy.execute(self.uri, self._data)
        return ApiResponse(result)  
    
    
class ContactAddAction(ApiAction):
    
    def set_number(self, number):
        self._data['add_contact'] = number

    def set_first_name(self, first_name):
        self._data['first_name'] = first_name
        
    def set_last_name(self, last_name):
        self._data['last_name'] = last_name
        
    def set_info(self, info):
        self._data['info'] = info
        
    def set_gender(self, gender):
        if gender in GENDERS:
            self._data['gender'] = gender
        else:
            raise ValueError("value must be one of: %s" % 
                             ', '.join('%s - %s' % (k, v) for k, v in enumerate(GENDERS)))
            
    def set_email(self, email):
        self._data['email'] = email
        
    def set_birthday(self, birthday):
        self._data['birthday'] = birthday
        
    def set_city(self, city):
        self._data['city'] = city

    def set_groups(self, groups):
        if isinstance(groups, (list, tuple)):
            groups = ','.join(groups)
        
        self._data['groups'] = groups

    @deprecated()
    def execute(self):
        return super(ContactAddAction, self).execute()


class ContactEditAction(ContactAddAction):
    
    def set_number(self, number):
        self._data['edit_contact'] = number

    @deprecated()
    def execute(self):
        return super(ContactEditAction, self).execute()


class ContactDeleteAction(ApiAction):
    
    def set_number(self, number):
        self._data['delete_contact'] = number

    @deprecated()
    def execute(self):
        return super(ContactDeleteAction, self).execute()
