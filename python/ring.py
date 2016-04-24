"""BoolPolyRing
"""
from monom import Monom
from poly import Poly
from zdd import ZDD


class BoolPolyRing(object):

    def __init__(self, n, poly_type="list"):
        Monom.size = n

        if poly_type == "list":
            self.gens = [
                Poly([Monom(vars=[i])])
                for i in range(n)
            ]
        elif poly_type == "zdd":
            self.gens = [ZDD(i) for i in range(n)]
