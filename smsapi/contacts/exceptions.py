# -*- coding: utf-8 -*-

from smsapi.exception import EndpointException


class ContactsException(EndpointException):

    def __init__(self, message, code=None, type=None, errors=None):

        super(ContactsException, self).__init__(message)

        self.message = message
        self.code = code or ''
        self.type = type
        self.errors = errors

    @classmethod
    def from_dict(cls, data):
        """
        Create EndpointException instance from dictionary.

        Args:
            data (dict)
        """

        code = data.get('code')
        type = data.get('type')
        message = data.get('message')

        return cls(message, code, type)
