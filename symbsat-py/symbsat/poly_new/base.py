import abc


class Poly(metaclass=abc.ABCMeta):
    """Base class for boolean polynomials."""

    def __init__(self, *, monoms=None, var=None, monom=None):
        is_monoms = monoms is not None
        is_var = var is not None
        is_monom = monom is not None

        # It should verify that we have only one parameter
        if (is_monoms or is_var) ^ is_monom:
            raise RuntimeError("Only one initialization parameter is allowed")

        if is_monoms:
            self._init_monoms(monoms)
        elif is_var:
            self._init_var(var)
        elif is_monom:
            self._init_monom(monom)
        else:
            raise NotImplementedError

    @abc.abstractclassmethod
    def make_zero(cls):
        raise NotImplementedError

    @abc.abstractclassmethod
    def make_one(cls):
        raise NotImplementedError

    @abc.abstractmethod
    def _init_monoms(self, monoms):
        raise NotImplementedError

    @abc.abstractmethod
    def _init_var(self, var):
        raise NotImplementedError

    @abc.abstractmethod
    def _init_monom(self, monom):
        raise NotImplementedError

    @abc.abstractmethod
    def __add__(self, other):
        raise NotImplementedError

    @abc.abstractmethod
    def __mul__(self, other):
        raise NotImplementedError

    @abc.abstractmethod
    def __str__(self):
        raise NotImplementedError

    @abc.abstractmethod
    def copy(self):
        raise NotImplementedError

    @abc.abstractmethod
    def is_zero(self):
        raise NotImplementedError

    @abc.abstractmethod
    def is_one(self):
        raise NotImplementedError

    @abc.abstractmethod
    def lm(self):
        raise NotImplementedError
