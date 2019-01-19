import unittest

import symbsat.gbinv as gbinv
from symbsat.monom import Monom4 as Monom


class TestGBInv(unittest.TestCase):

    def test_nmulti_vars(self):
        m1 = Monom([1, 1, 1, 0])

        vars_M = gbinv.nmulti_vars(m1)

        self.assertTrue(vars_M)

    def test_multi_vars(self):
        self.assertTrue(True)

    def test_is_divisible_inv(self):
        self.assertTrue(True)
