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

Poly Poly::operator*(const Monom& b) const {
    if (isZero() || b.isZero()) {
        return Poly();
    }
    std::unordered_set<Monom, Monom::hash> monoms_set;

    for (auto&& m: mMonoms) {
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

Poly Poly::operator*(const Poly& b) const {
    if (isZero() || b.isZero()) {
        // return 0
        return Poly();
    }
    std::unordered_set<Monom, Monom::hash> monoms_set;
    for (auto&& m1: mMonoms) {
        for (auto&& m2: b.mMonoms) {
            Monom tmp(m1*m2);
            if (monoms_set.find(tmp) == monoms_set.end()) {
                monoms_set.insert(tmp);
            } else {
                monoms_set.erase(tmp);
            }
        }
    }
    std::vector<Monom> monoms_vec(std::begin(monoms_set), std::end(monoms_set));
    return Poly(monoms_vec);
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

Poly spoly(const Poly& f, const Poly& g) {
    Monom f_lm = f.lm();
    Monom g_lm = g.lm();
    Monom lcm = f_lm*g_lm;

    Poly spoly;

    spoly = f*(lcm/f_lm) + g*(lcm/g_lm);

    return spoly;
}
