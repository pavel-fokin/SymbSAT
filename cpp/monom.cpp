#include "monom.h"

bool Monom::isdivisible(const Monom& other) const {
    if (other.isOne()) {
        return true;
    } else if (this->isOne()) {
        return false;
    } else {
        return mVars == (mVars | other.mVars);
    }

}

bool Monom::isrelativelyprime(const Monom& other) const {
    if (mVars == other.mVars) {
        return true;
    } else if (this->isOne()) {
        return true;
    } else {
        auto lcm = mVars | other.mVars;
        return (lcm ^ mVars) == other.mVars;
    }
}

Monom operator*(const Monom& a, const Monom& b) {
    if (a.isOne()) {
        return b;
    }
    if (b.isOne()) {
        return a;
    }
    if (a.isZero() || b.isZero()) {
        return Monom();
    }
    Monom tmp;
    tmp.mVars = a.mVars | b.mVars;
    return tmp;
}

Monom operator/(const Monom& a, const Monom& b) {
    if (b.isOne()) {
        return a;
    }
    if (a.isOne()) {
        return Monom();
    }
    if (a == b) {
        // return 1
        return Monom(0);
    }
    if (!a.isdivisible(b)) {
        // return 0
        return Monom();
    }
    Monom tmp;
    tmp.mVars = a.mVars ^ b.mVars;
    return tmp;
}

bool operator<(const Monom& a, const Monom& b) {
    for (size_t i = 1; i < a.mVars.size(); ++i) {
        if (a.mVars[i] < b.mVars[i])
            return true;
    }
    return false;
}

std::ostream& operator<<(std::ostream& out, const Monom &a) {
    if (a.isZero()) {
        out << "0";
        return out;
    }
    if (a.isOne()) {
        out << "1";
        return out;
    }
    out << "[ ";
    // start from 1 because first bit is for 0/1
    for (size_t i=1; i<a.mVars.size(); ++i) {
        if (a.mVars[i]) {
            out << i << " ";
        }
    }
    out << "]";
    return out;
}
