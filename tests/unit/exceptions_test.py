import pickle
import unittest

from smsapi.exception import (
    ClientException,
    EndpointException,
    SendException,
    SmsApiException,
)


class ExceptionPicklingTest(unittest.TestCase):
    """Ensure SMS API custom exceptions are pickleable."""

    message = 'test exception pickling'

    def test_client_exception_pickling(self):
        """Ensure ``ClientException`` is pickleable."""
        self.assert_is_pickleable(ClientException(self.message))

    def test_endpoint_exception_pickling(self):
        """Ensure ``EndpointException`` is pickleable."""
        self.assert_is_pickleable(EndpointException(self.message))

    def test_send_exception_pickling(self):
        """Ensure ``SendException`` is pickleable."""
        self.assert_is_pickleable(
            SendException(self.message, code='pickling_error'),
        )

    def test_smsapi_exception_pickling(self):
        """Ensure ``SmsApiException`` is pickleable."""
        self.assert_is_pickleable(SmsApiException(self.message))

    def assert_is_pickleable(self, exception):
        """Assert exception is pickleable."""
        pickled_exception = pickle.dumps(exception)
        self.assertEqual(pickle.loads(pickled_exception), exception)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ExceptionPicklingTest))
    return suite
