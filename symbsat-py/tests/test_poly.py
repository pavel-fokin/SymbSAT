# pylint: disable=invalid-name
import unittest

from monom import Monom
from poly import Poly
from ring import BoolPolyRing


class TestBoolPoly(unittest.TestCase):

    def setUp(self):
        self.B = BoolPolyRing(4)

    def test_zero_poly(self):
        p1 = Poly([Monom([1, 0, 0, 0])])
        p2 = Poly([Monom([1, 0, 0, 0])])

        self.assertEqual(p1 + p2, Poly.zero)

    def test_lm(self):
        a, b, c, d = self.B.gens
        _1 = Poly.one

        f = a*b*c + c*d + a*b + _1
        g = c*d + b

        self.assertEqual(f.lm(), (a*b*c).lm())
        self.assertEqual(g.lm(), b.lm())

    def test_add(self):
        a, b, c, d = self.B.gens

        p = (a+b+c+d)*b*c

        self.assertEqual(p, a*b*c + b*c*d)

    def test_add_monom(self):
        a, b, c, d = self.B.gens
        m_ab = Monom((1, 1, 0, 0))

        p = a*b + b + c

        r = p + m_ab

        self.assertEqual(r, b + c)

    def test_mul(self):
        a, b, c, d = self.B.gens
        _1 = Poly.one

        p = (a + b + c + d) * b*c
        self.assertEqual(p, a*b*c + b*c*d)

        p = (a*b + b + c) * a
        self.assertEqual(p, a*c)

        p = (a*c + a + c + _1) * c
        self.assertTrue(p.is_zero())

    def test_mul_monom(self):
        a, b, c, d = self.B.gens
        m_a = Monom((1, 0, 0, 0))

        p = a*b + b + c

        r = p * m_a

        self.assertEqual(r, a*c)
