#!/usr/bin/env python3

import pytest

from one_hot_encoder import fit_transform


def test_one_hot_encoder():
    # Test empty input.
    with pytest.raises(TypeError):
        fit_transform()

    # Test single input.
    assert fit_transform('') == [('', [1])]
    assert fit_transform('a') == [('a', [1])]
    assert fit_transform('ab') == [('ab', [1])]

    # Basic test.
    assert fit_transform('', 'a') == [('', [0, 1]), ('a', [1, 0])]
    assert fit_transform('a', '') == [('a', [0, 1]), ('', [1, 0])]

    # Test repeated inputs.
    assert fit_transform('', '', 'a') == [('', [0, 1]), ('', [0, 1]),
                                          ('a', [1, 0])]
    assert fit_transform('', 'a', 'a') == [('', [0, 1]), ('a', [1, 0]),
                                           ('a', [1, 0])]
