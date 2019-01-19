"""Generic functions for polynomials."""


def spoly(f, g):
    """Return s-polynomial."""
    f_lm, g_lm = f.lm(), g.lm()
    lcm = f_lm.lcm(g_lm)
    spoly = f*(lcm/f_lm) + g*(lcm/g_lm)
    return spoly


def normal_form(f, F):
    """
    NormalForm w.r.t F
    D. Cox, J. Little, D. O'Shea - Ideals, Varieties, and Algorithms
    $3 A Division Algorithm
    """
    p = f.copy()
    r = f.zero()

    if F == []:
        return p

    while not p.is_zero():
        i = 0
        divisionoccured = False
        while i < len(F) and (not divisionoccured):
            p_lm, fi_lm = p.lm(), F[i].lm()
            if p_lm.isdivisible(fi_lm):
                p = p + F[i]*(p_lm/fi_lm)
                divisionoccured = True
            else:
                i += 1
        if not divisionoccured:
            r = r + p_lm
            p = p + p_lm

    return r
