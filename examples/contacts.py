import os

from smsapi.client import SmsApiPlClient


access_token = os.getenv('SMSAPI_ACCESS_TOKEN')


client = SmsApiPlClient(access_token=access_token)


def create_contact():
    c = client.contacts.create_contact(
        first_name='Jon',
        last_name='Doe',
        idx='id for Your use',
        phone_number=123123123,
        email='jondoe@somedomain.com',
        birthday_date='1970-01-01',
        gender='{male|female|undefined}',
        city='some_city',
        source='some_contact_source',
        description='Jon Doe')

    print(
        c.id, c.idx, c.first_name, c.last_name, c.phone_number,
        c.gender, c.city, c.email, c.source, c.description,
        c.birthday_date, c.date_created, c.date_updated)


def update_contacts():
    c = client.contacts.update_contact(contact_id=1, description='new_description')

    print(c.id, c.first_name, c.last_name, c.phone_number)


def get_all_contacts():
    l = client.contacts.list_contacts()

    for c in l:
        print(c.id, c.first_name, c.last_name, c.phone_number)


def get_contacts():
    c = client.contacts.get_contact(contact_id=1)

    print(c.id)


def get_group():
    g = client.contacts.get_group(group_id=1)

    print(
        g.id, g.name, g.contacts_count, g.date_created,
        g.date_updated, g.description, g.created_by, g.idx, g.permissions)


def get_contact_groups():
    l = client.contacts.list_contact_groups(contact_id=1)

    for g in l:
        print(g.id)


def add_contact_to_group():
    client.contacts.bind_contact_to_group(contact_id=1, group_id=1)


def remove_contact():
    client.contacts.delete_contact(contact_id=1)


def create_group():
    g = client.contacts.create_group(name='group_name', description='group_description')

    print(g.id, g.name, g.contacts_count, g.date_created)


def get_all_groups():
    l = client.contacts.list_groups()

    for g in l:
        print(g.id)


def update_group():
    g = client.contacts.update_group(group_id=1, name='new_name')

    print(g.id, g.name, g.contacts_count, g.date_created)


def remove_group():
    client.contacts.delete_group(group_id=1)


def get_group_permissions():
    p = client.contacts.list_group_permissions(group_id=1)

    print(p.username, p.group_id, p.write, p.read, p.send)


def create_group_permissions():
    client.contacts.create_group_permission(group_id=1, read = True, write = False, send = True)


def get_user_group_permissions():
    client.contacts.list_user_group_permissions(group_id=1, username='some_username')


def remove_user_group_permissions():
    client.contacts.delete_user_group_permission(group_id=1, username='some_username')


def update_user_group_permissions():
    client.contacts.update_user_group_permission(group_id=1, username='some_username', read=False)


def remove_contacts_from_group():
    client.contacts.unpin_contact_from_group(group_id=1, contact_id=1)


def check_if_contact_is_in_group():
    client.contacts.contact_is_in_group(group_id=1, contact_id=1)


def list_custom_fields():
    l = client.contacts.list_custom_fields()

    for f in l:
        print(f.id, f.name, f.type)


def create_custom_field():
    f = client.contacts.create_custom_field(name='some_field_name', type='{TEXT|DATE|EMAIL|NUMBER|PHONENUMBER|}')

    print(f.id, f.name, f.type)


def update_custom_filed():
    client.contacts.update_custom_field(field_id='1', name='new_field_name')


def remove_custom_field():
    client.contacts.delete_custom_field(field_id=1)
