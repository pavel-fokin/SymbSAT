#include <iostream>

#include "poly.h"

int main() {
    Monom m1(0), m2(1), m3, m4;

    // m3 = m3.mul(m1, m2);
    m3 = m1 * m2;
    m4 = m3 / m2;
    Poly p1(m1);
    Poly p2(m2);
    Poly p3;
    Poly p4;
    p3 = p1 + p2;
    p4 = p3*p1;

    std::cout << m1 << std::endl;
    std::cout << m2 << std::endl;
    std::cout << m3 << std::endl;
    std::cout << m4 << std::endl;
    std::cout << "sizeof(Monom) " << sizeof(m1) << std::endl;
    std::cout << "sizeof(Poly) " << sizeof(p1) << std::endl;
    std::cout << p1 << std::endl;
    std::cout << p2 << std::endl;
    std::cout << p3 << std::endl;
    std::cout << std::endl;
    std::cout << p4 << std::endl;
}
