#ifndef POLY_H
#define POLY_H

#include <vector>

#include "monom.h"


class Poly {
    std::vector<Monom> mMonoms;

public:
    Poly() {};
    Poly(Monom& m) : mMonoms{m} {}
    Poly(std::vector<Monom>& monoms) : mMonoms(monoms) {}
    Poly(const Poly& other) : mMonoms(other.mMonoms) {}
    Poly& operator=(const Poly& other) {
        if (this != &other) {
            mMonoms = other.mMonoms;
        }
        return *this;
    }
    Poly(const Poly&& other) noexcept : mMonoms(other.mMonoms) {}
    // Poly& operator=(const Poly&& other);
    // ~Poly() {}

    Monom lm();

    friend Poly operator+(Poly& a, Poly& b);
    friend Poly operator*(Poly& a, Poly& b);
    friend Poly operator*(Poly& a, Monom& m);

    friend std::ostream& operator<<(std::ostream& out, const Poly &a);
};

#endif // POLY_H
