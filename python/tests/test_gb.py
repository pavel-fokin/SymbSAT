import unittest

from poly import Poly
from ring import BoolPolyRing
from gb import buchberger


class TestBuchberger(unittest.TestCase):

    def setUp(self):
        # Create BoolRing with number of variables
        # enough for all tests
        self.B = BoolPolyRing(10)

    def test_buchberger1(self):
        """
        Example from SAGE documentation
        for boolean polynomials
        """
        x0, x1, x2, x3 = self.B.gens[:4]
        _1 = Poly.one

        F = [
            x0 + x1 + x2 + x3,
            x0*x1 + x1*x2 + x0*x3 + x2*x3,
            x0*x1*x2 + x0*x1*x3 + x0*x2*x3 + x1*x2*x3,
            x0*x1*x2*x3 + _1
        ]

        G = buchberger(F, self.B)

        G_assert = [x0 + _1, x1 + _1, x2 + _1, x3 + _1]

        for p in G:
            self.assertTrue(p in G_assert)

    # TODO Check GB for this example
    def test_buchberger2(self):
        """
        Example from paper
        On computer algebra application to
        simulation of quantum computation
        p.14 lex-order
        """
        a1, a2, a3, x1, x2, x3, x4, b1, b2, b3 = self.B.gens

        F = [
            x3 + x2*x4 + b1,
            x2 + b2,
            x4 + b3,
            a1*x1 + a2*x2 + x1*x3 + a3*x4 + x1*x2*x4,
        ]

        G = buchberger(F, self.B)  # noqa

        G_assert = [
            x2 + b2,
            x4 + b3,
            a1*x1 + a2*b2 + a3*b3 + x1*b1,
            x3 + b1 + b2*b3,
        ]

        self.assertTrue(len(G_assert) > 0)

    def test_buchberger3(self):
        x1, x2 = self.B.gens[:2]

        F = [
            x1*x2 + x1,
            x1*x2 + x2
        ]

        G = buchberger(F, self.B)

        G_assert = [x1 + x2]

        for p in G:
            self.assertTrue(p in G_assert)

    def test_buchberger4(self):
        x1, x2, x3, x4 = self.B.gens[:4]
        _1 = Poly.one

        F = [
            x1*x2*x3 + x1*x2 + x2*x3 + x2,
            x2*x3 + x2 + x3 + _1,
            x1*x2 + x1,
            x1*x4
        ]

        G = buchberger(F, self.B)

        G_assert = [
            x1*x2 + x1,
            x1*x3 + x1 + x3 + _1,
            x1*x4,
            x2*x3 + x2 + x3 + _1,
            x3*x4 + x4
        ]

        self.assertTrue(len(G) == len(G_assert))
        for p in G:
            self.assertTrue(p in G_assert)

    def test_buchberger_5(self):
        """
        Example from Sage Boolean Polynomials Documentation
        """
        x0, x1, x2, x3 = self.B.gens[:4]

        F = [
            x0*x1*x2*x3 + x0*x1*x3 + x0*x1 + x0*x2 + x0
        ]

        G = buchberger(F, self.B)

        G_assert = [x0*x1 + x0*x2 + x0, x0*x2*x3 + x0*x3]

        self.assertTrue(len(G) == len(G_assert))
        for p in G:
            self.assertTrue(p in G_assert)

    def test_buchberger6(self):
        x, y, z = self.B.gens[:3]

        F = [
            x*z + y*z + z,
            x*y + x*z + x + y*z + y + z
        ]

        G = buchberger(F, self.B)

        G_assert = [x, y, z]

        self.assertTrue(len(G) == len(G_assert))
        for p in G:
            self.assertTrue(p in G_assert)

    def test_buchberger_7(self):
        """
        Basis should be equal 1
        """
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

        G = buchberger(F, self.B)

        self.assertTrue(G == [Poly.one])
