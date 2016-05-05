"""
Boolean Polynomials
"""

import collections
import operator
import itertools

from monom import Monom


class Poly(list):

    one = None
    zero = None

    def __new__(cls, monoms):
        return super(Poly, cls).__new__(cls, monoms)

    def __init__(self, monoms):
        return super(Poly, self).__init__(sorted(monoms, reverse=True))

    def __add__(self, other):
        # symmetric difference
        if isinstance(other, Monom):
            return Poly(set(self) ^ set([other]))
        elif isinstance(other, Poly):
            return Poly(set(self) ^ set(other))
        else:
            return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Monom):
            if self == Poly.zero or other.isZero():
                return Poly.zero
            monoms = map(lambda m: m*other, self)
        elif isinstance(other, Poly):
            if self == Poly.zero or other == Poly.zero:
                return Poly.zero
            monoms = itertools.starmap(
                operator.mul,
                (itertools.product(self, other))
            )
        else:
            return NotImplemented

        counter = collections.Counter(monoms)
        return Poly({m for m, c in counter.items() if c % 2 != 0})

    def __str__(self):
        if self == Poly.zero:
            return "0"
        return " + ".join(map(str, sorted(self, reverse=True)))

    def lm(self):
        if self == Poly.zero:
            return Monom.zero
        return self[0]

    @staticmethod
    def S(f, g):
        """
        Return s-polynomial
        """
        f_lm, g_lm = f.lm(), g.lm()
        lcm = f_lm.lcm(g_lm)
        spoly = f*(lcm/f_lm) + g*(lcm/g_lm)
        return spoly

    def NF(self, F):
        """
        NormalForm w.r.t F
        D. Cox, J. Little, D. O'Shea - Ideals, Varieties, and Algorithms
        $3 A Division Algorithm
        """
        p = Poly(self)
        r = Poly.zero

        if F == []:
            return p

        while p != Poly.zero:
            i = 0
            divisionoccured = False
            while i < len(F) and (not divisionoccured):
                p_lm, fi_lm = p.lm(), F[i].lm()
                if p_lm.isdivisible(fi_lm):
                    p = p + F[i]*(p_lm/fi_lm)
                    divisionoccured = True
                else:
                    i += 1
            if not divisionoccured:
                r = r + p_lm
                p = p + p_lm

        return r

Poly.zero = Poly([])
Poly.one = Poly([Monom.one])
