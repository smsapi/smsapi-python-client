# -*- coding: utf-8 -*-

from smsapi.models import InvalidNumber


class SmsApiException(Exception):

    def __init__(self, message, code=None, *args):
        super(SmsApiException, self).__init__(*args)

        self.message = message
        self.code = code

    @classmethod
    def from_dict(cls, data):
        message = data.get('message')
        error = data.get('error')

        return cls(message, error)

    def __eq__(self, other):
        return other and self.__dict__ == other.__dict__

    def __repr__(self):
        return "<%s %s>" % (self.__class__.__name__, self.__dict__)

    def __str__(self):
        return "<%s %s>" % (self.__class__.__name__, self.__dict__)


class ClientException(SmsApiException):
    pass


class EndpointException(SmsApiException):

    def __init__(self, message, code=None, *args, **kwargs):
        super(EndpointException, self).__init__(message, code, *args)

        self.url = kwargs.get('url')
        self.http_method = kwargs.get('http_method')


class SendException(EndpointException):

    def __init__(self, message, code):
        super(SendException, self).__init__(message, code)

        self.invalid_numbers = []

    @classmethod
    def from_dict(cls, response):

        message = response.get('message')
        error = response.get('error')

        e = cls(message, error)

        invalid_numbers = response.get('invalid_numbers') or []

        for n in invalid_numbers:
            e.add_invalid_number(InvalidNumber.from_dict(n))

        return e

    def add_invalid_number(self, invalid_number):
        self.invalid_numbers.append(invalid_number)