from symbsat.zdd_new import ZDD
from .base import Poly


class PolyZDD(Poly):

    @classmethod
    def make_zero(cls):
        raise NotImplementedError

    @classmethod
    def make_one(cls):
        raise NotImplementedError

    def _init_var(self, var: int):
        self._zdd = ZDD(var)

    def _init_monom(self, monom):
        if monom.is_zero():
            self._zdd = ZDD.zero()
        elif monom.is_one():
            self._zdd = ZDD.one()
        else:
            self._zdd = ZDD(monom.vars[0])
            for var in monom.vars[1:]:
                self._zdd *= ZDD(var)

    def _init_monoms(self, monoms):
        raise NotImplementedError

    def __add__(self, other):
        raise NotImplementedError

    def __mul__(self, other):
        raise NotImplementedError

    def __imul__(self, other):
        raise NotImplementedError

    def __str__(self):
        raise NotImplementedError

    def copy(self):
        raise NotImplementedError

    def is_zero(self):
        raise NotImplementedError

    def is_one(self):
        raise NotImplementedError

    def lm(self):
        raise NotImplementedError
