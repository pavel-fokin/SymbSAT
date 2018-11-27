# pylint: disable=invalid-name
"""Monomial order.

Implementing different monomial orderings, for our purpose
it is enough to implement '<' operation.
"""
import operator


class Order:
    @staticmethod
    def lt(first, second):
        raise NotImplementedError


class Lex(Order):
    @staticmethod
    def lt(first, second):
        if first.is_zero() or first.is_one():
            return True
        if second.is_zero() or second.is_one():
            return False

        vec = [
            var for var in map(operator.sub, first, second)
            if var != 0
        ]
        # the left-most nonzero entry of vector a - b is positive
        return len(vec) > 0 > vec[0]


class DegLex(Order):
    @staticmethod
    def lt(first, second):
        if first.is_zero() or first.is_one():
            return True
        if second.is_zero() or second.is_one():
            return False

        if first.degree < second.degree:
            return True
        if first.degree > second.degree:
            return False
        return Lex.lt(first, second)


class DegRevLex(Order):
    @staticmethod
    def lt(first, second):
        if first.is_zero() or first.is_one():
            return True
        if second.is_zero() or second.is_one():
            return False

        if first.degree < second.degree:
            return True
        if first.degree > second.degree:
            return False

        return not Lex.lt(first, second)
