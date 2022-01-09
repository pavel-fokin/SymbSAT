#include "catch.hpp"

#include <iostream>

#include "monom.h"
#include "order.h"

using namespace symbsat;

typedef Monom<32> Monom32;

TEST_CASE("Monoms Lex Order", "[order-lex]") {
  Monom32 a(0), b(1), c(2), d(3);
  Monom32 _0, _1; _1.setOne();

  // 0 < a
  REQUIRE(Lex<Monom32>::lt(_0, a));
  // not a < 0
  REQUIRE(!Lex<Monom32>::lt(a, _0));
  // 0 < 1
  // REQUIRE(Lex<Monom32>::lt(_0, _1));
  // not 0 < 0
  REQUIRE(!Lex<Monom32>::lt(_0, _0));

  REQUIRE(!Lex<Monom32>::lt(a, _1));
  REQUIRE(Lex<Monom32>::lt(_1, a));
  REQUIRE(!Lex<Monom32>::lt(_1, _1));

  REQUIRE(!Lex<Monom32>::lt(a, a));
  REQUIRE(!Lex<Monom32>::lt(a, b));
  REQUIRE(Lex<Monom32>::lt(b, a));
  REQUIRE(!Lex<Monom32>::lt(b, b));

  Monom32 ab(a*b), bc(b*c);
  // bc < a < ab
  REQUIRE(Lex<Monom32>::lt(a, ab));
  REQUIRE(Lex<Monom32>::lt(bc, a));
  REQUIRE(Lex<Monom32>::lt(bc, ab));

  Monom32 abc(a*b*c), bcd(b*c*d);
  // bcd < abc
  REQUIRE(Lex<Monom32>::lt(bcd, abc));
  REQUIRE(!Lex<Monom32>::lt(abc, bcd));

}

TEST_CASE("Monoms DegLex Order", "[order-deglex]") {
  Monom32 a(0), b(1), c(2), d(3);
  Monom32 _0, _1; _1.setOne();

  // 0 < a
  REQUIRE(DegLex<Monom32>::lt(_0, a));
  // not a < 0
  REQUIRE(!DegLex<Monom32>::lt(a, _0));
  // 0 < 1
  // REQUIRE(DegLex<Monom32>::lt(_0, _1));
  // not 0 < 0
  REQUIRE(!DegLex<Monom32>::lt(_0, _0));

  REQUIRE(DegLex<Monom32>::lt(_1, a));
  REQUIRE(!DegLex<Monom32>::lt(a, _1));
  REQUIRE(!DegLex<Monom32>::lt(_1, _1));

  REQUIRE(!DegLex<Monom32>::lt(a, a));
  REQUIRE(!DegLex<Monom32>::lt(a, b));
  REQUIRE(DegLex<Monom32>::lt(b, a));
  REQUIRE(!DegLex<Monom32>::lt(b, b));

  Monom32 ab(a*b), bc(b*c);
  // a < bc < ab
  REQUIRE(DegLex<Monom32>::lt(a, ab));
  REQUIRE(DegLex<Monom32>::lt(a, bc));
  REQUIRE(DegLex<Monom32>::lt(bc, ab));

  Monom32 abc(a*b*c), bcd(b*c*d);
  // bcd < abc
  REQUIRE(DegLex<Monom32>::lt(bcd, abc));
  REQUIRE(!DegLex<Monom32>::lt(abc, bcd));

}

TEST_CASE("Monoms DegRevLex Order", "[order-degrevlex]") {
  Monom32 a(0), b(1), c(2), d(3);
  Monom32 _0, _1; _1.setOne();

  // 0 < a
  REQUIRE(DegRevLex<Monom32>::lt(_0, a));
  // not a < 0
  REQUIRE(!DegRevLex<Monom32>::lt(a, _0));
  // 0 < 1
  // REQUIRE(DegRevLex<Monom32>::lt(_0, _1));
  // not 0 < 0
  REQUIRE(!DegRevLex<Monom32>::lt(_0, _0));

  REQUIRE(DegRevLex<Monom32>::lt(_1, a));
  REQUIRE(!DegRevLex<Monom32>::lt(a, _1));
  REQUIRE(!DegRevLex<Monom32>::lt(_1, _1));

  // REQUIRE(!DegRevLex<Monom32>::lt(a, a));
  REQUIRE(DegRevLex<Monom32>::lt(a, b));
  REQUIRE(!DegRevLex<Monom32>::lt(b, a));
  REQUIRE(!DegRevLex<Monom32>::lt(b, b));

  Monom32 ab(a*b), bc(b*c);
  // a < ab < bc
  REQUIRE(DegRevLex<Monom32>::lt(a, ab));
  REQUIRE(DegRevLex<Monom32>::lt(a, bc));
  REQUIRE(DegRevLex<Monom32>::lt(ab, bc));

  Monom32 abc(a*b*c), bcd(b*c*d);
  // bcd < abc
  REQUIRE(!DegRevLex<Monom32>::lt(bcd, abc));
  REQUIRE(DegRevLex<Monom32>::lt(abc, bcd));

}
