class Node:

    __slots__ = ('var', 'mul', 'add')

    def __init__(self, var, m, a):
        if m and m.is_zero():
            raise TypeError('Multiply branch cannot be zero')

        self.var = var
        self.mul = m  # and
        self.add = a  # xor

    @classmethod
    def zero(cls):
        return cls(-2, None, None)

    @classmethod
    def one(cls):
        return cls(-1, None, None)

    def copy(self):
        if self.var < 0:
            return self
        return Node(
            self.var,
            self.mul.copy(),
            self.add.copy()
        )

    def is_zero(self):
        return self.var == -2

    def is_one(self):
        return self.var == -1

    def __str__(self):
        if self.is_one():
            return "_one"
        if self.is_zero():
            return "_zero"

        return (
            '%s -> {%s} {%s}' %
            (self.var, self.mul, self.add)
        )

    def __eq__(self, other):
        return id(self) == id(other)
