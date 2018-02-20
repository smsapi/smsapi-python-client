# -*- coding: utf-8 -*-

from smsapi.models import Model
from smsapi.utils import convert_iso8601_str_to_datetime, convert_date_str_to_date


class ContactModel(Model):

    def __init__(self, **kwargs):
        super(ContactModel, self).__init__()

        self.id = kwargs.get('id')
        self.idx = kwargs.get('idx')
        self.first_name = kwargs.get('first_name')
        self.last_name = kwargs.get('last_name')
        self.phone_number = kwargs.get('phone_number')
        self.gender = kwargs.get('gender')
        self.city = kwargs.get('city')
        self.email = kwargs.get('email')
        self.source = kwargs.get('source')
        self.description = kwargs.get('description')
        self.birthday_date = kwargs.get('birthday_date')
        self.date_created = kwargs.get('date_created')
        self.date_updated = kwargs.get('date_updated')

        if self.birthday_date:
            self.birthday_date = convert_date_str_to_date(self.birthday_date)

        if self.date_created:
            self.date_created = convert_iso8601_str_to_datetime(self.date_created)

        if self.date_updated:
            self.date_updated = convert_iso8601_str_to_datetime(self.date_updated)


class GroupModel(Model):

    def __init__(self, **kwargs):
        super(GroupModel, self).__init__()

        self.id = kwargs.get('id')
        self.name = kwargs.get('name')
        self.contacts_count = kwargs.get('contacts_count')
        self.date_created = kwargs.get('date_created')
        self.date_updated = kwargs.get('date_updated')
        self.description = kwargs.get('description')
        self.created_by = kwargs.get('created_by')
        self.idx = kwargs.get('idx')
        self.permissions = kwargs.get('permissions')

    @classmethod
    def from_dict(cls, data, **kwargs):
        model = super(GroupModel, cls).from_dict(data)

        permissions = data.get('permissions', [])
        model.permissions = [GroupPermissionModel.from_dict(p) for p in permissions]

        return model


class CustomFieldModel(Model):

    def __init__(self, **kwargs):
        super(CustomFieldModel, self).__init__()

        self.id = kwargs.get('id')
        self.name = kwargs.get('name')
        self.type = kwargs.get('type')


class GroupPermissionModel(Model):

    def __init__(self, **kwargs):
        super(GroupPermissionModel, self).__init__()

        self.username = kwargs.get('username')
        self.group_id = kwargs.get('group_id')
        self.write = kwargs.get('write')
        self.read = kwargs.get('read')
        self.send = kwargs.get('send')
