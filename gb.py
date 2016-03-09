"""
Groebner Basis
"""

import sys
import itertools
import time

from poly import Poly, generate_n_vars


def autoreduce(G):
    """
    Code from Toy Bucberger Algorithm Sympy
    https://mattpap.github.io/masters-thesis/html/src/groebner.html
    """
    G_red = []
    for i, g in enumerate(G):
        G[i] = g.NF(G[:i] + G[i+1:])
        if G[i] != Poly.zero:
            G_red.append(G[i])
    return G_red

def buchberger(F, variables):
    """
    Basic Buchberger algorithm without any optimizations
    """
    if len(F)>1:
        G = autoreduce(F)
    else:
        G = F
    k = len(G)

    x = generate_n_vars(variables)
    assert x != []

    # Fill pairs with negative indexes for field polynomials
    pairs = [(i, j) for i in range(-len(variables), 0) for j in range(len(G))]

    pairs += list(itertools.combinations(range(len(G)), 2))

    count = 0
    while pairs != []:
        i, j = pairs.pop(0)

        # case with field polynomial
        if i < 0:
            Gj_lm, xi = G[j].lt(), x[abs(i)-1].lt()
            if Gj_lm.isrelativelyprime(xi):
                continue
            s = G[j]*x[abs(i)-1]
        else:
            p, q = G[i], G[j]
            p_lm, q_lm = p.lt(), q.lt()
            #TODO Check first criteria
            if p_lm.isrelativelyprime(q_lm):
                continue
            s = Poly.S(p, q)
        h = s.NF(G)
        if h != Poly.zero:
            G.append(h)
            k += 1
            pairs += [(i, k-1) for i in range(-len(variables), k-1)]
        count += 1

    # Autoreduce
    G_red = autoreduce(G)

    return G_red
