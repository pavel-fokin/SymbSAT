import unittest

from monom import Monom
from zdd import ZDD
from ring import BoolPolyRing


class TestZDD(unittest.TestCase):

    def setUp(self):
        self.B = BoolPolyRing(4, poly_type="zdd")

    def test_init(self):
        a, b, c, d = self.B.gens

        z1 = ZDD(1)
        self.assertEqual(z1, b)

        m = Monom((1, 1, 1, 1))

        z = ZDD(monom=m)

        self.assertEqual(z, a*b*c*d)

    def test_add(self):
        a, b, c, d = self.B.gens

        p = a + c + c + d
        self.assertEqual(p, a + d)

        p = a + a + b + b
        self.assertTrue(p.isZero())

    def test_add_monom(self):
        a, b, c, d = self.B.gens
        m_ab = Monom((1, 1, 0, 0))

        p = a*b + b + c

        r = p + m_ab

        self.assertEqual(r, b + c)

    def test_mul(self):
        a, b, c, d = self.B.gens

        p = (a + b + c + d) * b*c
        self.assertEqual(p, a*b*c + b*c*d)

        p = (a*b + b + c) * a
        self.assertEqual(p, a*c)

    def test_mul_monom(self):
        a, b, c, d = self.B.gens
        m_a = Monom((1, 0, 0, 0))

        p = a*b + b + c

        r = p * m_a

        self.assertEqual(r, a*c)
