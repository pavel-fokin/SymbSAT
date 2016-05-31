try:
    from sympy.logic.utilities.dimacs import load
    from sympy.logic.algorithms.dpll import dpll_satisfiable
except ImportError:
    raise ImportError("SymPy is required.")


def main():
    with open(sys.argv[1]) as cnf_file:
        cnf = load(cnf_file.read())
    result = dpll_satisfiable(cnf)
    print(result)
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main())
