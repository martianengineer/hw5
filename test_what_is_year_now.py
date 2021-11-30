#!/usr/bin/env python3

import unittest
from io import StringIO
from unittest.mock import patch
from urllib.error import URLError

from what_is_year_now import what_is_year_now


class TestWhatIsYearNow(unittest.TestCase):
    @patch('urllib.request.urlopen')
    def test_basic(self, urlopen_mock):
        normal_response_body = """{"$id":"1",
        "currentDateTime":"2021-11-30T02:34Z","utcOffset":"00:00:00",
        "isDayLightSavingsTime":false,"dayOfTheWeek":"Tuesday",
        "timeZoneName":"UTC","currentFileTime":132827132797333343,
        "ordinalDate":"2021-334","serviceResponse":null}"""

        urlopen_mock.return_value = StringIO(normal_response_body)
        self.assertEqual(what_is_year_now(), 2021)

    @patch('urllib.request.urlopen')
    def test_unreachable_external_api(self, urlopen_mock):
        urlopen_mock.side_effect = URLError("no connectivity")
        self.assertRaises(URLError, what_is_year_now)

    @patch('urllib.request.urlopen')
    def test_current_date_time_format_YYYY_MM_DD(self, urlopen_mock):
        response_body = """{"currentDateTime":"2021-11-30T02:34Z"}"""
        urlopen_mock.return_value = StringIO(response_body)
        self.assertEqual(what_is_year_now(), 2021)

    @patch('urllib.request.urlopen')
    def test_current_date_time_format_YYYY_MM_DD_dots(self, urlopen_mock):
        response_body = """{"currentDateTime":"01.03.2019T02:34Z"}"""
        urlopen_mock.return_value = StringIO(response_body)
        self.assertEqual(what_is_year_now(), 2019)

    @patch('urllib.request.urlopen')
    def test_current_date_time_invalid_format(self, urlopen_mock):
        response_body = """{"currentDateTime":"01,03,2019T02:34Z"}"""
        urlopen_mock.return_value = StringIO(response_body)
        self.assertRaises(ValueError, what_is_year_now)


if __name__ == '__main__':
    unittest.main()
