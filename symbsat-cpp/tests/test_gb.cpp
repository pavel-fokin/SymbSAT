#include "catch.hpp"

#include "monom.h"
#include "poly.h"
#include "zdd.h"
#include "gb.h"

using namespace symbsat;

TEST_CASE("Buchberger 1 PolyZDD", "[buchberger-polyzdd]") {
    ZDD<Monom32> x1(1), x2(2),
                         x3(4), x4(4), _1;
    _1.setOne();

    std::vector<ZDD<Monom32>> F {
        x1 + x2 + x3 + x4,
        x1*x2 + x2*x3 + x1*x3 + x3*x4,
        x1*x2*x3 + x1*x2*x4 + x1*x3*x4 + x2*x3*x4,
        x1*x2*x3*x4 + _1
    };

    auto G = buchberger(F, 4);

    // for (auto& p: G)
        // std::cout << p << std::endl;

    REQUIRE(true);
}

TEST_CASE("Buchberger 1 PolyList", "[buchberger-polylist]") {
    Poly<Monom32> x1(1), x2(2),
                          x3(4), x4(4), _1;
    _1.setOne();

    std::vector<Poly<Monom32>> F {
        x1 + x2 + x3 + x4,
        x1*x2 + x2*x3 + x1*x3 + x3*x4,
        x1*x2*x3 + x1*x2*x4 + x1*x3*x4 + x2*x3*x4,
        x1*x2*x3*x4 + _1
    };

    auto G = buchberger(F, 4);

    // for (auto& p: G)
        // std::cout << p << std::endl;

    REQUIRE(true);
}

TEST_CASE("Buchberger 3 PolyZDD", "[buchberger3-polyzdd]") {
    ZDD<Monom32> x1(1), x2(2), _1;
    _1.setOne();

    std::vector<ZDD<Monom32>> F {
        x1*x2 + x1,
        x1*x2 + x2
    };

    auto G = buchberger(F, 2);

    REQUIRE(true);
}

TEST_CASE("Buchberger 3 PolyList", "[buchberger3-polylist]") {
    Poly<Monom32> x1(1), x2(2), _1;
    _1.setOne();

    std::vector<Poly<Monom32>> F {
        x1*x2 + x1,
        x1*x2 + x2
    };

    auto G = buchberger(F, 2);

    REQUIRE(true);
}

TEST_CASE("Buchberger 7 PolyZDD", "[buchberger7-polyzdd]") {
    ZDD<Monom32> x1(1), x2(2), x3(3), _1;
    _1.setOne();

    std::vector<ZDD<Monom32>> F {
        x1*x2*x3,
        x1*x2*x3 + x1*x2,
        x1*x2*x3 + x1*x3,
        x1*x2*x3 + x1*x2 + x1*x3 + x1,
        x1*x2*x3 + x2*x3,
        x1*x2*x3 + x1*x2 + x2*x3 + x2,
        x1*x2*x3 + x1*x3 + x2*x3 + x3,
        x1*x2*x3 + x1*x2 + x1*x3 + x1 + x2*x3 + x2 + x3 + _1
    };

    auto G = buchberger(F, 3);

    REQUIRE(true);
}

TEST_CASE("Buchberger 7 PolyList", "[buchberger7-polylist]") {
    Poly<Monom32> x1(1), x2(2), x3(3), _1;
    _1.setOne();

    std::vector<Poly<Monom32>> F {
        x1*x2*x3,
        x1*x2*x3 + x1*x2,
        x1*x2*x3 + x1*x3,
        x1*x2*x3 + x1*x2 + x1*x3 + x1,
        x1*x2*x3 + x2*x3,
        x1*x2*x3 + x1*x2 + x2*x3 + x2,
        x1*x2*x3 + x1*x3 + x2*x3 + x3,
        x1*x2*x3 + x1*x2 + x1*x3 + x1 + x2*x3 + x2 + x3 + _1
    };

    auto G = buchberger(F, 3);

    REQUIRE(true);
}
