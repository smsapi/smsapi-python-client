import unittest
import datetime

from smsapi.utils import convert_iso8601_str_to_datetime, FixedOffset


class UtilsTest(unittest.TestCase):

    def test_convert_iso8601_string_with_Z_utc_offset_info_to_datetime(self):
        iso8601_str = "2060-01-01T20:00:00Z"

        r = convert_iso8601_str_to_datetime(iso8601_str)

        self.assertEqual(datetime.datetime(2060, 1, 1, 20, 0, 0, tzinfo=FixedOffset()), r)

    def test_convert_iso8601_string_without_utc_offset_to_datetime(self):
        iso8601_str = "2060-01-01T20:00:00"

        r = convert_iso8601_str_to_datetime(iso8601_str)

        self.assertEqual(datetime.datetime(2060, 1, 1, 20, 0, 0, tzinfo=FixedOffset()), r)

    def test_convert_iso8601_string_with_colon_separated_utc_offset_info_to_datetime(self):
        iso8601_str = "2060-01-01T20:00:00+02:04"

        r = convert_iso8601_str_to_datetime(iso8601_str)

        expected_datetime = datetime.datetime(2060, 1, 1, 20, 0, 0,
                                              tzinfo=FixedOffset(offset_hours=2, offset_minutes=4))
        self.assertEqual(expected_datetime, r)

    def test_convert_iso8601_string_with_utc_offset_info_to_datetime(self):
        iso8601_str = "2060-01-01T20:00:00+0204"

        r = convert_iso8601_str_to_datetime(iso8601_str)

        expected_datetime = datetime.datetime(2060, 1, 1, 20, 0, 0,
                                              tzinfo=FixedOffset(offset_hours=2, offset_minutes=4))
        self.assertEqual(expected_datetime, r)


def suite():
    s = unittest.TestSuite()
    s.addTest(unittest.makeSuite(UtilsTest))
    return s
