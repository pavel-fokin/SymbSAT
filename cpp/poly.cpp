#include <algorithm>
#include <iterator>
#include <vector>
#include <unordered_set>
#include <iostream>

#include "poly.h"


// TODO Super naive implementation
bool Poly::operator==(const Poly& other) const {
    Poly a(*this), b(other);

    std::sort(a.mMonoms.begin(), a.mMonoms.end());
    std::sort(b.mMonoms.begin(), b.mMonoms.end());
    return a.mMonoms == b.mMonoms;
}

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

Poly normalform(const Poly& f, const std::vector<Poly>& F) {
    Poly p(f), r;

    if (F.empty()) {
        return r;
    }

    while (!p.isZero()) {
        int i {0};
        bool divisionoccured {false};
        Monom p_lm, fi_lm;
        while (i < F.size() && !divisionoccured) {
            p_lm = p.lm();
            fi_lm = F[i].lm();
            if (p_lm.isdivisible(fi_lm)) {
                p = p + F[i]*(p_lm/fi_lm);
                divisionoccured = true;
            } else {
                i++;
            }
        }
        if (!divisionoccured) {
            r = r + Poly(p_lm);
            p = p + Poly(p_lm);
        }
    }
    return r;
}
