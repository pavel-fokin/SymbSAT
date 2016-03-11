#ifndef MONOM_H
#define MONOM_H

#include <iostream>
#include <bitset>
#include <string>
#include <utility>
#include <memory>

class Monom {
    // first bit is indicate zero one

public:
    std::bitset<128> mVars;
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

    bool isZero() const {
        // return this == Monom::sZero.get();
        return mVars.none();
    }
    bool isOne() const {
        // return this == Monom::sOne.get();
        return mVars.test(0);
    }

    bool isdivisible(const Monom& other) const;
    bool isrelativelyprime(const Monom& other) const;

    bool operator==(const Monom& other) const {
        return mVars == other.mVars;
    }

    friend Monom lcm(const Monom& a, const Monom& b);
    friend Monom operator*(const Monom& a, const Monom& b);
    friend Monom operator/(const Monom& a, const Monom& b);
    friend bool operator<(const Monom& a, const Monom& b);

    friend std::ostream& operator<<(std::ostream& out, const Monom &a);

    // static const Monom *const sZero;
    // static const Monom *const sOne;

    // static const std::unique_ptr<Monom> sZero;
    // static const std::unique_ptr<Monom> sOne;
};

#endif // MONOM_H
