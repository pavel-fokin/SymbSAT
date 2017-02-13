#include "catch.hpp"

#include "monomt.h"
#include "zddt.h"

using namespace symbsat;

TEST_CASE("ZDD Constructor", "[zdd-constructor]") {
  ZDD<Monoms::Monom32> z;
  REQUIRE(z.isZero());

  ZDD<Monoms::Monom32> z1(1), z2(2);
  REQUIRE(!(z1 == z2));

  ZDD<Monoms::Monom32> z3(z1);
  REQUIRE(z1 == z3);

  ZDD<Monoms::Monom32> z4 = z2;
  REQUIRE(z4 == z2);

  ZDD<Monoms::Monom32> z5(5), z6;
  REQUIRE(!(z5 == z6));

  z5 = z6;
  REQUIRE(z5 == z6);
}

TEST_CASE("ZDD Constructor of Monoms", "[zdd-constructor-monom]") {
  Monoms::Monom32 a(1), b(2), c(3);
  Monoms::Monom32 abc(a * b * c);

  ZDD<Monoms::Monom32> z(abc);
  REQUIRE(abc == z.lm());

  Monoms::Monom32 m_zero;
  ZDD<Monoms::Monom32> z_zero(m_zero);
  REQUIRE(z_zero.isZero());

  Monoms::Monom32 m_one;
  m_one.setOne();
  ZDD<Monoms::Monom32> z_one(m_one);
  REQUIRE(z_one.isOne());
}

TEST_CASE("ZDD MonomIterator", "[zdd-monom-iter]") {
  ZDD<Monoms::Monom32> z1(1), z2(2);
  ZDD<Monoms::Monom32> z3 = z1 * z2 + z2;

  ZDD<Monoms::Monom32>::MonomConstIterator it(z3);

  while (!it) {
    ++it;
  }

  REQUIRE(true);
}

TEST_CASE("ZDD LM", "[zdd-lm]") {
  Monoms::Monom32 a(1), b(2), c(3);
  Monoms::Monom32 abc(a * b * c);

  ZDD<Monoms::Monom32> z1(1), z2(2), z3(3);
  ZDD<Monoms::Monom32> z4 = z1 * z2 * z3;

  REQUIRE(abc == z4.lm());

  ZDD<Monoms::Monom32> z_zero;
  REQUIRE(z_zero.lm().isZero());

  ZDD<Monoms::Monom32> z_one;
  z_one.setOne();
  REQUIRE(z_one.lm().isOne());
}

TEST_CASE("ZDD Addition", "[zdd-add]") {
  ZDD<Monoms::Monom32> a(1), b(2), c(3), d(4);

  ZDD<Monoms::Monom32> p1 = a + a + b + b;
  REQUIRE(p1.isZero());

  ZDD<Monoms::Monom32> p2 = a + c + c + d;

  REQUIRE(a + d == p2);
}

TEST_CASE("ZDD Add Monom", "[zdd-add-monom]") {
  ZDD<Monoms::Monom32> a(1), b(2), c(3), d(4);
  Monoms::Monom32 m_ab;
  m_ab.setVar(1);
  m_ab.setVar(2);

  ZDD<Monoms::Monom32> p = a * b + b + c;

  ZDD<Monoms::Monom32> r = p + m_ab;

  REQUIRE(r == b + c);
}

TEST_CASE("ZDD Multiplication", "[zdd-mul]") {
  ZDD<Monoms::Monom32> a(1), b(2), c(3), d(4);

  ZDD<Monoms::Monom32> p1 = a * a;
  REQUIRE(p1 == a);

  ZDD<Monoms::Monom32> p2 = (a + b + c + d) * b * c;
  REQUIRE(p2 == a * b * c + b * c * d);

  ZDD<Monoms::Monom32> p3 = (a * b + b + c) * a;
  REQUIRE(p3 == a * c);
}

TEST_CASE("ZDD Mult Monom", "[zdd-mul-monom]") {
  ZDD<Monoms::Monom32> a(1), b(2), c(3), d(4);
  Monoms::Monom32 m_a;
  m_a.setVar(1);

  ZDD<Monoms::Monom32> p = a * b + b + c;

  ZDD<Monoms::Monom32> r = p * m_a;
  REQUIRE(r == a * c);
}

TEST_CASE("ZDD Print", "[zdd-print]") {
  ZDD<Monoms::Monom32> a(1), b(2), c(3), d(4);
  ZDD<Monoms::Monom32> p = a + b + c + d;
  REQUIRE(p.toStr() == "[ 1 ] [ 2 ] [ 3 ] [ 4 ] ");

  ZDD<Monoms::Monom32> zero;
  REQUIRE(zero.toStr() == "0");

  ZDD<Monoms::Monom32> one;
  one.setOne();
  REQUIRE(one.toStr() == "1");
}
