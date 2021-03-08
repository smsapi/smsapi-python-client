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

    def test_exception_pickling(self):
        """Ensure SMS API exceptions are pickleable."""
        message = 'test exception pickling'
        exceptions = [
            ClientException(message),
            EndpointException(message),
            SendException(message, code='pickiling_error'),
            SmsApiException(message),
        ]
        for exception in exceptions:
            with self.subTest(exception=exception):
                self.assert_is_pickleable(exception)

    def assert_is_pickleable(self, exception):
        """Assert exception is pickleable."""
        pickled_exception = pickle.dumps(exception)
        self.assertEqual(pickle.loads(pickled_exception), exception)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ExceptionPicklingTest))
    return suite
