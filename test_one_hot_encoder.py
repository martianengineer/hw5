#!/usr/bin/env python3

import unittest

from one_hot_encoder import fit_transform


class TestOneHotEncoder(unittest.TestCase):
    def test_empty(self):
        self.assertRaises(TypeError, fit_transform)

    def test_single_input(self):
        self.assertIsInstance(fit_transform('a', ''), list)
        self.assertEqual(fit_transform(''), [('', [1])])
        self.assertEqual(fit_transform('a'), [('a', [1])])
        self.assertEqual(fit_transform('ab'), [('ab', [1])])

    def test_basic(self):
        self.assertEqual(fit_transform('', 'a'), [('', [0, 1]), ('a', [1, 0])])
        self.assertEqual(fit_transform('a', ''), [('a', [0, 1]), ('', [1, 0])])

    def test_repeated(self):
        self.assertEqual(fit_transform('', '', 'a'),
                         [('', [0, 1]), ('', [0, 1]), ('a', [1, 0])])
        self.assertEqual(fit_transform('', 'a', 'a'),
                         [('', [0, 1]), ('a', [1, 0]), ('a', [1, 0])])


if __name__ == '__main__':
    unittest.main()
