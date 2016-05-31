import unittest

from ring import BoolPolyRing
from polyfuncs import spoly, normal_form


class TestPolyUtils(object):

    def test_spoly(self):
        a, b, c, d = self.B.gens

        _1 = self.B.one

        s = spoly(a*b*c, a*b + _1)
        self.assertEqual(s, c)

        s = spoly(a*b*c + _1, a*b + _1)
        self.assertEqual(s, c + _1)

        f = a*b*c + c*d + a*b + _1
        g = c*d + b

        s = spoly(f, g)
        self.assertEqual(s, a*b + a*c*d + c*d + _1)

    def test_normal_form_1(self):
        x0, x1, x2, x3 = self.B.gens

        _1 = self.B.one

        F = [
            x0 + x1 + x2 + x3,
            x0*x1 + x1*x2 + x0*x3 + x2*x3,
            x0*x1*x2 + x0*x1*x3 + x0*x2*x3 + x1*x2*x3,
            x0*x1*x2*x3 + _1
        ]

        p = x0*x1*x2 + x0*x1*x3 + x0*x2*x3 + x2

        p_nf = normal_form(p, F)

        self.assertEqual(p_nf, x1*x2*x3 + x2)

    def test_normal_form_2(self):
        x0, x1, x2, x3 = self.B.gens

        _1 = self.B.one
        _0 = self.B.zero
        # Groebner basis for F should reduce to 0
        G = [x0 + _1, x1 + _1, x2 + _1, x3 + _1]

        p = x0*x1*x2 + x0*x1*x3 + x0*x2*x3 + x2

        p_nf = normal_form(p, G)

        self.assertEqual(_0, p_nf)

    def test_normal_form_3(self):
        x0, x1, x2, x3 = self.B.gens

        _1 = self.B.one

        F = [
            x0 + x1 + x2 + x3,
            x0*x1 + x0*x3 + x1*x2 + x2*x3,
            x0*x1*x2 + x0*x1*x3 + x0*x2*x3 + x1*x2*x3,
            x0*x1*x2*x3 + _1,
            x1 + x3
        ]

        p = x1*x2*x3 + _1

        p_nf = normal_form(p, F)

        self.assertEqual(p_nf, x2*x3 + _1)

    def test_normal_form_4(self):
        x1, x2, x3 = self.B.gens[:3]

        _1 = self.B.one

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

        nf = normal_form(s, F)

        self.assertEqual(s, nf)

    def test_normal_form_5(self):
        x1, x2, x3 = self.B.gens[:3]

        _1 = self.B.one

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
        nf = normal_form(s, F)

        self.assertTrue(nf.isZero())


class TestPolyListUtils(unittest.TestCase, TestPolyUtils):

    def setUp(self):
        self.B = BoolPolyRing(4, poly_type="list")


class TestPolyZDDUtils(unittest.TestCase, TestPolyUtils):

    def setUp(self):
        self.B = BoolPolyRing(4, poly_type="zdd")
