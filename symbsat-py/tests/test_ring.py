import unittest

from zdd import ZDD
from ring import BoolPolyRing


class TestBoolPolyRing(unittest.TestCase):

    def setUp(self):
        self.ring_size = 5

    def test_ring(self):
        B = BoolPolyRing(self.ring_size)
        x1, x2, x3, x4, x5 = B.gens

        _1 = B.one
        self.assertTrue(_1.is_one())
        self.assertFalse(_1.is_zero())

        _0 = B.zero
        self.assertTrue(_0.is_zero())
        self.assertFalse(_0.is_one())

        self.assertEqual(self.ring_size, len(B.gens))

    def test_ring_zdd(self):
        B = BoolPolyRing(self.ring_size, poly_type="zdd")
        x1, x2, x3, x4, x5 = B.gens

        _1 = B.one
        self.assertTrue(_1.is_one())
        self.assertFalse(_1.is_zero())

        _0 = B.zero
        self.assertTrue(_0.is_zero())
        self.assertFalse(_0.is_one())

        for var in B.gens:
            self.assertTrue(isinstance(var, ZDD))
