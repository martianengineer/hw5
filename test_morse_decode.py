#!/usr/bin/env python3

import pytest
from morse import decode


@pytest.mark.parametrize('encoded_string,expected_output', [
    ('', ''),
    ('... --- ...', 'SOS'),
    ('- .... -..-', 'THX')
])
def test_decode(encoded_string, expected_output):
    assert decode(encoded_string) == expected_output
