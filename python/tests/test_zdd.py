import unittest

from zdd import ZDD


class TestZDD(unittest.TestCase):

    def test_init(self):
        z1 = ZDD(1)
        self.assertTrue(True)

    def test_add(self):
        z1 = ZDD(1)
        z2 = ZDD(2)

        z3 = z1 + z2
        self.assertTrue(True)

    def test_mul(self):
        z1 = ZDD(1)
        z2 = ZDD(2)

        z3 = z1 * z2

        self.assertTrue(True)

    def test_lm(self):
        z1 = ZDD(1)
        z2 = ZDD(2)

        z3 = z1 * z2 + z1

        self.assertTrue(True)

    def test_iter(self):
        z1 = ZDD(1)
        z2 = ZDD(2)

        z3 = z1 + z2

        self.assertTrue(True)
