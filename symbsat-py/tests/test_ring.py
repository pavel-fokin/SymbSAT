import unittest

from zdd import ZDD
from ring import BoolPolyRing


class TestBoolPolyRing(unittest.TestCase):

    def setUp(self):
        self.ring_size = 5

    def test_ring(self):
        B = BoolPolyRing(self.ring_size)
        x1, x2, x3, x4, x5 = B.gens

        self.assertEqual(self.ring_size, len(B.gens))

    def test_ring_zdd(self):
        B = BoolPolyRing(self.ring_size, poly_type="zdd")
        x1, x2, x3, x4, x5 = B.gens

        for var in B.gens:
            self.assertTrue(isinstance(var, ZDD))
