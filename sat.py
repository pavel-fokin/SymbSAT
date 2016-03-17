"""
Check SAT UNSAT
"""

import functools

import cnftools
import gb
from poly import Poly


def sat_mult(P):

    _1 = Poly.one

    res = functools.reduce(lambda res, p: res*(p+_1), P, _1)

    if res == Poly.zero:
        print('UNSAT')
    else:
        print('SAT')


def sat_groebner(P, variables):

    res = gb.buchberger(P, variables)

    if res == [Poly.one]:
        print('UNSAT')
    else:
        print('SAT')


def main():

    P, variables = cnftools.cnf2polys(sys.argv[1])
    sat_groebner(P, variables)
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main())
