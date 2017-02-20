#include <iostream>

#include "catch.hpp"

#include "monomt.h"
#include "polyt.h"
#include "zddt.h"
#include "polyfuncs.h"

using namespace symbsat;

TEST_CASE("S-polynomial PolyZDD", "[spoly-polyzdd]") {
  ZDD<Monoms::Monom32> f, g;
  ZDD<Monoms::Monom32> a(1), b(2), c(3), d(4);
  ZDD<Monoms::Monom32> s, s1, s2;
  ZDD<Monoms::Monom32> _1; _1.setOne();

  s = spoly<ZDD<Monoms::Monom32>>(f, g);
  REQUIRE(s.isZero());

  s1 = spoly<ZDD<Monoms::Monom32>>(a*b*c, a*b + _1);
  REQUIRE(s1 == c);

  s = spoly<ZDD<Monoms::Monom32>>(a*b*c + _1, a*b + _1);

  REQUIRE(s == c + _1);

  ZDD<Monoms::Monom32> f1 = a*b*c + c*d + a*b + _1;
  ZDD<Monoms::Monom32> g1 = c*d + b;

  s = spoly(f1, g1);
  REQUIRE(s == a*b + a*c*d + c*d + _1);
}
