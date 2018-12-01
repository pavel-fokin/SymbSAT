"""Boolean Monomials."""
import itertools
import operator

from symbsat.order import Lex


class Monom(tuple):

    size = 0
    zero = None
    one = None

    def __new__(cls, bits=None, vars=None, order=Lex):

        cls.order = order

        if bits is not None:
            return super(Monom, cls).__new__(cls, bits)
        if vars is not None:
            bits = list(itertools.repeat(0, Monom.size))
            for var in vars:
                bits[var] = 1
            return super(Monom, cls).__new__(cls, bits)
        return Monom.zero

    def __mul__(self, other):
        if self.is_one():
            return other
        if other.is_one():
            return self
        if self.is_zero() or other.is_zero():
            return Monom.zero

        return Monom(map(operator.or_, self, other), order=self.order)

    def __truediv__(self, other):
        if other.is_one():
            return self
        if self.is_one():
            return Monom.zero
        if self == other:
            return Monom.one
        if not self.isdivisible(other):
            return Monom.zero

        return Monom(map(operator.xor, self, other), order=self.order)

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

    def is_one(self):
        return id(self) == id(Monom.one)

    def is_zero(self):
        return id(self) == id(Monom.zero)

    def isdivisible(self, other):
        if other.is_one():
            return True
        if self.is_one():
            return False
        return self == Monom(map(operator.or_, self, other), order=self.order)

    def isrelativelyprime(self, other):
        if self == other:
            return True
        if self.is_one():
            return True
        lcm = self.lcm(other)
        return Monom(map(operator.xor, lcm, self), order=self.order) == other

    def prolong(self, i):
        """Prolongation of the monomial m*x."""
        assert not self[i]
        self[i] = 1

    @property
    def vars(self):
        """Return list of variables positions."""
        return [i for i, v in enumerate(self) if v == 1]

    @property
    def degree(self):
        return sum(self)


Monom.one = Monom(())
Monom.zero = Monom(())
