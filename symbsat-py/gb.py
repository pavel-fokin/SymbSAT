"""Groebner Basis."""

from polyfuncs import spoly, normal_form


def autoreduce(G):
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


def buchberger(F, BRing):
    """Basic Buchberger algorithm without any optimizations."""
    if len(F) > 1:
        G = autoreduce(F)
    else:
        G = F
    k = len(G)

    x = BRing.gens

    # Fill pairs with negative indexes for field polynomials
    pairs = [(i, j) for i in range(-len(BRing.gens), k) for j in range(len(G))]

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
            p, q = G[i], G[j]
            p_lm, q_lm = p.lm(), q.lm()
            # TODO Check first criteria
            if p_lm.isrelativelyprime(q_lm):
                continue
            s = spoly(p, q)
        h = normal_form(s, G)
        if not h.isZero():
            G.append(h)
            pairs += [(i, k) for i in range(-len(BRing.gens), k)]
            k += 1
        count += 1

    # Autoreduce
    G_red = autoreduce(G)

    return G_red
