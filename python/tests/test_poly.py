import unittest

from monom import Monom
from poly import Poly
from ring import BoolPolyRing


class TestBoolPoly(unittest.TestCase):

    def setUp(self):
        self.B = BoolPolyRing(4)

    def test_init(self):
        self.assertTrue(True)

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
        p = a*b + b + c

        r = p * a

        self.assertEqual(r, a*c)

    def test_mul_monom(self):
        a, b, c, d = self.B.gens
        m_a = Monom((1, 0, 0, 0))

        p = a*b + b + c

        r = p * m_a

        self.assertEqual(r, a*c)

    def test_S(self):
        a, b, c, d = self.B.gens

        _1 = Poly.one

        s = Poly.S(a*b*c, a*b + _1)
        self.assertEqual(s, c)

        s = Poly.S(a*b*c + _1, a*b + _1)
        self.assertEqual(s, c + _1)

        f = a*b*c + c*d + a*b + _1
        g = c*d + b

        s = Poly.S(f, g)
        self.assertEqual(s, a*b + a*c*d + c*d + _1)

    def test_NF_1(self):
        x0, x1, x2, x3 = self.B.gens

        _1 = Poly.one

        F = [
            x0 + x1 + x2 + x3,
            x0*x1 + x1*x2 + x0*x3 + x2*x3,
            x0*x1*x2 + x0*x1*x3 + x0*x2*x3 + x1*x2*x3,
            x0*x1*x2*x3 + _1
        ]

        p = x0*x1*x2 + x0*x1*x3 + x0*x2*x3 + x2

        p_nf = p.NF(F)

        self.assertEqual(p_nf, x1*x2*x3 + x2)

    def test_NF_2(self):
        x0, x1, x2, x3 = self.B.gens

        _1 = Poly.one
        _0 = Poly.zero
        # Groebner basis for F should reduce to 0
        G = [x0 + _1, x1 + _1, x2 + _1, x3 + _1]

        p = x0*x1*x2 + x0*x1*x3 + x0*x2*x3 + x2

        p_nf = p.NF(G)

        self.assertEqual(_0, p_nf)

    def test_NF_3(self):
        x0, x1, x2, x3 = self.B.gens

        _1 = Poly.one

        F = [
            x0 + x1 + x2 + x3,
            x0*x1 + x0*x3 + x1*x2 + x2*x3,
            x0*x1*x2 + x0*x1*x3 + x0*x2*x3 + x1*x2*x3,
            x0*x1*x2*x3 + _1,
            x1 + x3
        ]

        p2 = x1*x2*x3 + _1

        p_nf = p2.NF(F)

        self.assertEqual(p_nf, x2*x3 + _1)

    def test_NF_4(self):
        x1, x2, x3 = self.B.gens[:3]

        _1 = Poly.one

        F = [
            x1*x2*x3,
            x1*x2*x3 + x1*x2,
            x1*x2*x3 + x1*x3,
            x1*x2*x3 + x1*x2 + x1*x3 + x1,
            x1*x2*x3 + x2*x3,
            x1*x2*x3 + x1*x2 + x2*x3 + x2,
            x1*x2*x3 + x1*x3 + x2*x3 + x3,
            x1*x2*x3 + x1*x2 + x1*x3 + x1 + x2*x3 + x2 + x3 + _1
        ]

        # S-polynomial for p = x1*x2*x3 + x1*x2 and
        # q = x1*x2*x3 + x1*x2 + x1*x3 + x1 + x2*x3 + x2 + x3 + 1
        s = x1*x3 + x1 + x2*x3 + x2 + x3 + _1

        nf = s.NF(F)

        self.assertTrue(s == nf)

    def test_NF_5(self):
        x1, x2, x3 = self.B.gens[:3]

        _1 = Poly.one

        s = x1*x3 + x1 + x2*x3 + x2 + x3 + _1

        F = [
            x1*x2*x3,
            x1*x2*x3 + x1*x2,
            x1*x2*x3 + x1*x3,
            x1*x2*x3 + x1*x2 + x1*x3 + x1,
            x1*x2*x3 + x2*x3,
            x1*x2*x3 + x1*x2 + x2*x3 + x2,
            x1*x2*x3 + x1*x3 + x2*x3 + x3,
            x1*x2*x3 + x1*x2 + x1*x3 + x1 + x2*x3 + x2 + x3 + _1,
            x1*x3,
            x2*x3,
            x3,
            x1*x2,
            x2,
            x1,
            _1
        ]

        # Should reduce to 0
        nf = s.NF(F)

        self.assertTrue(nf == Poly.zero)
