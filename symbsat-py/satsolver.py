"""Check SAT UNSAT."""
import argparse
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

    parser = argparse.ArgumentParser(
        description='Check files in DIMACS format'
    )
    parser.add_argument(
        'file', metavar='DIMACS', type=argparse.FileType('r'),
        help='File in DIMACS format'
    )
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument(
        '--polylist', action='store_const', dest='polytype', const='list',
        default='list'
    )
    group.add_argument(
        '--polyzdd', action='store_const', dest='polytype', const='zdd'
    )

    args = parser.parse_args()

    P, ring = dimacs.load(args.file, args.polytype)
    sat_groebner(P, ring)
    #  sat_mult(P)
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main())
