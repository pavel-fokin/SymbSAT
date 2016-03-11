#include "monom.h"

// const std::unique_ptr<Monom> Monom::sZero = std::make_unique<Monom>();
// const std::unique_ptr<Monom> Monom::sOne = std::make_unique<Monom>();

bool Monom::isdivisible(const Monom& other) const {
    if (other.isOne()) {
        return true;
    } else if (this->isOne()) {
        return false;
    } else {
        return mVars == (mVars | other.mVars);
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
    // std::cout << a << b << std::endl;
    if (!a.isdivisible(b)) {
        // return 0
        return Monom();
    }
    Monom tmp;
    tmp.mVars = a.mVars ^ b.mVars;
    return tmp;
}

bool operator<(const Monom& a, const Monom& b) {
    return a.mVars.to_string() < b.mVars.to_string();
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
    for (size_t i=0; i<a.mVars.size(); ++i) {
        if (a.mVars[i]) {
            out << i << " "; 
        }
    }
    out << "]";
    return out;
}
