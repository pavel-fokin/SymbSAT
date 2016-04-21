import unittest

from ring import BoolPolyRing


class TestBoolPolyRing(unittest.TestCase):

    def test_ring(self):
        ring_size = 5

        B = BoolPolyRing(ring_size)
        x1, x2, x3, x4, x5 = B.gens

        self.assertEqual(ring_size, len(B.gens))
