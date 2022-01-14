#include "catch.hpp"

#include "monom.h"
#include "zdd.h"

using namespace symbsat;

typedef Monom<32> Monom32;

TEST_CASE("ZDD MonomIterator", "[zdd-monom-iter]") {
  ZDD<Monom32> z1(1), z2(2);
  ZDD<Monom32> z3 = z1 * z2 + z2;

  ZDD<Monom32>::MonomConstIterator it1(z3);

  while (!it1) {
    ++it1;
  }

  ZDD<Monom32> z4;
  ZDD<Monom32>::MonomConstIterator it2(z4);

  while (!it2) {
    ++it2;
  }

  REQUIRE(true);
}

TEST_CASE("ZDD Constructor", "[zdd-constructor]") {
  ZDD<Monom32> z;
  REQUIRE(z.isZero());

  ZDD<Monom32> z1(1), z2(2);
  REQUIRE(!(z1 == z2));

  ZDD<Monom32> z3(z1);
  REQUIRE(z1 == z3);

  ZDD<Monom32> z4 = z2;
  REQUIRE(z4 == z2);

  ZDD<Monom32> z5(5), z6;
  REQUIRE(!(z5 == z6));

  z5 = z6;
  REQUIRE(z5 == z6);
}

TEST_CASE("ZDD Constructor of Monoms", "[zdd-constructor-monom]") {
  Monom32 a(1), b(2), c(3);
  Monom32 abc(a * b * c);

  ZDD<Monom32> z(abc);
  REQUIRE(abc == z.lm());

  Monom32 m_zero;
  ZDD<Monom32> z_zero(m_zero);
  REQUIRE(z_zero.isZero());

  Monom32 m_one;
  m_one.setOne();
  ZDD<Monom32> z_one(m_one);
  REQUIRE(z_one.isOne());
}

TEST_CASE("ZDD LM", "[zdd-lm]") {
  Monom32 a(1), b(2), c(3);
  Monom32 abc(a * b * c);

  ZDD<Monom32> z1(1), z2(2), z3(3);
  ZDD<Monom32> z4 = z1 * z2 * z3;

  REQUIRE(abc == z4.lm());

  ZDD<Monom32> z_zero;
  REQUIRE(z_zero.lm().isZero());

  ZDD<Monom32> z_one;
  z_one.setOne();
  REQUIRE(z_one.lm().isOne());
}

TEST_CASE("ZDD Addition", "[zdd-add]") {
  ZDD<Monom32> a(1), b(2), c(3), d(4), _1;
  _1.setOne();

  // ZDD<Monom32> p1 = a + a + b + b;
  // REQUIRE(p1.isZero());

  // ZDD<Monom32> p2 = a + c + c + d;
  // REQUIRE(a + d == p2);

  // ZDD<Monom32> p3;
  // p3 = a*(b + _1);
  ZDD<Monom32> p1 = a*b + a;
  ZDD<Monom32> p2 = c + _1;
  ZDD<Monom32> p3 = p1 * p2;
}

TEST_CASE("ZDD Add Monom", "[zdd-add-monom]") {
  ZDD<Monom32> a(1), b(2), c(3), d(4);
  Monom32 m_ab;
  m_ab.setVar(1);
  m_ab.setVar(2);

  ZDD<Monom32> p = a * b + b + c;

  ZDD<Monom32> r = p + m_ab;

  REQUIRE(r == b + c);
}

TEST_CASE("ZDD Multiplication", "[zdd-mul]") {
  ZDD<Monom32> a(1), b(2), c(3), d(4);

  ZDD<Monom32> p1 = a * a;
  REQUIRE(p1 == a);

  ZDD<Monom32> p2 = (a + b + c + d) * b * c;
  REQUIRE(p2 == a * b * c + b * c * d);

  ZDD<Monom32> p3 = (a * b + b + c) * a;
  REQUIRE(p3 == a * c);
}

TEST_CASE("ZDD Mult Monom", "[zdd-mul-monom]") {
  ZDD<Monom32> a(1), b(2), c(3), d(4);
  Monom32 m_a;
  m_a.setVar(1);

  ZDD<Monom32> p = a * b + b + c;

  ZDD<Monom32> r = p * m_a;
  REQUIRE(r == a * c);
}

TEST_CASE("ZDD Print", "[zdd-print]") {
  ZDD<Monom32> a(1), b(2), c(3), d(4);
  ZDD<Monom32> p = a + b + c + d;
  REQUIRE(p.toStr() == "[ 1 ] [ 2 ] [ 3 ] [ 4 ] ");

  ZDD<Monom32> zero;
  REQUIRE(zero.toStr() == "0");

  ZDD<Monom32> one;
  one.setOne();
  REQUIRE(one.toStr() == "1");
}

TEST_CASE("ZDD Count Nodes", "[zdd-count-nodes]") {
  ZDD<Monom32> x(1), y(2), z(3);
  ZDD<Monom32> _1; _1.setOne();
  ZDD<Monom32> p1, p2, p3;

  p1 = x*y*z + x;
  p2 = x*y*z + y;
  p3 = (x + _1)*(y + _1)*(z + _1);

  REQUIRE(x.count_nodes() == 1);
  REQUIRE(p1.count_nodes() == 9);
  REQUIRE(p2.count_nodes() == 10);
  REQUIRE(p3.count_nodes() == 12);

}
