# -*- coding: utf-8 -*-

import unittest
from factorial import afactaral


class FactorialTestCase(unittest.TestCase):

    def test_factor(self):
        f = afactaral(3)
        self.assertEqual(f, 6)

# unittest.main()
