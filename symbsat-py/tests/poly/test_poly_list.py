import unittest

from symbsat.monom import Monom
from symbsat.poly_new import PolyList


class TestPolyList(unittest.TestCase):

    def test_init_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            PolyList()

    def test_init_from_monoms(self):
        Monom.size = 4
        monom_a = Monom(vars=[1])
        monom_b = Monom(vars=[2])
        PolyList(monoms=[monom_a, monom_b])
