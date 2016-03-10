#include <algorithm>
#include <iterator>
#include <vector>

#include "poly.h"

Poly operator+(Poly& a, Poly& b) {
    std::vector<Monom> monoms;
    std::set_symmetric_difference(
        a.mMonoms.begin(), a.mMonoms.end(),
        b.mMonoms.begin(), b.mMonoms.end(),
        std::back_inserter(monoms)
    );

    return Poly(monoms);
}

Poly operator*(Poly& a, Monom& b) {
    for (auto&& m: a.mMonoms) {
        std::cout << m*b << std::endl;
    }
    return Poly();
}

std::ostream& operator<<(std::ostream& out, const Poly &a) {
    for (auto&& m: a.mMonoms) {
        out << m << " ";
    }
    return out;
}
