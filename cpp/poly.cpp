#include <algorithm>
#include <iterator>
#include <vector>
#include <unordered_set>
#include <iostream>

#include "poly.h"


Poly Poly::operator+(const Poly& b) const {
    std::vector<Monom> monoms;
    std::set_symmetric_difference(
        mMonoms.begin(), mMonoms.end(),
        b.mMonoms.begin(), b.mMonoms.end(),
        std::back_inserter(monoms)
    );

    return Poly(monoms);
}
// Poly operator+(Poly& a, Poly& b) {
    // std::vector<Monom> monoms;
    // std::set_symmetric_difference(
        // a.mMonoms.begin(), a.mMonoms.end(),
        // b.mMonoms.begin(), b.mMonoms.end(),
        // std::back_inserter(monoms)
    // );

    // return Poly(monoms);
// }

Poly operator*(const Poly& a, const Monom& b) {
    std::unordered_set<Monom, Monom::hash> monoms_set;

    for (auto&& m: a.mMonoms) {
        Monom tmp(m*b);

        if (monoms_set.find(tmp) == monoms_set.end()) {
            monoms_set.insert(tmp);
        } else {
            monoms_set.erase(tmp);
        }
    }

    std::vector<Monom> monoms_vec(std::begin(monoms_set), std::end(monoms_set));

    return Poly(monoms_vec);
}

Poly operator*(Poly& a, Poly& b) {
    for (auto&& m: a.mMonoms) {
        std::cout << m << std::endl;
    }
    return Poly();
}

std::ostream& operator<<(std::ostream& out, const Poly &a) {
    if (a.isZero()) {
        out << "0";
    } else if (a.isOne()) {
        out << "1";
    } else {
        for (auto&& m: a.mMonoms) {
            out << m << " ";
        }
    }
    return out;
}
