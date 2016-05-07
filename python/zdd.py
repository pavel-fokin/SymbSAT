"""ZDDs
"""

from monom import Monom


class ZDD(object):

    _slots__ = ['root', '_cache', '_lm']

    class Node(object):

        __slots__ = ['var', 'mul', 'add']

        def __init__(self, var, m, a):
            self.var = var
            self.mul = m  # and
            self.add = a  # xor

        def isZero(self):
            return self.var == -2

        def isOne(self):
            return self.var == -1

        def __str__(self):
            if self == ZDD._one:
                return "_one"
            elif self == ZDD._zero:
                return "_zero"
            else:
                return "{} -> {} {}".format(str(self.var),
                                            str(self.mul),
                                            str(self.add))

        def __eq__(self, other):
            return id(self) == id(other)

    ring = None
    _one = Node(-1, None, None)
    _zero = Node(-2, None, None)

    def __init__(self, var=-1, monom=None):
        self._lm = None
        self._cache = {}

        if monom is not None:
            if monom.isOne():
                self.setOne()
            elif monom.isZero():
                self.setZero()
            else:
                self.root = self._create_node(
                    monom.vars[0], ZDD._one, ZDD._zero
                )
                root = self.root
                for var in monom.vars[1:]:
                    root.mul = self._create_node(var, ZDD._one, ZDD._zero)
                    root = root.mul
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

        r = None

        if (var, id(m), id(a)) in self._cache:
            r = self._cache[var, id(m), id(a)]
        else:
            r = ZDD.Node(var, m, a)
            self._cache[var, id(m), id(a)] = r

        return r

    def _add(self, i, j):

        if i.isZero():
            return j
        elif j.isZero():
            return i
        elif i == j:
            return ZDD._zero
        elif i.isOne():
            r = self._create_node(j.var, j.mul, self._add(j.add, ZDD._one))
        elif j.isOne():
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

        if i.isOne():
            return j
        elif i.isZero() or j.isZero():
            return ZDD._zero
        elif j.isOne() or i == j:
            return i
        else:
            r = None
            if i.var < j.var:
                m = self._mul(i.mul, j)
                a = self._mul(i.add, j)

                if m.isZero():
                    return a

                r = self._create_node(i.var, m, a)
            elif i.var > j.var:
                m = self._mul(j.mul, i)
                a = self._mul(j.add, i)

                if m.isZero():
                    return a

                r = self._create_node(j.var, m, a)
            else:
                m1 = self._mul(i.add, j.mul)
                m2 = self._mul(i.mul, j.mul)
                m3 = self._mul(i.mul, j.add)
                ms_sum = self._add(m1, self._add(m2, m3))

                if ms_sum.isZero():
                    return self._mul(i.add, j.add)

                r = self._create_node(i.var, ms_sum, self._mul(i.add, j.add))
            return r

    def __add__(self, other):

        if isinstance(other, Monom):
            return self + ZDD(monom=other)
        elif isinstance(other, ZDD):
            r = ZDD()
            r.root = self._add(self.root, other.root)
            r._cache = self._cache
            return r
        else:
            return NotImplemented

    def __mul__(self, other):

        if isinstance(other, Monom):
            return self * ZDD(monom=other)
        elif isinstance(other, ZDD):
            r = ZDD()
            r.root = self._mul(self.root, other.root)
            r._cache = self._cache
            return r
        else:
            return NotImplemented

    def copy(self):
        r = ZDD()
        r.root = self.root
        r._cache = self._cache
        return r

    def setZero(self):
        self.root = ZDD._zero

    def setOne(self):
        self.root = ZDD._one

    def isZero(self):
        return self.root.isZero()

    def isOne(self):
        return self.root.isOne()

    def lm(self):
        if self.root.isZero():
            return Monom.zero
        elif self.root.isOne():
            return Monom.one
        else:
            if self._lm is None:
                monom = []
                i = self.root
                while i.var >= 0:
                    monom.append(i.var)
                    i = i.mul
                self._lm = Monom(vars=monom)
            return self._lm

    def __iter__(self):
        if self.root.isZero():
            yield Monom.zero
        elif self.root.isOne():
            yield Monom.one
        else:
            monom, path = [], []
            i = self.root
            while i.var >= 0:
                monom.append(i.var)
                path.append(i)
                i = i.mul
            yield Monom(vars=monom)
            while path:
                while path and path[-1].add.isZero():
                    path.pop()
                    monom.pop()
                if path:
                    i = path.pop().add
                    monom.pop()
                    while i != ZDD._one:
                        monom.append(i.var)
                        path.append(i)
                        i = i.mul
                    yield Monom(vars=monom)

    def __str__(self):
        return " + ".join(map(str, self))
