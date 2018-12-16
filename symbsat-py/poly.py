"""Boolean Polynomials."""

import collections
import operator
import itertools

from monom import Monom


class Poly(list):

    ring = None
    one = None
    zero = None

    def __new__(cls, monoms):
        return super(Poly, cls).__new__(cls, monoms)

    def __init__(self, monoms):
        super(Poly, self).__init__(sorted(monoms, reverse=True))

    def __add__(self, other):
        # symmetric difference
        if isinstance(other, Monom):
            return Poly(set(self) ^ set([other]))
        if isinstance(other, Poly):
            return Poly(set(self) ^ set(other))
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Monom):
            if self.is_zero() or other.is_zero():
                return Poly.zero
            monoms = map(lambda m: m*other, self)
        elif isinstance(other, Poly):
            if self.is_zero() or other.is_zero():
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
        if self.is_zero():
            return "0"
        return " + ".join(map(str, sorted(self, reverse=True)))

    def copy(self):
        return Poly(self)

    def is_zero(self):
        #  return self == Poly.zero
        return self == []

    def is_one(self):
        #  return self == Poly.one
        return len(self) == 1 and self[0].is_one()

    def lm(self):
        if self == Poly.zero:
            return Monom.zero()
        return self[0]


Poly.zero = Poly([])
Poly.one = Poly([Monom.one()])
