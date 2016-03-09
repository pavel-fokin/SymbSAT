import unittest

from monom import Monom
from poly import Poly


class TestBoolPoly(unittest.TestCase):

    def setUp(self):
        Monom.variables = "abcd"

    def test_init(self):
        self.assertTrue(True)

    def test_zero_poly(self):
        p1 = Poly([Monom([1,0,0,0])])
        p2 = Poly([Monom([1,0,0,0])])

        self.assertEqual(p1 + p2, Poly.zero)

    def test_add(self):
        a = Poly([Monom([1,0,0,0])])
        b = Poly([Monom([0,1,0,0])])
        c = Poly([Monom([0,0,1,0])])
        d = Poly([Monom([0,0,0,1])])

        p = (a+b+c+d)*b*c

        self.assertEqual(str(p), 'abc + bcd')

    def test_S(self):
        a = Poly([Monom([1,0,0,0])])
        b = Poly([Monom([0,1,0,0])])
        c = Poly([Monom([0,0,1,0])])
        d = Poly([Monom([0,0,0,1])])

        _1 = Poly([Monom.one])

        self.assertEqual('%s' % Poly.S(a*b*c, a*b + _1), 'c')
        self.assertEqual('%s' % Poly.S(a*b*c + _1, a*b + _1), 'c + 1')

        f = a*b*c + c*d + a*b + _1
        g = c*d + b

        self.assertEqual('%s' % Poly.S(f, g), 'ab + acd + cd + 1')

    def test_NF(self):
        return
        Monom.variables = ['x0', 'x1', 'x2', 'x3']
        x0 = Poly([Monom([1,0,0,0])])
        x1 = Poly([Monom([0,1,0,0])])
        x2 = Poly([Monom([0,0,1,0])])
        x3 = Poly([Monom([0,0,0,1])])

        _1 = Poly.one

        F = [
            x0 + x1 + x2 + x3,
            x0*x1 + x1*x2 + x0*x3 + x2*x3,
            x0*x1*x2 + x0*x1*x3 + x0*x2*x3 + x1*x2*x3,
            x0*x1*x2*x3 + _1
        ]

        p = x0*x1*x2 + x0*x1*x3 + x0*x2*x3 + x2

        p_nf = p.NF(F)

        self.assertEqual(str(p_nf), 'x1x2x3 + x2')

        # Groebner basis for F should reduce to 0
        G = [x0 + _1, x1 + _1, x2 + _1, x3 + _1]

        p_nf = p.NF(G)

        self.assertEqual(str(p_nf), '0')

        # Another example not reduced yet
        F1 = [
            x0 + x1 + x2 + x3,
            x0*x1 + x0*x3 + x1*x2 + x2*x3,
            x0*x1*x2 + x0*x1*x3 + x0*x2*x3 + x1*x2*x3,
            x0*x1*x2*x3 + _1,
            x1 + x3
        ]

        p2 = x1*x2*x3 + _1

        p_nf = p2.NF(F1)

        self.assertEqual(str(p_nf), 'x2x3 + 1')

    def test_NF_1(self):
        return
        Monom.variables = ['x1', 'x2', 'x3']
        x1 = Poly([Monom([1,0,0])])
        x2 = Poly([Monom([0,1,0])])
        x3 = Poly([Monom([0,0,1])])

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

    def test_NF_2(self):
        Monom.variables = ['x1', 'x2', 'x3']
        x1 = Poly([Monom([1,0,0])])
        x2 = Poly([Monom([0,1,0])])
        x3 = Poly([Monom([0,0,1])])

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
