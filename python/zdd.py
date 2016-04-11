"""ZDDs
"""


class ZDD(object):

    class Node(object):

        def __init__(self, var, m, a):
            self.var = var
            self.mul = m
            self.add = a

        def __eq__(self, other):
            return id(self) == id(other)

    _one = Node(-1, None, None)
    _zero = Node(-1, None, None)

    def __init__(self, var):
        self._cache = {}
        self.root = self._create_node(var, ZDD._one, ZDD._zero)

    def _create_node(self, var, m, a):
        r = None

        if (var, m.var, a.var) in self._cache:
            r = self._cache[var, m.var, a.var]
        else:
            r = ZDD.Node(var, m, a)
            self._cache[var, m.var, a.var] = r

        return r

    def _add(self, i, j):
        if i.var > j.var:
            r = self._create_node(i.var, i.mul, self._add(i.add, j))
        elif i.var < j.var:
            r = self._create_node(j.var, j.mul, self._add(j.add, i))
        elif i.var < 0:
            r = ZDD._zero if i == j else ZDD._one
        else:
            m, a = self._add(i.mul, j.mul), self._add(i.add, j.add)
            r = a if m == ZDD._zero else ZDD._create_node(i.var, m, add)
        return r

    def _mul(self, i, j):
        if i.var > j.var:
            m, a = self._mul(i.mul, j), self._mul(i.add, j.var)
            r = a if m == ZDD._zero else self._create_node(i.var, m, a)
        elif i.var == j.var:
            m = self._add(i.mul, i.add)
            r = ZDD._zero if m == ZDD.__zero else self._create_node(j.var, m, ZDD._zero)
        elif i.var >= 0:
            r = self._create_node(j.var, i, ZDD._zero)
        else:
            r = ZDD._zero if i == ZDD._zero else self._create_node(j.var, ZDD._one, ZDD._zero)
        return r

    def __add__(self, other):
        r = ZDD(-1)
        r.root = self._add(self.root, other.root)
        r._cache = self._cache.copy()
        return r

    def __mul__(self, other):
        r = ZDD(-1)
        r.root = self._mul(self.root, other.root)
        r._cache = self._cache.copy()
        return r

    def lm(self):
        return next(iter(self))

    def __iter__(self):
        if self.root == ZDD._zero:
            yield None
        elif self.root == ZDD._one:
            yield []
        else:
            i, p = self.root, []
            while i != ZDD._one:
                p.append([i, True])
                i = i.mul
            yield [j.var for j, a in p]
            while True:
                while p[-1][0].add == ZDD._zero or not p[-1][1]:
                    del p[-1]
                    if not p:
                        return
                p[-1][1] = False
                i = p[-1][0].add
                while i != ZDD._one:
                    p.append([i, True])
                    i = i.mul
                yield [j.var for j, a in p if a]
