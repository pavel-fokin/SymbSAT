# pylint: disable=invalid-name
import unittest

from monom import Monom
from order import Lex, DegLex, DegRevLex


class TestBoolMonomOrder(unittest.TestCase):

    def setUp(self):
        Monom.size = 4
        self.variables = (
            Monom(vars=[0]),  # a
            Monom(vars=[1]),  # b
            Monom(vars=[2]),  # c
            Monom(vars=[3]),  # d
        )

    def test_lex(self):
        """Test lexicographic order."""
        a, b, c, d = self.variables
        _1 = Monom.one
        _0 = Monom()

        # a > b > c > d
        self.assertFalse(Lex.lt(a, b))  # a > b
        self.assertFalse(Lex.lt(b, b))  # b > b
        self.assertTrue(Lex.lt(b, a))   # b < a
        self.assertTrue(Lex.lt(d, c))   # c < d

        self.assertFalse(Lex.lt(a, _1))  # a < 1
        self.assertTrue(Lex.lt(_1, a))  # 1 < a

        self.assertTrue(Lex.lt(_0, a))  # 0 < a
        self.assertTrue(Lex.lt(_0, _1))  # 0 < 1

        self.assertFalse(Lex.lt(a, _0))  # a > 0
        self.assertFalse(Lex.lt(_1, _0))  # 1 > 0

        ab = Monom(vars=[0, 1])
        bc = Monom(vars=[1, 2])

        # bc < a < ab
        self.assertTrue(Lex.lt(a, ab))  # a < ab
        self.assertTrue(Lex.lt(bc, a))  # bc < a
        self.assertTrue(Lex.lt(bc, ab))  # bc < ab

        abc = Monom(vars=[0, 1, 2])
        bcd = Monom(vars=[1, 2, 3])

        # bcd < abc
        self.assertTrue(Lex.lt(bcd, abc))  # bcd < abc
        self.assertFalse(Lex.lt(abc, bcd))  # abc > bcd

    def test_deglex(self):
        a, b, c, d = self.variables
        _1 = Monom.one
        _0 = Monom()

        self.assertFalse(DegLex.lt(a, b))
        self.assertFalse(DegLex.lt(b, c))
        self.assertFalse(DegLex.lt(c, d))
        self.assertFalse(DegLex.lt(a, d))

        self.assertFalse(Lex.lt(a, _1))  # a < 1
        self.assertTrue(Lex.lt(_1, a))  # 1 < a

        self.assertTrue(Lex.lt(_0, a))  # 0 < a
        self.assertTrue(Lex.lt(_0, _1))  # 0 < 1

        self.assertFalse(Lex.lt(a, _0))  # a > 0
        self.assertFalse(Lex.lt(_1, _0))  # 1 > 0

        ab = Monom(vars=[0, 1], order=DegLex)
        bc = Monom(vars=[1, 2], order=DegLex)

        # a < bc < ab
        self.assertTrue(DegLex.lt(a, ab))
        self.assertFalse(DegLex.lt(ab, a))

        self.assertTrue(DegLex.lt(a, bc))
        self.assertFalse(DegLex.lt(bc, a))

        self.assertTrue(DegLex.lt(bc, ab))
        self.assertFalse(DegLex.lt(ab, bc))

        abc = Monom(vars=[0, 1, 2])
        bcd = Monom(vars=[1, 2, 3])

        # bcd < abc
        self.assertTrue(DegLex.lt(bcd, abc))
        self.assertFalse(DegLex.lt(abc, bcd))

    def test_degrevlex(self):
        a, b, c, d = self.variables
        _1 = Monom.one
        _0 = Monom()

        # a < b < c < d
        self.assertFalse(DegRevLex.lt(b, a))
        self.assertFalse(DegRevLex.lt(c, b))
        self.assertFalse(DegRevLex.lt(d, c))
        self.assertFalse(DegRevLex.lt(d, a))

        self.assertFalse(Lex.lt(a, _1))  # a < 1
        self.assertTrue(Lex.lt(_1, a))  # 1 < a

        self.assertFalse(Lex.lt(a, _0))  # a > 0
        self.assertFalse(Lex.lt(_1, _0))  # 1 > 0

        self.assertTrue(Lex.lt(_0, a))  # 0 < a
        self.assertTrue(Lex.lt(_0, _1))  # 0 < 1

        ab = Monom(vars=[0, 1], order=DegRevLex)
        bc = Monom(vars=[1, 2], order=DegRevLex)

        # a < ab < bc
        self.assertFalse(DegRevLex.lt(ab, a))
        self.assertFalse(DegRevLex.lt(bc, a))
        self.assertFalse(DegRevLex.lt(bc, ab))

        abc = Monom(vars=[0, 1, 2])
        bcd = Monom(vars=[1, 2, 3])

        # abc < bcd
        self.assertFalse(DegRevLex.lt(bcd, abc))
        self.assertTrue(DegRevLex.lt(abc, bcd))
