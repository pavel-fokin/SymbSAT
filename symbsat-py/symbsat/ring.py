"""Boolean Polynomial Ring."""
from symbsat.monom import Monom
from symbsat.poly import Poly
from symbsat.zdd import ZDD


class BoolPolyRing:

    def __init__(self, n, poly_type="list"):

        Monom.size = n

        if poly_type == "list":
            Poly.ring = self
            self.one = Poly.one
            self.zero = Poly.zero

            self.gens = [
                Poly([Monom(vars=[i])])
                for i in range(n)
            ]
        elif poly_type == "zdd":
            ZDD.ring = self

            one = ZDD()
            one.setOne()

            zero = ZDD()
            zero.setZero()

            self.one = one
            self.zero = zero

            self.gens = [ZDD(i) for i in range(n)]
