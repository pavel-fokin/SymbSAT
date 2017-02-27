#include "catch.hpp"

#include "monomt.h"

TEST_CASE("Monom Constructor", "[monom-constructor]") {
  Monoms::Monom32 x1(0), x2(1);
  Monoms::Monom32 _0;
  Monoms::Monom32 _1;
  _1.setOne();

  CHECK(!(x1 == x2));
  REQUIRE(x1.toStr() == "[ 0 ]");
  REQUIRE(x2.toStr() == "[ 1 ]");
  REQUIRE(_0.toStr() == "0");
  REQUIRE(_1.toStr() == "1");
}

TEST_CASE("Monom Ordering", "[monom-ordering]") {
  Monoms::Monom64 a(0), b(1), c(2), ab(a * b);
  Monoms::Monom64 _0, _1;
  _1.setOne();

  REQUIRE(!(a < b));
  REQUIRE(b < a);
  REQUIRE(c < a);
  REQUIRE(!(b < c));
  REQUIRE(b < ab);
}

TEST_CASE("Monom Multiplication", "[monom-mul]") {
    Monoms::Monom64 a(0), b(1), c(2), abc;
    Monoms::Monom64 _0, _1;
    _1.setOne();

    abc = a*b*c;

    REQUIRE(abc == a*b*c);

    REQUIRE(a*b == b*a);
    REQUIRE(a*a == a);

    b = a * _1;
    REQUIRE(a == b);

    b = _1 * a;
    REQUIRE(a == b);

    b = a * _0;
    REQUIRE(b.isZero());

    b = _0 * a;
    REQUIRE(b.isZero());

    SECTION ("Multiply 1*1") {
        Monoms::Monom32 one_1, one_2, res;
        one_1.setOne();
        one_2.setOne();
        res = one_1 * one_2;

        REQUIRE(res.isOne());
    }
}

TEST_CASE("Monom IsDivisible", "[monom-isdivisible]") {
    Monoms::Monom64 a(0), b(1), ab;
    Monoms::Monom64 _0, _1;
    _1.setOne();

    // REQUIRE(!a.isdivisible(_0));
    // a/1 = a True
    REQUIRE(a.isdivisible(_1));
    // a/b = 0 False
    REQUIRE(!a.isdivisible(b));
    // 1/b = 0 False
    REQUIRE(!_1.isdivisible(b));

    ab = a*b;
    REQUIRE(ab.isdivisible(a));
    REQUIRE(ab.isdivisible(b));
}

TEST_CASE("Monom Division", "[monom-division]") {
    Monoms::Monom64 a(0), b(1), c(2);
    Monoms::Monom64 ab(a*b), bc(b*c), abc(a*b*c);
    Monoms::Monom64 _0, _1;
    _1.setOne();

    // b = a/_1;
    // a == a/_1;
    REQUIRE(a == a/_1);

    // a/b == _0;
    REQUIRE(_0 == a/b);

    // ab/b == a;
    REQUIRE(a == ab/b);
    // ab/a == b;
    REQUIRE(b == ab/a);
    // abc/ab == c;
    REQUIRE(c == abc/ab);
    // ab/bc == 0;
    REQUIRE(_0 == ab/bc);
}

TEST_CASE("Monom IsRelativelyPrime", "[monom-isrelativelyprime]") {
    Monoms::Monom64 a(0), b(1), ab(a*b);
    Monoms::Monom64 _0, _1;
    _1.setOne();

    REQUIRE(a.isrelativelyprime(a));
    REQUIRE(a.isrelativelyprime(_1));
    REQUIRE(a.isrelativelyprime(b));
    REQUIRE(!ab.isrelativelyprime(b));
}

TEST_CASE("Monom GetVars", "[monom-getvars]") {
    Monoms::Monom64 a(0), b(1), c(2), d(3);
    Monoms::Monom64 abd(a*b*d);

    std::vector<int> vars {0,1,3};
    REQUIRE(abd.getVars() == vars);
}
