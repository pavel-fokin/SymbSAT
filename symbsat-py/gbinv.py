"""
Compute Involutive Groebner Basis
"""


def nmulti_vars(m):
    """Pommaret Non-Multiplicative Variables
    """
    for i, bit in enumerate(reversed(m)):
        if bit == 1:
            return range(len(m) - i, len(m) + 1)


def multi_vars(m):
    """Pommaret Multiplicative Variables
    """
    vars_multi = []
    for i, bit in enumerate(m):
        if bit == 1:
            return vars_multi.append(i)


def IsDivisibleInv(a, b):
    """Check Involutive Divisibility
    """
    if a.isdivisible(b):
        return True


def NormalFormInv(p, F):
    """Compute Involutive NormalForm
    """
    raise NotImplemented


def AutoreduceInv(F):
    """Autoreduce set of polynomials
    """
    raise NotImplemented
