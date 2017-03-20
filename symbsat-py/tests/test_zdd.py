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
        _1 = self.B.one

        p = a + c + c + d
        self.assertEqual(p, a + d)

        p = a + a + b + b
        self.assertTrue(p.isZero())

        p = a + a + _1
        self.assertTrue(p.isOne())

    def test_add_monom(self):
        a, b, c, d = self.B.gens
        m_ab = Monom((1, 1, 0, 0))

        p = a*b + b + c

        r = p + m_ab

        self.assertEqual(r, b + c)

    def test_mul(self):
        a, b, c, d = self.B.gens
        _1 = self.B.one

        p = (a + b + c + d) * b*c
        self.assertEqual(p, a*b*c + b*c*d)

        p = (a*b + b + c) * a
        self.assertEqual(p, a*c)

        p = (a*c + a + c + _1) * c
        self.assertTrue(p.isZero())

        p = _1 * a
        self.assertEqual(p, a)

        p = a * _1
        self.assertEqual(p, a)

    def test_mul_monom(self):
        a, b, c, d = self.B.gens
        m_a = Monom((1, 0, 0, 0))

        p = a*b + b + c

        r = p * m_a

        self.assertEqual(r, a*c)

    def test_lm(self):
        a, b, c, d = self.B.gens

        m_abc = Monom((1, 1, 1, 0))
        m_b = Monom((0, 1, 0, 0))

        _1 = self.B.one

        f = a*b*c + c*d + a*b + _1
        g = c*d + b

        self.assertEqual(f.lm(), m_abc)
        self.assertEqual(g.lm(), m_b)

    def test_str(self):
        a, b, c, d = self.B.gens
        _1 = self.B.one
        _0 = self.B.zero

        self.assertEqual(str(a + _1), '[0] + 1')
        self.assertEqual(str(_1), '1')
        self.assertEqual(str(_0), '0')
