# -*- coding: utf-8 -*-

from smsapi.contacts.exceptions import ContactsException
from smsapi.models import ModelCollection
from smsapi.contacts.models import ContactModel, GroupModel, GroupPermissionModel, CustomFieldModel

from smsapi.api import Api
from smsapi.endpoint import bind_api_endpoint
from smsapi.models import HeaderDirectResult

list_params = ['offset', 'limit', 'orderBy']

contact_params = ['first_name', 'last_name', 'phone_number', 'email',
                  'gender', 'birthday_date', 'description']


class Contacts(Api):

    list_contacts = bind_api_endpoint(
        method='GET',
        path='contacts',
        mapping=(ContactModel, ModelCollection),
        exception_class=ContactsException,
        accept_parameters=contact_params + list_params + ['q']
    )

    get_contact = bind_api_endpoint(
        method='GET',
        path='contacts/{contact_id}',
        mapping=ContactModel,
        exception_class=ContactsException,
        accept_parameters=['contact_id']
    )

    update_contact = bind_api_endpoint(
        method='PUT',
        path='contacts/{contact_id}',
        mapping=ContactModel,
        exception_class=ContactsException,
        accept_parameters=contact_params + ['contact_id']
    )

    create_contact = bind_api_endpoint(
        method='POST',
        path='contacts',
        mapping=ContactModel,
        exception_class=ContactsException,
        accept_parameters=contact_params
    )

    delete_contact = bind_api_endpoint(
        method='DELETE',
        path='contacts/{contact_id}',
        exception_class=ContactsException,
        accept_parameters=['contact_id']
    )

    list_contact_groups = bind_api_endpoint(
        method='GET',
        path='contacts/{contact_id}/groups',
        mapping=(GroupModel, ModelCollection),
        exception_class=ContactsException,
        accept_parameters=['contact_id', 'group_id']
    )

    bind_contact_to_group = bind_api_endpoint(
        method='POST',
        path='contacts/{contact_id}/groups/{group_id}',
        exception_class=ContactsException,
        accept_parameters=['contact_id', 'group_id']
    )

    list_groups = bind_api_endpoint(
        method='GET',
        path='contacts/groups',
        mapping=(GroupModel, ModelCollection),
        accept_parameters=['group_id', 'name'],
        exception_class=ContactsException,
        force_parameters={'with': 'contacts_count'}
    )

    create_group = bind_api_endpoint(
        method='POST',
        path='contacts/groups',
        mapping=GroupModel,
        exception_class=ContactsException,
        accept_parameters=['name', 'description', 'idx']
    )

    delete_group = bind_api_endpoint(
        method='DELETE',
        path='contacts/groups/{group_id}',
        exception_class=ContactsException,
        accept_parameters=['group_id']
    )

    get_group = bind_api_endpoint(
        method='GET',
        path='contacts/groups/{group_id}',
        mapping=GroupModel,
        accept_parameters=['group_id'],
        exception_class=ContactsException,
        force_parameters={'with': 'contacts_count'}
    )

    update_group = bind_api_endpoint(
        method='PUT',
        path='contacts/groups/{group_id}',
        mapping=GroupModel,
        exception_class=ContactsException,
        accept_parameters=['group_id', 'name', 'description', 'idx']
    )

    list_group_permissions = bind_api_endpoint(
        method='GET',
        path='contacts/groups/{group_id}/permissions',
        mapping=GroupPermissionModel,
        exception_class=ContactsException,
        accept_parameters=['group_id']
    )

    create_group_permission = bind_api_endpoint(
        method='POST',
        path='contacts/groups/{group_id}/permissions',
        mapping=GroupPermissionModel,
        exception_class=ContactsException,
        accept_parameters=['group_id', 'username', 'read', 'write', 'send']
    )

    list_user_group_permissions = bind_api_endpoint(
        method='GET',
        path='contacts/groups/{group_id}/permissions/{username}',
        mapping=(GroupPermissionModel, ModelCollection),
        exception_class=ContactsException,
        accept_parameters=['group_id', 'username']
    )

    delete_user_group_permission = bind_api_endpoint(
        method='DELETE',
        path='contacts/groups/{group_id}/permissions/{username}',
        exception_class=ContactsException,
        accept_parameters=['group_id', 'username']
    )

    update_user_group_permission = bind_api_endpoint(
        method='PUT',
        path='contacts/groups/{group_id}/permissions/{username}',
        mapping=GroupPermissionModel,
        exception_class=ContactsException,
        accept_parameters=['group_id', 'username', 'read', 'write', 'send']
    )

    unpin_contact_from_group = bind_api_endpoint(
        method='DELETE',
        path='contacts/groups/{group_id}/members/{contact_id}',
        exception_class=ContactsException,
        accept_parameters=['group_id', 'contact_id']
    )

    contact_is_in_group = bind_api_endpoint(
        method='GET',
        path='contacts/groups/{group_id}/members/{contact_id}',
        mapping=ContactModel,
        exception_class=ContactsException,
        accept_parameters=['group_id', 'contact_id']
    )

    pin_contact_to_group = bind_api_endpoint(
        method='PUT',
        path='contacts/groups/{group_id}/members/{contact_id}',
        mapping=ContactModel,
        exception_class=ContactsException,
        accept_parameters=['group_id', 'contact_id']
    )

    list_custom_fields = bind_api_endpoint(
        method='GET',
        mapping=(CustomFieldModel, ModelCollection),
        exception_class=ContactsException,
        path='contacts/fields'
    )

    create_custom_field = bind_api_endpoint(
        method='POST',
        path='contacts/fields',
        mapping=CustomFieldModel,
        exception_class=ContactsException,
        accept_parameters=['name', 'type']
    )

    delete_custom_field = bind_api_endpoint(
        method='DELETE',
        path='contacts/fields',
        exception_class=ContactsException,
        accept_parameters=['field_id']
    )

    update_custom_field = bind_api_endpoint(
        method='PUT',
        path='contacts/fields',
        mapping=CustomFieldModel,
        exception_class=ContactsException,
        accept_parameters=['name', 'type']
    )

    unpin_contact_from_group_by_query = bind_api_endpoint(
        method='DELETE',
        path='contacts/groups/{group_id}/members',
        exception_class=ContactsException,
        accept_parameters=contact_params[:-1] + ['group_id', 'q']
    )

    count_contacts_in_trash = bind_api_endpoint(
        method='HEAD',
        path='contacts/trash',
        mapping=HeaderDirectResult('X-Result-Count'),
        exception_class=ContactsException
    )

    restore_contacts_in_trash = bind_api_endpoint(
        method='PUT',
        path='contacts/trash',
        exception_class=ContactsException
    )

    clean_trash = bind_api_endpoint(
        method='DELETE',
        path='contacts/trash',
        exception_class=ContactsException
    )
