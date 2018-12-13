from .base import Poly


class PolyZDD(Poly):

    @classmethod
    def make_zero(cls):
        raise NotImplementedError

    @classmethod
    def make_one(cls):
        raise NotImplementedError

    def _init_monoms(self, monoms):
        raise NotImplementedError

    def _init_var(self, var):
        raise NotImplementedError

    def _init_monom(self, monom):
        raise NotImplementedError

    def __add__(self, other):
        raise NotImplementedError

    def __mul__(self, other):
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
