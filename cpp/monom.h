#include <iostream>
#include <bitset>
#include <string>
#include <utility>

class Monom {
    std::bitset<64> mVars;

public:
    Monom() {};
    Monom(size_t var) {
        mVars.set(var);
    }
    Monom(const Monom& m): mVars(m.mVars) {}
    Monom(const Monom&& m) noexcept : mVars(std::move(m.mVars)) {}
    // Monom& operator=(const Monom&& other);
    Monom& operator=(const Monom& other) {
        if (this != &other) {
            mVars = other.mVars;
        }
        return *this;
    }
    // ~Monom() {}

    bool isZero() {
        return this == sZero;
    }
    bool isOne() {
        return this == sOne;
    }

    bool isdivisible(Monom& other);
    bool isrelativelyprime(Monom& other);

    friend Monom lcm(const Monom& a, const Monom& b);
    friend Monom operator*(const Monom& a, const Monom& b);
    friend Monom operator/(const Monom& a, const Monom& b);
    friend bool operator<(const Monom& a, const Monom& b);
    friend std::ostream& operator<<(std::ostream& out, const Monom &a);

    static const Monom *const sZero;
    static const Monom *const sOne;
};
