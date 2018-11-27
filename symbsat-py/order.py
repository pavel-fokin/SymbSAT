# pylint: disable=invalid-name
"""Monomial order.

Implementing different monomial orderings, for our purpose
it is enough to implement '<' operation.
"""
import operator


class Order:

    @classmethod
    def lex_condition(cls, first, second):
        vec = [
            var for var in map(operator.sub, first, second)
            if var != 0
        ]
        # the left-most nonzero entry of vector a - b is positive
        return len(vec) > 0 > vec[0]

    @classmethod
    def lt(cls, first, second):
        raise NotImplementedError


class Lex(Order):
    @classmethod
    def lt(cls, first, second):
        if first.is_zero():
            return True
        if second.is_zero():
            return False

        if first.is_one():
            return True
        if second.is_one():
            return False

        return cls.lex_condition(first, second)


class DegLex(Order):
    @classmethod
    def lt(cls, first, second):
        if first.is_zero():
            return True
        if second.is_zero():
            return False

        if first.is_one():
            return True
        if second.is_one():
            return False

        if first.degree < second.degree:
            return True
        if first.degree > second.degree:
            return False

        return cls.lex_condition(first, second)


class DegRevLex(Order):
    @classmethod
    def lt(cls, first, second):
        if first.is_zero():
            return True
        if second.is_zero():
            return False

        if first.is_one():
            return True
        if second.is_one():
            return False

        if first.degree < second.degree:
            return True
        if first.degree > second.degree:
            return False

        return not cls.lex_condition(first, second)
