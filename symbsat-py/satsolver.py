"""Check SAT UNSAT."""

import functools

import dimacs
import gb
from poly import Poly


def sat_mult(P):

    _1 = Poly.one

    res = functools.reduce(lambda res, p: res*(p+_1), P, _1)

    if res == Poly.zero:
        print('UNSAT')
    else:
        print('SAT')


def sat_groebner(P, ring):

    res = gb.buchberger(P, ring)

    if res == [Poly.one]:
        print('UNSAT')
    else:
        print('SAT')


def main():

    P, ring = dimacs.load(sys.argv[1], sys.argv[2] or "list")
    sat_groebner(P, ring)
    #  sat_mult(P)
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main())
