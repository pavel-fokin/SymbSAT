"""
Boolean Monom
"""

import itertools
import operator


class Monom(tuple):

    size = 0
    zero = None
    one = None

    def __new__(cls, bits=None, vars=None):
        if bits is not None:
            return super(Monom, cls).__new__(cls, bits)
        elif vars is not None:
            bits = list(itertools.repeat(0, Monom.size))
            for var in vars:
                bits[var] = 1
            return super(Monom, cls).__new__(cls, bits)
        else:
            return Monom.zero

    def __mul__(self, other):
        if self.isOne():
            return other
        if other.isOne():
            return self
        if self.isZero() or other.isZero():
            return Monom.zero

        return Monom(map(operator.or_, self, other))

    def __truediv__(self, other):
        if other.isOne():
            return self
        if self.isOne():
            return Monom.zero
        if self == other:
            return Monom.one
        if not self.isdivisible(other):
            return Monom.zero

        return Monom(map(operator.xor, self, other))

    __div__ = __truediv__

    def __str__(self):
        if self.isOne():
            return "1"
        if self.isZero():
            return "0"
        return str(self.vars)

    def pprint(self, alphabet, op=""):
        return op.join(l for v, l in zip(self, alphabet) if v == 1)

    def lcm(self, other):
        return self*other

    def isOne(self):
        return id(self) == id(Monom.one)

    def isZero(self):
        return id(self) == id(Monom.zero)

    def isdivisible(self, other):
        if other.isOne():
            return True
        if self.isOne():
            return False
        return self == Monom(map(operator.or_, self, other))

    def isrelativelyprime(self, other):
        if self == other:
            return True
        if self.isOne():
            return True
        lcm = self.lcm(other)
        return Monom(map(operator.xor, lcm, self)) == other

    def prolong(self, i):
        """Prolongation of the monomial m*x
        """
        assert(not self[i])
        self[i] = 1

    @property
    def vars(self):
        """Return list of variables positions
        """
        return [i for i, v in enumerate(self) if v == 1]

    @property
    def degree(self):
        return sum(self)

    def lex(self, other):
        raise NotImplemented

    def deglex(self, other):
        raise NotImplemented


Monom.one = Monom(())
Monom.zero = Monom(())
