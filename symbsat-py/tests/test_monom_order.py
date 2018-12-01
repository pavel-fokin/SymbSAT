# pylint: disable=invalid-name
import unittest

from monom import Monom
from order import Lex, DegLex, DegRevLex


class TestBoolMonomOrder(unittest.TestCase):

    def setUp(self):
        Monom.size = 4

    def test_base_rules(self):
        a, b = (
            Monom(vars=[0], order=Lex),  # a
            Monom(vars=[1], order=Lex),  # b
        )

        with self.assertRaises(TypeError):
            a <= b

        with self.assertRaises(TypeError):
            a >= b

    def test_lex(self):
        a, b, c, d = (
            Monom(vars=[0], order=Lex),  # a
            Monom(vars=[1], order=Lex),  # b
            Monom(vars=[2], order=Lex),  # c
            Monom(vars=[3], order=Lex),  # d
        )

        # a > b > c > d
        self.assertTrue(a > b)
        self.assertTrue(b < a)

        self.assertTrue(b > c)
        self.assertTrue(c < b)

        self.assertTrue(c > d)
        self.assertTrue(d < c)

        self.assertTrue(a > d)
        self.assertTrue(d < a)

        _1 = Monom.one
        _0 = Monom()

        self.assertTrue(a > _1)
        self.assertTrue(_1 < a)

        self.assertTrue(_0 < _1)
        self.assertTrue(_0 < a)

        self.assertTrue(_1 > _0)
        self.assertTrue(a > _0)

        ab = Monom(vars=[0, 1], order=Lex)
        bc = Monom(vars=[1, 2], order=Lex)

        # bc < a < ab
        self.assertTrue(a < ab)
        self.assertTrue(bc < a)
        self.assertTrue(bc < ab)

        abc = Monom(vars=[0, 1, 2], order=Lex)
        bcd = Monom(vars=[1, 2, 3], order=Lex)

        self.assertTrue(bcd < abc)
        self.assertTrue(abc > bcd)

    def test_deglex(self):
        a, b, c, d = (
            Monom(vars=[0], order=DegLex),  # a
            Monom(vars=[1], order=DegLex),  # b
            Monom(vars=[2], order=DegLex),  # c
            Monom(vars=[3], order=DegLex),  # d
        )

        # a < b < c < d
        self.assertTrue(a > b)
        self.assertTrue(b < a)

        self.assertTrue(b > c)
        self.assertTrue(c < b)

        self.assertTrue(c > d)
        self.assertTrue(d < c)

        self.assertTrue(a > d)
        self.assertTrue(d < a)

        _1 = Monom.one
        _0 = Monom()

        self.assertTrue(a > _1)
        self.assertTrue(_1 < a)

        self.assertTrue(_0 < _1)
        self.assertTrue(_0 < a)

        self.assertTrue(_1 > _0)
        self.assertTrue(a > _0)

        ab = Monom(vars=[0, 1], order=DegLex)
        bc = Monom(vars=[1, 2], order=DegLex)

        # a < bc < ab
        self.assertTrue(a < ab)
        self.assertTrue(a < bc)
        self.assertTrue(bc < ab)

        abc = Monom(vars=[0, 1, 2], order=DegLex)
        bcd = Monom(vars=[1, 2, 3], order=DegLex)

        # bcd < abc
        self.assertTrue(bcd < abc)
        self.assertTrue(abc > bcd)

    def test_degrevlex(self):
        a, b, c, d = (
            Monom(vars=[0], order=DegRevLex),  # a
            Monom(vars=[1], order=DegRevLex),  # b
            Monom(vars=[2], order=DegRevLex),  # c
            Monom(vars=[3], order=DegRevLex),  # d
        )

        self.assertTrue(a < b)
        self.assertTrue(b > a)

        self.assertTrue(b < c)
        self.assertTrue(c > b)

        self.assertTrue(c < d)
        self.assertTrue(d > c)

        self.assertTrue(a < d)
        self.assertTrue(d > a)

        _1 = Monom.one
        _0 = Monom()

        self.assertTrue(a > _1)
        self.assertTrue(_1 < a)

        self.assertTrue(_0 < _1)
        self.assertTrue(_0 < a)

        self.assertTrue(_1 > _0)
        self.assertTrue(a > _0)

        ab = Monom(vars=[0, 1], order=DegRevLex)
        bc = Monom(vars=[1, 2], order=DegRevLex)

        # a < bc < ab
        self.assertTrue(a < ab)
        self.assertTrue(a < bc)
        self.assertTrue(ab < bc)

        abc = Monom(vars=[0, 1, 2], order=DegRevLex)
        bcd = Monom(vars=[1, 2, 3], order=DegRevLex)

        # abc < bcd
        self.assertTrue(bcd > abc)
        self.assertTrue(abc < bcd)
