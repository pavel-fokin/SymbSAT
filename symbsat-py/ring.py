"""Boolean Polynomial Ring."""
from monom import make_monom_type
from poly import Poly
from zdd import make_zdd_type


class BoolPolyRing:

    def __init__(self, n, poly_type="list"):

        monom_type = make_monom_type(n)

        if poly_type == "list":
            Poly.ring = self

            self.one = Poly._one
            self.zero = Poly._zero

            self.gens = [
                Poly([monom_type(vars=[i])])
                for i in range(n)
            ]
        elif poly_type == "zdd":
            ZDD = make_zdd_type(monom_type)

            one = ZDD()
            one.setOne()

            zero = ZDD()
            zero.setZero()

            self.one = one
            self.zero = zero

            self.gens = [ZDD(i) for i in range(n)]
