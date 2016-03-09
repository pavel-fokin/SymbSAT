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
        return super().__new__(cls, monoms)

    def __init__(self, monoms):
        return super().__init__(sorted(monoms, reverse=True))

    def __add__(self, other):
        # difference_symetric
        return Poly(set(self) ^ set(other))

    def __mul__(self, other):
        # if self == Poly.one:
            # return other
        # if other == Poly.one:
            # return self
        if self == Poly.zero or other == Poly.zero:
            return Poly.zero
        m = itertools.starmap(operator.mul, (itertools.product(self, other)))
        counter = collections.Counter(m)
        return Poly({m for m, c in counter.items() if c % 2 != 0})

    def __str__(self):
        if self == Poly.zero:
            return "0"
        return " + ".join(map(str, sorted(self, reverse=True)))

    def lt(self):
        if self == Poly.zero:
            return Monom.zero
        return self[0]

    @staticmethod
    def S(f, g):
        """
        Return s-polynomial
        """
        f_lt, g_lt = f.lt(), g.lt()
        lcm = f_lt.lcm(g_lt)
        spoly = f*Poly([lcm/f_lt]) + g*Poly([lcm/g_lt])
        return spoly

    @staticmethod
    def NFHead(p, F):
        raise NotImplemented

    @staticmethod
    def NFTail(self, F):
        raise NotImplemented

    def NF(self, F):
        """
        NormalForm w.r.t F
        D. Cox, J. Little, D. O'Shea - Ideals, Varieties, and Algorithms
        $3 A Division Algorithm
        """
        p = Poly(self.copy())
        r = Poly.zero

        if F == []:
            return r

        while p != Poly.zero:
            i = 0
            divisionoccured = False
            while i < len(F) and divisionoccured == False:
                p_lm, fi_lm = p.lt(), F[i].lt()
                if p_lm.isdivisible(fi_lm):
                    p = p + F[i]*Poly([p_lm/fi_lm])
                    divisionoccured = True
                else:
                    i += 1
            if divisionoccured == False:
                r = r + Poly([p_lm])
                p = p + Poly([p_lm])

        return r

Poly.zero = Poly([])
Poly.one = Poly([Monom.one])


def generate_n_vars(variables):
    """
    Generate `n` vars as `n` univariate polynomials
    """
    Monom.variables = variables
    n = len(variables)

    vars = list(itertools.repeat(None, n))

    for i in range(n):
        bin_var = list(itertools.repeat(0, n))
        bin_var[i] = 1
        vars[i] = Poly([Monom(bin_var)])

    return vars
