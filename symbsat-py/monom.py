"""Boolean Monomials."""
import itertools
import operator
from functools import partialmethod

from order import Lex


class Monom:

    def __init__(self, size, bits=None, vars=None, order=Lex):
        self.size = size
        self.order = order
        if bits is not None:
            self.bits = tuple(bits)
        elif vars is not None:
            bits = [0] * size
            for var in vars:
                bits[var] = 1
            self.bits = tuple(bits)
        else:
            self.bits = tuple()

    @classmethod
    def zero(cls):
        super(cls).__init__()
        return cls(size=0, bits=tuple())

    @classmethod
    def one(cls):
        return cls(size=1, bits=(0,))

    def is_zero(self):
        return self.bits == ()

    def is_one(self):
        return self.bits == (0,)

    def __mul__(self, other):
        if self.is_one():
            return other
        if other.is_one():
            return self
        if self.is_zero():
            return Monom.zero()
        if other.is_zero():
            return Monom.zero()

        return Monom(
            size=self.size,
            bits=map(operator.or_, self.bits, other.bits),
            order=self.order
        )

    def __truediv__(self, other):
        if other.is_one():
            return self
        if self.is_one():
            return Monom.zero()
        if self == other:
            return Monom.one()
        if not self.isdivisible(other):
            return Monom.zero()

        return Monom(
            size=self.size,
            bits=map(operator.xor, self.bits, other.bits),
            order=self.order
        )

    def __hash__(self):
        return hash(self.bits)

    def __eq__(self, other):
        return self.bits == other.bits

    def __lt__(self, other):
        return self.order.lt(self, other)

    def __le__(self, other):
        return NotImplemented

    def __gt__(self, other):
        return not self.order.lt(self, other)

    def __ge__(self, other):
        return NotImplemented

    def __str__(self):
        if self.is_one():
            return "1"
        if self.is_zero():
            return "0"
        return str(self.vars)

    def pprint(self, alphabet, op=""):
        return op.join(l for v, l in zip(self, alphabet) if v == 1)

    def lcm(self, other):
        return self*other

    def isdivisible(self, other):
        if other.is_one():
            return True
        if self.is_one():
            return False
        return self == Monom(
            size=self.size,
            bits=map(operator.or_, self.bits, other.bits),
            order=self.order
        )

    def isrelativelyprime(self, other):
        if self == other:
            return True
        if self.is_one():
            return True
        lcm = self.lcm(other)
        return Monom(
            size=self.size,
            bits=map(operator.xor, lcm.bits, self.bits),
            order=self.order
        ) == other

    def prolong(self, i):
        """Prolongation of the monomial m*x."""
        assert not self[i]
        self[i] = 1

    @property
    def vars(self):
        """Return list of variables positions."""
        return [i for i, v in enumerate(self.bits) if v == 1]

    @property
    def degree(self):
        return sum(self.bits)


def make_monom_type(size):

    class _Monom(Monom):
        __init__ = partialmethod(Monom.__init__, size)

        @classmethod
        def zero(cls):
            return cls(bits=tuple())

        @classmethod
        def one(cls):
            return cls(bits=(0,))
    return _Monom

Monom4 = make_monom_type(4)
