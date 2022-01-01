from .node import Node


class ZDD:

    def __init__(self, var=-1):
        if var < 0:
            self.root = Node.zero()
        else:
            self.root = self.create_node(
                var, Node.one(), Node.zero()
            )

    def create_node(self, var: int, m: Node, a: Node):
        return Node(var, m, a)

    @classmethod
    def zero(cls):
        return cls()

    @classmethod
    def one(cls):
        zdd = cls()
        zdd.root = Node.one()
        return zdd

    def _add(self, i, j):

        if i.is_zero():
            return j
        if j.is_zero():
            return i
        if i == j:
            return self.zero()

        if i.is_one():
            r = self.create_node(
                j.var, j.mul, self._add(j.add, Node.one())
            )
        elif j.is_one():
            r = self.create_node(
                i.var, i.mul, self._add(i.add, Node.one())
            )
        else:
            if i.var < j.var:
                r = self.create_node(i.var, i.mul, self._add(i.add, j))
            elif i.var > j.var:
                r = self.create_node(j.var, j.mul, self._add(i, j.add))
            else:
                m = self._add(i.mul, j.mul)
                a = self._add(i.add, j.add)

                if m.is_zero():
                    return a

                r = self.create_node(i.var, m, a)
        return r

    def _mul(self, i, j):

        if i.is_one():
            return j
        if i.is_zero() or j.is_zero():
            return Node.zero()
        if j.is_one() or i == j:
            return i

        r = None
        if i.var < j.var:
            m = self._mul(i.mul, j)
            a = self._mul(i.add, j)

            if m.is_zero():
                return a

            r = self.create_node(i.var, m, a)
        elif i.var > j.var:
            m = self._mul(j.mul, i)
            a = self._mul(j.add, i)

            if m.is_zero():
                return a

            r = self.create_node(j.var, m, a)
        else:
            m1 = self._mul(i.add, j.mul)
            m2 = self._mul(i.mul, j.mul)
            m3 = self._mul(i.mul, j.add)
            ms_sum = self._add(m1, self._add(m2, m3))

            if ms_sum.is_zero():
                return self._mul(i.add, j.add)

            r = self.create_node(i.var, ms_sum, self._mul(i.add, j.add))
        return r

    def __mul__(self, other):
        self_cls = type(self)
        zdd = self_cls()
        zdd.root = zdd._mul(self.root, other.root)
        return zdd

    def __add__(self, other):
        self_cls = type(self)
        zdd = self_cls()
        zdd.root = zdd._add(self.root, other.root)
        return zdd

