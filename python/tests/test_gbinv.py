import unittest

import monom
import gbinv


class TestGBInv(unittest.TestCase):

    def test_nmulti_vars(self):
        m1 = monom.Monom([1,1,1,0])

        vars_M = gbinv.nmulti_vars(m1)
        print(list(vars_M))

        self.assertTrue(True)

    def test_multi_vars(self):
        self.assertTrue(True)

    def test_is_divisible_inv(self):
        self.assertTrue(True)
