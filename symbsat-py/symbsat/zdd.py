"""ZDDs."""
from functools import partialmethod

from symbsat.monom import Monom


class ZDD:

    __slots__ = ('monom_type', 'root', '_lm')

    class Node:

        __slots__ = ('var', 'mul', 'add')

        def __init__(self, var, m, a):
            self.var = var
            self.mul = m  # and
            self.add = a  # xor

        def copy(self):
            if self.var < 0:
                return self
            return ZDD.Node(
                self.var,
                self.mul.copy(),
                self.add.copy()
            )

        def is_zero(self):
            return self.var == -2

        def is_one(self):
            return self.var == -1

        def __str__(self):
            if self == ZDD._one:
                return "_one"
            if self == ZDD._zero:
                return "_zero"

            return (
                '%s -> {%s} {%s}' %
                (self.var, self.mul, self.add)
            )

        def __eq__(self, other):
            return id(self) == id(other)

    ring = None
    _one = Node(-1, None, None)
    _zero = Node(-2, None, None)

    def __init__(self, monom_type, var=-1, monom=None):
        self.monom_type = monom_type
        self._lm = None

        if monom is not None:
            if monom.is_one():
                self.setOne()
            elif monom.is_zero():
                self.setZero()
            else:
                self.root = self._create_node(
                    monom.vars[0], ZDD._one, ZDD._zero
                )
                for var_ in monom.vars[1:]:
                    self.root = self._mul(
                        self.root, self._create_node(var_, ZDD._one, ZDD._zero)
                    )
        elif var < 0:
            self.root = ZDD._zero
        else:
            self.root = self._create_node(var, ZDD._one, ZDD._zero)

    def __eq__(self, other):
        """Compare two ZDDs as their representation
        as the list of monomials in lex order
        """
        return list(self) == list(other)

    def _create_node(self, var, m, a):
        assert m != ZDD._zero

        return ZDD.Node(var, m, a)

    def _add(self, i, j):

        if i.is_zero():
            return j
        if j.is_zero():
            return i
        if i == j:
            return ZDD._zero

        if i.is_one():
            r = self._create_node(j.var, j.mul, self._add(j.add, ZDD._one))
        elif j.is_one():
            r = self._create_node(i.var, i.mul, self._add(i.add, ZDD._one))
        else:
            if i.var < j.var:
                r = self._create_node(i.var, i.mul, self._add(i.add, j))
            elif i.var > j.var:
                r = self._create_node(j.var, j.mul, self._add(i, j.add))
            else:
                m = self._add(i.mul, j.mul)
                a = self._add(i.add, j.add)

                if m == ZDD._zero:
                    return a

                r = self._create_node(i.var, m, a)
        return r

    def _mul(self, i, j):

        if i.is_one():
            return j
        if i.is_zero() or j.is_zero():
            return ZDD._zero
        if j.is_one() or i == j:
            return i

        r = None
        if i.var < j.var:
            m = self._mul(i.mul, j)
            a = self._mul(i.add, j)

            if m.is_zero():
                return a

            r = self._create_node(i.var, m, a)
        elif i.var > j.var:
            m = self._mul(j.mul, i)
            a = self._mul(j.add, i)

            if m.is_zero():
                return a

            r = self._create_node(j.var, m, a)
        else:
            m1 = self._mul(i.add, j.mul)
            m2 = self._mul(i.mul, j.mul)
            m3 = self._mul(i.mul, j.add)
            ms_sum = self._add(m1, self._add(m2, m3))

            if ms_sum.is_zero():
                return self._mul(i.add, j.add)

            r = self._create_node(i.var, ms_sum, self._mul(i.add, j.add))
        return r

    def __add__(self, other):

        if isinstance(other, Monom):
            return self + ZDD(self.monom_type, monom=other)
        if isinstance(other, ZDD):
            r = ZDD(self.monom_type)
            r.root = self._add(self.root, other.root)
            return r
        return NotImplemented

    def __mul__(self, other):

        if isinstance(other, Monom):
            return self * ZDD(self.monom_type, monom=other)
        if isinstance(other, ZDD):
            r = ZDD(self.monom_type)
            r.root = self._mul(self.root, other.root)
            return r

        return NotImplemented

    def copy(self):
        r = ZDD(self.monom_type)
        r.root = self.root.copy()
        r._lm = self._lm
        return r

    def zero(self):
        zdd_zero = ZDD(self.monom_type)
        zdd_zero.setZero()
        return zdd_zero

    def one(self):
        zdd_one = ZDD(self.monom_type)
        zdd_one.setOne()
        return zdd_one

    def setZero(self):
        self.root = ZDD._zero

    def setOne(self):
        self.root = ZDD._one

    def is_zero(self):
        return self.root.is_zero()

    def is_one(self):
        return self.root.is_one()

    def lm(self):
        if self.root.is_zero():
            return self.monom_type.zero()
        if self.root.is_one():
            return self.monom_type.one()

        if self._lm is None:
            monom = []
            i = self.root
            while i.var >= 0:
                monom.append(i.var)
                i = i.mul
            #  self._lm = Monom(vars=monom)
            self._lm = self.monom_type(vars=monom)
        return self._lm

    def __iter__(self):
        if self.root.is_zero():
            yield self.monom_type.zero()
        elif self.root.is_one():
            yield self.monom_type.one()
        else:
            monom, path = [], []
            i = self.root
            while i.var >= 0:
                monom.append(i.var)
                path.append(i)
                i = i.mul
            #  yield Monom(vars=monom)
            yield self.monom_type(vars=monom)
            while path:
                while path and path[-1].add.is_zero():
                    path.pop()
                    monom.pop()
                if path:
                    i = path.pop().add
                    monom.pop()
                    while i != ZDD._one:
                        monom.append(i.var)
                        path.append(i)
                        i = i.mul
                    if monom == []:
                        yield self.monom_type.one()
                        break
                    #  yield Monom(vars=monom)
                    yield self.monom_type(vars=monom)

    def __str__(self):
        return " + ".join(map(str, self))


def make_zdd_type(monom_type):
    class _ZDD(ZDD):
        __init__ = partialmethod(ZDD.__init__, monom_type)

    return _ZDD
