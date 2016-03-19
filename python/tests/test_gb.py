import unittest

from monom import Monom
from poly import Poly, generate_n_vars
from gb import autoreduce, buchberger


class TestBuchberger(unittest.TestCase):

    def test_buchberger1(self):
        """
        Example from SAGE documentation
        for boolean polynomials
        """
        #  return
        variables = ('x0', 'x1', 'x2', 'x3')
        x0, x1, x2, x3 = generate_n_vars(variables)
        _1 = Poly.one

        F = [
            x0 + x1 + x2 + x3,
            x0*x1 + x1*x2 + x0*x3 + x2*x3,
            x0*x1*x2 + x0*x1*x3 + x0*x2*x3 + x1*x2*x3,
            x0*x1*x2*x3 + _1
        ]

        G = buchberger(F, variables)

        G_assert = [x0 + _1, x1 + _1, x2 + _1, x3 + _1]

        for p in G:
            self.assertTrue(p in G_assert)

    #TODO Check GB for this example
    def test_buchberger2(self):
        """
        Example from paper
        On computer algebra application to
        simulation of quantum computation
        p.14 lex-order
        """
        #  return
        variables = ('a1', 'a2', 'a3', 'x1', 'x2', 'x3', 'x4', 'b1', 'b2', 'b3')
        a1, a2, a3, x1, x2, x3, x4, b1, b2, b3 = generate_n_vars(variables)

        F = [
            x3 + x2*x4 + b1,
            x2 + b2,
            x4 + b3,
            a1*x1 + a2*x2 + x1*x3 + a3*x4 + x1*x2*x4,
        ]

        G = buchberger(F, variables)

        G_assert = [
            x2 + b2,
            x4 + b3,
            a1*x1 + a2*b2 + a3*b3 + x1*b1,
            x3 + b1 + b2*b3,
        ]

        #  for p in G:
            #  print(p)
            #  self.assertTrue(p in G_assert)

    def test_buchberger3(self):
        variables = ('x1', 'x2')
        x1, x2 = generate_n_vars(variables)
        _1 = Poly.one

        F = [
            x1*x2 + x1,
            x1*x2 + x2
        ]

        G = buchberger(F, variables)

        G_assert = [x1 + x2]

        for p in G:
            self.assertTrue(p in G_assert)

    def test_buchberger4(self):
        variables = ('x1', 'x2', 'x3', 'x4')
        x1, x2, x3, x4 = generate_n_vars(variables)
        _1 = Poly.one

        F = [
            x1*x2*x3 + x1*x2 + x2*x3 + x2,
            x2*x3 + x2 + x3 + _1,
            x1*x2 + x1,
            x1*x4
        ]

        G = buchberger(F, variables)

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
        variables = ('x0', 'x1', 'x2', 'x3')
        x0, x1, x2, x3 = generate_n_vars(variables)
        _1 = Poly.one

        F = [
            x0*x1*x2*x3 + x0*x1*x3 + x0*x1 + x0*x2 + x0
        ]

        G = buchberger(F, variables)

        G_assert = [x0*x1 + x0*x2 + x0, x0*x2*x3 + x0*x3]

        self.assertTrue(len(G) == len(G_assert))
        for p in G:
            self.assertTrue(p in G_assert)

    def test_buchberger6(self):
        variables = ('x', 'y', 'z')
        x, y, z = generate_n_vars(variables)
        _1 = Poly.one

        F = [
            x*z + y*z + z,
            x*y + x*z + x + y*z + y + z
        ]

        G = buchberger(F, variables)

        G_assert = [x, y, z]

        self.assertTrue(len(G) == len(G_assert))
        for p in G:
            self.assertTrue(p in G_assert)

    def test_buchberger_7(self):
        """
        Basis should be equal 1
        """
        variables = ('x1', 'x2', 'x3')
        x1, x2, x3 = generate_n_vars(variables)
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

        G = buchberger(F, variables)

        self.assertTrue(G == [Poly.one])
