import os
import tempfile

import unittest

import dimacs
from ring import BoolPolyRing


DIMACS_1 = b"""
c Example 2.2.2
p cnf 4 2
1 -2 0
-3 4 0
"""

DIMACS_2 = b"""
c Example 2.2.6
p cnf 3 4
-1 -2 3 0
-1 2 -3 0
1 -2 -3 0
1 2 3 0
"""

dimacs_marg2x2 = b"""
c marg2x2
p cnf 12 32
8 12 6 0
7 -2 9 0
8 -12 -6 0
-8 12 -6 0
6 -11 -7 0
-10 1 -3 0
11 7 6 0
11 -7 -6 0
-3 -12 -5 0
3 -10 -1 0
-12 -8 6 0
-2 -7 -9 0
-9 7 2 0
-6 7 -11 0
12 -3 5 0
-1 -3 10 0
-5 -4 11 0
5 4 11 0
8 -9 -10 0
1 -4 2 0
9 8 10 0
12 -5 3 0
5 3 -12 0
-10 9 -8 0
10 1 3 0
9 -7 2 0
-5 4 -11 0
2 -1 4 0
-4 -11 5 0
4 -2 1 0
-8 10 -9 0
-1 -2 -4 0
"""


class TestDIMACS:

    def test_load_dimacs_1(self):

        with tempfile.NamedTemporaryFile(delete=False) as dimacs_file:
            dimacs_file.write(DIMACS_1)

        P, B = dimacs.load(dimacs_file.name, poly_type=self.poly_type)
        os.remove(dimacs_file.name)

        x1, x2, x3, x4 = B.gens

        self.assertTrue(len(P) == 2)
        self.assertTrue(P[0] == x1*x2 + x1)
        self.assertTrue(P[1] == x3*x4 + x4)

    def test_load_dimacs_2(self):

        with tempfile.NamedTemporaryFile(delete=False) as dimacs_file:
            dimacs_file.write(DIMACS_2)

        P, B = dimacs.load(dimacs_file.name, poly_type=self.poly_type)
        os.remove(dimacs_file.name)

        x1, x2, x3 = B.gens
        self.assertTrue(len(P) == 4)
        self.assertTrue(P[0] == x1*x2*x3 + x1*x3 + x2*x3 + x3)
        self.assertTrue(P[1] == x1*x2*x3 + x1*x2 + x2*x3 + x2)
        self.assertTrue(P[2] == x1*x2*x3 + x1*x2 + x1*x3 + x1)
        self.assertTrue(P[3] == x1*x2*x3)

    def test_load_marg2x2(self):

        with tempfile.NamedTemporaryFile(delete=False) as dimacs_file:
            dimacs_file.write(dimacs_marg2x2)

        P, B = dimacs.load(dimacs_file.name, poly_type=self.poly_type)
        os.remove(dimacs_file.name)

        x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12 = B.gens
        self.assertTrue(P[0] == x6*x8*x12)
        self.assertTrue(P[1] == x2*x7*x9 + x7*x9)
        self.assertTrue(P[2] == x6*x8*x12 + x6*x8 + x8*x12 + x8)
        self.assertTrue(P[3] == x6*x8*x12 + x6*x12 + x8*x12 + x12)
        self.assertTrue(P[4] == x6*x7*x11 + x6*x7 + x6*x11 + x6)


class TestDIMACSPolyZDD(unittest.TestCase, TestDIMACS):

    def setUp(self):
        self.poly_type = 'zdd'
        self.B = BoolPolyRing(10, poly_type=self.poly_type)


class TestDIMACSPolyLIST(unittest.TestCase, TestDIMACS):

    def setUp(self):
        self.poly_type = 'list'
        self.B = BoolPolyRing(10, poly_type=self.poly_type)
