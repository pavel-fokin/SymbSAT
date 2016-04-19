"""
Boolean Monom
"""

import operator


class Monom(tuple):

    variables = []
    zero = None
    one = None

    def __new__(cls, it):
        return super().__new__(cls, it)

    def __mul__(self, other):
        if self == Monom.one:
            return other
        if other == Monom.one:
            return self
        if self == Monom.zero or other == Monom.zero:
            return Monom.zero

        assert len(self) == len(other)

        return Monom(map(operator.or_, self, other))

    def __truediv__(self, other):
        if other == Monom.one:
            return self
        if self == Monom.one:
            return Monom.zero
        if self == other:
            return Monom.one
        if not self.isdivisible(other):
            return Monom.zero

        return Monom(map(operator.xor, self, other))

    __div__ = __truediv__

    def __str__(self):
        if self == Monom.one:
            return "1"
        if self == Monom.zero:
            return "0"
        return "".join(l for v, l in zip(self, self.variables) if v == 1)

    def lcm(self, other):
        return self*other

    def isdivisible(self, other):
        if other == Monom.one:
            return True
        if self == Monom.one:
            return False
        return self == Monom(map(operator.or_, self, other))

    def isrelativelyprime(self, other):
        if self == other:
            return True
        if self == Monom.one:
            return True
        lcm = self.lcm(other)
        return Monom(map(operator.xor, lcm, self)) == other

    def prolong(i):
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


Monom.one = Monom((-1,))
Monom.zero = Monom(())
