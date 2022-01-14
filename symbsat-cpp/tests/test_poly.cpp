#include "catch.hpp"

#include "monom.h"
#include "poly.h"

using namespace symbsat;

typedef Monom<32> Monom32;

TEST_CASE("Poly Constructor", "[poly-constructor]") {
  Monom32 a(0), b(1), c(2);

  Poly<Monom32> p1;
  Poly<Monom32> p2(a);
  Poly<Monom32> p3({a, b, c});

  std::vector<Monom32> monoms {b, c, a};
  Poly<Monom32> p4(monoms);
}

TEST_CASE("Polynomial Leading Monomial", "[poly-lm]") {
  Monom32 a(0), b(1), c(2);
  Monom32 _0;

  Poly<Monom32> p1({b, c, a});

  CHECK(p1.toStr() == "[ 0 ] [ 1 ] [ 2 ]");
  REQUIRE(p1.lm() == a);

  Poly<Monom32> p2;

  CHECK(p2.isZero());
  REQUIRE(p2.lm() == _0);
}

TEST_CASE("Polynomial Addition", "[poly-add]") {
  Monom32 a(0), b(1);
  Poly<Monom32> p_a(a), p_b(b), p_ab, p_aa;

  p_ab = p_a + p_b;
  p_aa = p_a + p_a;
  REQUIRE(p_aa.isZero());

}

TEST_CASE("Polynomial Multiplication", "[poly-mul]") {
  Monom32 a(0), b(1), c(2);

  Poly<Monom32> p_a(a), p_b(b), p_c(c), p_abc;

  p_abc = p_a + p_b + p_c;
  CHECK(p_abc.toStr() == "[ 0 ] [ 1 ] [ 2 ]");

  Poly<Monom32> p_res;
  p_res = p_abc * p_c;

  CHECK(p_abc.toStr() == "[ 0 ] [ 1 ] [ 2 ]");
  REQUIRE(p_res.toStr() == "[ 0 2 ] [ 1 2 ] [ 2 ]");

  Poly<Monom32> p_zero;

  CHECK(p_zero.isZero());

  p_res *= p_zero;

  REQUIRE(p_res.isZero());

  SECTION("Multiply by Monom") {
  }

  SECTION("Fix Bug Monoms == 1") {
    Monom32 a(0), b(1), c(2);
    Poly<Monom32> x1(0), x2(1), x3(2), _1;
    _1.setOne();

    Poly<Monom32> p1, p2;

    p1 = (x1 + _1)*(b*c);
    p2 = (x1 + _1)*(x2*x3);
    REQUIRE(p1 == x1*x2*x3 + x2*x3);
    REQUIRE(p2 == x1*x2*x3 + x2*x3);

  }
  SECTION ("Fix Bug p = x1 + x1 + 1") {
    Poly<Monom32> x1(1), p, f, _1;
    _1.setOne();

   p = x1;
   f = x1 + _1;
   p = p + f*_1;
  }
}

TEST_CASE("Polynomial Multiply by Monom", "[poly-mul-monom]") {
    Monom32 a(0), b(1), c(2), _0;
    Poly<Monom32> p_a(a), p_b(b), p_c(c), p_res;

    p_res = p_a * b;

    REQUIRE(p_res.toStr() == "[ 0 1 ]");

    p_res *= _0;

    REQUIRE(p_res.isZero());

    Poly<Monom32> p1, p2;
    p1 = p_a * p_b + p_a;
    p1 = p1 * a;
    REQUIRE(p1.toStr() == "[ 0 1 ] [ 0 ]");

    p2 = p_a * p_b + p_a + p_c;
    p2 = p2 * b;
    REQUIRE(p2.toStr() == "[ 1 2 ]");
}
