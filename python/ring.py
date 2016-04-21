"""BoolPolyRing
"""
from monom import Monom
from poly import Poly


class BoolPolyRing(object):

    def __init__(self, n):
        Monom.size = n

        self.gens = [
            Poly([Monom(vars=[i])])
            for i in range(n)
        ]
