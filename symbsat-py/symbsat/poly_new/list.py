import collections
import itertools
import operator

from symbsat.monom import Monom

from .base import Poly


class PolyList(Poly):

    def _init_monoms(self, monoms):
        self._list = sorted(monoms, reverse=True)

    def _init_var(self, var):
        self._list = [Monom(vars=[var])]

    def _init_monom(self, monom):
        self._list = [monom]

    @classmethod
    def make_zero(cls):
        raise NotImplementedError

    @classmethod
    def make_one(cls):
        raise NotImplementedError

    def __add__(self, other):
        # symmetric difference
        if isinstance(other, Monom):
            return PolyList(monoms=list(set(self) ^ set([other])))
        if isinstance(other, PolyList):
            return PolyList(monoms=list(set(self) ^ set(other)))
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Monom):
            if self.is_zero() or other.is_zero():
                return PolyList.make_zero()
            monoms = map(lambda m: m*other, self)
        elif isinstance(other, PolyList):
            if self.is_zero() or other.is_zero():
                return PolyList.make_zero()
            monoms = itertools.starmap(
                operator.mul,
                (itertools.product(self, other))
            )
        else:
            return NotImplemented

        counter = collections.Counter(monoms)
        return PolyList(monoms={m for m, c in counter.items() if c % 2 != 0})

    def __str__(self):
        raise NotImplementedError

    def copy(self):
        raise NotImplementedError

    def is_zero(self):
        raise NotImplementedError

    def is_one(self):
        raise NotImplementedError

    def lm(self):
        raise NotImplementedError
