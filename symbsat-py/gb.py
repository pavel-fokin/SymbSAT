# pylint: disable=invalid-name
"""Groebner Basis."""

from polyfuncs import spoly, normal_form


def _autoreduce(G):
    """
    Code from Toy Bucberger Algorithm Sympy
    https://mattpap.github.io/masters-thesis/html/src/groebner.html
    """
    G_red = []
    for i, g in enumerate(G):
        G[i] = normal_form(g, G[:i] + G[i+1:])
        if not G[i].isZero():
            G_red.append(G[i])
    return G_red


def autoreduce(F):
    """Autoreduce set of polynomials
    K. Geddes, S. Czapor, G. Labahn
    Algorithms for Computer Algebra (1992)
    p. 448 ReduceSet(E)
    """
    G = F.copy()
    P = []

    while G != []:
        h = G.pop(-1)
        h = normal_form(h, P)
        if not h.isZero():
            P_size = len(P)
            i = 0
            while i < P_size:
                p = P[i]
                if p.lm().isdivisible(h.lm()):
                    G.append(p)
                    P.remove(p)
                    P_size -= 1
                else:
                    i += 1
            P.append(h)

    P_size = len(P)
    i = 0
    while i < P_size:
        h = P.pop()
        h = normal_form(h, P)
        if h.isZero():
            P_size -= 1
        else:
            P.append(h)
        i += 1
    return P


def _criteria(i, j, M, G):
    """Two Buchberger's criteria"""

    Gi, Gj = G[i], G[j]
    Gi_lm, Gj_lm = Gi.lm(), Gj.lm()

    if Gi_lm.isrelativelyprime(Gj_lm):
        return True

    for k, _ in enumerate(G):
        if ((M[i][k] and M[k][j])
                and G[k].lm().isdivisible(Gi_lm * Gj_lm)):
            return True

    return False


def buchberger(F, BRing):
    """Basic Buchberger algorithm with two criteria."""
    if len(F) > 1:
        G = autoreduce(F)
    else:
        G = F
    k = len(G)

    x = BRing.gens

    # Fill pairs with negative indexes for field polynomials
    pairs = [(i, j) for i in range(-len(BRing.gens), k) for j in range(len(G))]
    # Matrix M with treated pairs
    M = [[0 for i in range(len(G))] for j in range(len(G))]

    count = 0
    while pairs != []:
        i, j = pairs.pop(0)

        # case with field polynomial
        if i < 0:
            Gj_lm, xi = G[j].lm(), x[abs(i)-1].lm()
            if Gj_lm.isrelativelyprime(xi):
                continue
            s = G[j]*x[abs(i)-1]
        else:
            M[i][j] = 1
            if _criteria(i, j, M, G):
                continue
            p, q = G[i], G[j]
            s = spoly(p, q)

        h = normal_form(s, G)

        if not h.isZero():
            G.append(h)

            pairs += [(i, k) for i in range(-len(BRing.gens), k)]
            k += 1

            # Extend M with new entry (h, g) forall g in G
            for row in M:
                row.append(0)
            M.append([0 for i in range(len(G))])

        count += 1

    # Autoreduce
    G_red = autoreduce(G)

    return G_red
