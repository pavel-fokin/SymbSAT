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


if __name__ == '__main__':

    # SAT
    FILENAME1 = 'cnf/quinn.cnf'
    # UNSAT
    FILENAME2 = 'cnf/hole6.cnf'
    FILENAME3 = 'cnf/dubois20.cnf'
    FILENAME4 = 'cnf/dubois22.cnf'
    FILENAME5 = 'cnf/aim-100-1_6-no-1.cnf'
    # Minimal unsat
    FILENAME6 = 'cnf/unsat.cnf'
    FILENAME7 = 'cnf/rope_0001.shuffled.cnf'
    FILENAME8 = 'cnf/marg/marg2x2.cnf'
    FILENAME9 = 'cnf/marg/marg2x3.cnf'
    FILENAME10 = 'cnf/marg/marg2x4.cnf'
    FILENAME11 = 'cnf/marg/marg2x5.cnf'
    FILENAME12 = 'cnf/marg/marg2x6.cnf'
    FILENAME13 = 'cnf/x1_16.shuffled.cnf'

    P, variables = cnftools.cnf2polys(FILENAME10)

    # print()
    # for p in P:
        # print(p)

    # sat_mult(P)
    sat_groebner(P, variables)
