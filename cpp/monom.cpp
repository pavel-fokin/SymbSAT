#include "monom.h"

Monom operator*(const Monom& a, const Monom& b) {
    Monom tmp;
    tmp.mVars = a.mVars | b.mVars;
    return tmp;
}

Monom operator/(const Monom& a, const Monom& b) {
    Monom tmp;
    tmp.mVars = a.mVars ^ b.mVars;
    return tmp;
}

bool operator<(const Monom& a, const Monom& b) {
    return a.mVars.to_string() < b.mVars.to_string();
}

std::ostream& operator<<(std::ostream& out, const Monom &a) {
    out << "[ ";
    for (size_t i=0; i<a.mVars.size(); ++i) {
        if (a.mVars[i]) {
            out << i << " "; 
        }
    }
    out << "]";
    return out;
}
