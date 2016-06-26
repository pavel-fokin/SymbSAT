#ifndef MONOM_H
#define MONOM_H

#include <iostream>
#include <bitset>
#include <vector>
#include <string>
#include <utility>
#include <memory>

class Monom {
    // first bit indicates zero/one
    std::bitset<128> mVars;

public:
    Monom() {};
    explicit Monom(size_t var) {
        mVars.set(var);
    }
    Monom(const Monom& m): mVars(m.mVars) {}
    Monom(const Monom&& m) noexcept : mVars(std::move(m.mVars)) {}
    Monom& operator=(Monom&& other) noexcept {
        if (this != &other) {
            mVars = std::move(other.mVars);
        }
        return *this;
    }
    Monom& operator=(const Monom& other) {
        if (this != &other) {
            mVars = other.mVars;
        }
        return *this;
    }
    ~Monom() {}

    void setVar(size_t var) {
        mVars.set(var);
    }
    std::vector<int> getVars() const {
        std::vector<int> vars;

        size_t msize = mVars.size();
        for (size_t i = 1; i < msize; ++i) {
            if (mVars[i]) {
                vars.push_back(i);
            }
        }
        return vars;
    }

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

    bool operator<(const Monom& a) const;
    bool operator==(const Monom& other) const {
        return mVars == other.mVars;
    }

    Monom operator*(const Monom& b) const;
    Monom operator/(const Monom& b) const;
    friend Monom lcm(const Monom& a, const Monom& b);

    friend std::ostream& operator<<(std::ostream& out, const Monom &a);

    struct hash {
        size_t operator()(const Monom& x) const {
            return std::hash<std::bitset<128>>()(x.mVars);
        }
    };
};

#endif // MONOM_H
