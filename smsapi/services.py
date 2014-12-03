# -*- coding: utf-8 -*-

from .actions import sms, mms, vms, sender, client, phonebook, hlr

class Service(object):
    
    def __init__(self, proxy):
        self.proxy = proxy


class ServiceSms(Service):

    service_uri= 'sms.do'

    def __init__(self, proxy):
        super(ServiceSms, self).__init__(proxy)

    def action_send(self):
        return sms.SendAction(self.proxy, self.service_uri)
    
    def action_get(self):
        return sms.GetAction(self.proxy, self.service_uri)

    def action_delete(self):
        return sms.DeleteAction(self.proxy, self.service_uri)


class ServiceMms(Service):

    service_uri = 'mms.do'

    def __init__(self, proxy):
        super(ServiceMms, self).__init__(proxy)

    def action_send(self):
        return mms.SendAction(self.proxy, self.service_uri)
    
    def action_get(self):
        return mms.GetAction(self.proxy, self.service_uri)

    def action_delete(self):
        return mms.DeleteAction(self.proxy, self.service_uri)


class ServiceVms(Service):

    service_uri = 'vms.do'    
    
    def __init__(self, proxy):
        super(ServiceVms, self).__init__(proxy)

    def action_send(self):
        return vms.SendAction(self.proxy, self.service_uri)

    def action_get(self):
        return vms.GetAction(self.proxy, self.service_uri)

    def action_delete(self):
        return vms.DeleteAction(self.proxy, self.service_uri)


class ServiceClient(Service):
    
    service_uri = 'user.do'    
    
    def __init__(self, proxy):
        super(ServiceClient, self).__init__(proxy)
        
    def action_add_subuser(self):
        return client.AddSubuserAction(self.proxy, self.service_uri)

    def action_edit_subuser(self):
        return client.EditSubuserAction(self.proxy, self.service_uri)    
    
    def action_subuser_details(self):
        return client.SubuserDetailsAction(self.proxy, self.service_uri)
    
    def action_account_details(self):
        return client.AccountDetailsAction(self.proxy, self.service_uri)
    
    def action_list_subuser(self):
        return client.ListAction(self.proxy, self.service_uri)


class ServiceSender(Service):
    
    service_uri = 'sender.do'
    
    def __init__(self, proxy):
        super(ServiceSender, self).__init__(proxy)
        
    def action_add(self):
        return sender.AddAction(self.proxy, self.service_uri)

    def action_status(self):
        return sender.StatusAction(self.proxy, self.service_uri)
    
    def action_delete(self):
        return sender.DeleteAction(self.proxy, self.service_uri)
    
    def action_list(self):
        return sender.ListAction(self.proxy, self.service_uri)
    
    def action_default(self):
        return sender.SetDefaultAction(self.proxy, self.service_uri)    


class ServicePhonebook(Service):
    
    service_uri = 'phonebook.do'

    def __init__(self, proxy):
        super(ServicePhonebook, self).__init__(proxy)
        
    def action_group_details(self):
        return phonebook.GroupDetailsAction(self.proxy, self.service_uri)

    def action_group_list(self):
        return phonebook.GroupListAction(self.proxy, self.service_uri)

    def action_group_add(self):
        return phonebook.GroupAddAction(self.proxy, self.service_uri)
    
    def action_group_edit(self):
        return phonebook.GroupEditAction(self.proxy, self.service_uri)    

    def action_group_delete(self):
        return phonebook.GroupDeleteAction(self.proxy, self.service_uri)
    
    def action_contact_details(self):
        return phonebook.ContactDetailsAction(self.proxy, self.service_uri)
    
    def action_contact_list(self):
        return phonebook.ContactListAction(self.proxy, self.service_uri)
    
    def action_contact_add(self):
        return phonebook.ContactAddAction(self.proxy, self.service_uri)
    
    def action_contact_edit(self):
        return phonebook.ContactEditAction(self.proxy, self.service_uri)
    
    def action_contact_delete(self):
        return phonebook.ContactDeleteAction(self.proxy, self.service_uri)    


class ServiceHlr(Service):

    service_uri = 'hlr.do'

    def __init__(self, proxy):
        super(ServiceHlr, self).__init__(proxy)

    def action_check(self):
        return hlr.CheckAction(self.proxy, self.service_uri)
