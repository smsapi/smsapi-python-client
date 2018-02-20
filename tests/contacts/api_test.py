# -*- coding: utf-8 -*-

import unittest
from datetime import datetime, date
from smsapi.contacts.models import ContactModel, CustomFieldModel
from tests import SmsApiTestCase
from tests.contacts.fixtures import create_collection_from_fixture


class ContactsApiTest(SmsApiTestCase):

    def test_create_contact(self):
        contact = self.client.contacts.create_contact(
            first_name='Jon',
            phone_number=987654321,
            email='jondoe@somedomain.com')

        self.assertIsInstance(contact, ContactModel)
        self.assertIsInstance(contact.date_created, datetime)
        self.assertIsInstance(contact.birthday_date, date)

    def test_update_contact(self):
        contact = self.client.contacts.update_contact(contact_id=1, last_name='Doe')

        self.assertEqual(contact.last_name, 'Doe')

    def test_list_contacts(self):
        contacts = self.client.contacts.list_contacts()

        expected_contacts = create_collection_from_fixture('list_contacts', ContactModel)

        self.assertEqual(contacts, expected_contacts)

    def test_get_contact(self):
        self.client.contacts.get_contact(contact_id=1)

    def test_delete_contact(self):
        self.client.contacts.delete_contact(contact_id=1)

    def test_list_contacts_groups(self):
        self.client.contacts.list_contact_groups(contact_id=1)

    def test_bind_contact_to_group(self):
        self.client.contacts.bind_contact_to_group(contact_id=1, group_id=1)

    def test_list_groups(self):
        self.client.contacts.list_groups()

        self.assertEqual(self.client.domain + 'contacts/groups', self.request_fake.url)
        self.assertEqual({'with': 'contacts_count'}, self.request_fake.params)

    def test_create_group(self):
        self.client.contacts.create_group()

    def test_delete_group(self):
        self.client.contacts.delete_group(group_id=1)

    def test_get_group(self):
        self.client.contacts.get_group(group_id=1)

        self.assertEqual(self.client.contacts.client.domain + 'contacts/groups/1', self.request_fake.url)
        self.assertEqual({'with': 'contacts_count'}, self.request_fake.params)

    def test_update_group(self):
        self.client.contacts.update_group(group_id=1)

    def test_list_group_permission(self):
        self.client.contacts.list_group_permissions(group_id=1)

    def test_create_group_permission(self):
        self.client.contacts.create_group_permission(group_id=1)

    def test_list_user_group_permission(self):
        self.client.contacts.list_user_group_permissions(group_id=1, username='test')

    def test_delete_user_group_permission(self):
        self.client.contacts.delete_user_group_permission(group_id=1, username='test')

    def test_update_user_group_permission(self):
        self.client.contacts.update_user_group_permission(group_id=1, username='test')

    def test_unpin_contact_from_group(self):
        self.client.contacts.unpin_contact_from_group(group_id=1, contact_id=1)

    def test_contact_is_in_group(self):
        self.client.contacts.contact_is_in_group(group_id=1, contact_id=1)

    def test_pin_contact_to_group(self):
        self.client.contacts.pin_contact_to_group(group_id=1, contact_id=1)

    def test_list_custom_fields(self):
        r = self.client.contacts.list_custom_fields()

        expected_collection = create_collection_from_fixture('list_custom_fields', CustomFieldModel)

        self.assertEqual(expected_collection, r)

    def test_create_custom_field(self):
        self.client.contacts.create_custom_field()

    def test_delete_custom_field(self):
        self.client.contacts.delete_custom_field(field_id=1)

    def test_update_custom_field(self):
        self.client.contacts.update_custom_field(field_id=1, name='test_f')

    def test_unpin_contact_from_group_by_query(self):
        number, email = '100200300', 'some@email.com'

        args = {'phone_number': number, 'email': email, 'q': 'any text'}

        self.client.contacts.unpin_contact_from_group_by_query(group_id=1, **args)

        self.assertEqual(args, self.request_fake.data)

    def test_count_contacts_in_trash(self):
        r = self.client.contacts.count_contacts_in_trash()

        self.assertEqual(2, r)

    def test_restore_contacts_in_trash(self):
        self.client.contacts.restore_contacts_in_trash()

    def test_clean_trash(self):
        self.client.contacts.clean_trash()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ContactsApiTest))
    return suite
