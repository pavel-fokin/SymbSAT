#include "catch.hpp"

#include "monom.h"
#include "poly.h"
#include "zdd.h"
#include "polyfuncs.h"

using namespace symbsat;

TEST_CASE("S-polynomial PolyZDD", "[spoly-polyzdd]") {
  ZDD<Monom32> f, g;
  ZDD<Monom32> a(1), b(2), c(3), d(4);
  ZDD<Monom32> s, s1, s2;
  ZDD<Monom32> _1; _1.setOne();

  s = spoly<ZDD<Monom32>>(f, g);
  REQUIRE(s.isZero());

  s1 = spoly<ZDD<Monom32>>(a*b*c, a*b + _1);
  REQUIRE(s1 == c);

  s = spoly<ZDD<Monom32>>(a*b*c + _1, a*b + _1);

  REQUIRE(s == c + _1);

  ZDD<Monom32> f1 = a*b*c + c*d + a*b + _1;
  ZDD<Monom32> g1 = c*d + b;

  s = spoly(f1, g1);
  REQUIRE(s == a*b + a*c*d + c*d + _1);
}

TEST_CASE("S-polynomial PolyList", "[spoly-polylist]") {
  Poly<Monom32> f, g;
  Poly<Monom32> a(1), b(2), c(3), d(4);
  Poly<Monom32> s, s1, s2, s3;
  Poly<Monom32> _1; _1.setOne();

  s = spoly<Poly<Monom32>>(f, g);
  REQUIRE(s.isZero());

  s1 = spoly<Poly<Monom32>>(a*b*c, a*b + _1);
  REQUIRE(s1 == c);

  s2 = spoly<Poly<Monom32>>(a*b*c + _1, a*b + _1);

  REQUIRE(s == c + _1);

  Poly<Monom32> f1 = a*b*c + c*d + a*b + _1;
  Poly<Monom32> g1 = c*d + b;

  s3 = spoly(f1, g1);
  REQUIRE(s == a*b + a*c*d + c*d + _1);
}

TEST_CASE("NormalForm 1 PolyList", "[normalform-polylist]") {
  Poly<Monom32> x1(1), x2(2),
                x3(3), x4(4), _1;
  _1.setOne();

  Poly<Monom32> p = x1*x2*x3 + x1*x2*x4 + x1*x3*x4 + x3;
  Poly<Monom32> p_nf;

  std::vector<Poly<Monom32>> F {
      x1 + x2 + x3 + x4,
      x1*x2 + x2*x3 + x1*x3 + x3*x4,
      x1*x2*x3 + x1*x2*x4 + x1*x3*x4 + x2*x3*x4,
      x1*x2*x3*x4 + _1
  };

  p_nf = normalform(p, F);

  REQUIRE(p_nf == x2*x3*x4 + x3);
}

TEST_CASE("NormalForm 1 PolyZDD", "[normalform-polyzdd]") {
  ZDD<Monom32> x1(1), x2(2),
               x3(3), x4(4), _1;
  _1.setOne();

  ZDD<Monom32> p = x1*x2*x3 + x1*x2*x4 + x1*x3*x4 + x3;
  ZDD<Monom32> p_nf;

  std::vector<ZDD<Monom32>> F {
      x1 + x2 + x3 + x4,
      x1*x2 + x2*x3 + x1*x3 + x3*x4,
      x1*x2*x3 + x1*x2*x4 + x1*x3*x4 + x2*x3*x4,
      x1*x2*x3*x4 + _1
  };

  p_nf = normalform(p, F);

  REQUIRE(p_nf == x2*x3*x4 + x3);
}

TEST_CASE("NormalForm 2 PolyList", "[normalform2-polylist]") {
  Poly<Monom32> x1(1), x2(2),
                x3(3), x4(4), _1;
  _1.setOne();

  Poly<Monom32> p = x1*x2*x3 + x1*x2*x4 + x1*x3*x4 + x3;
  Poly<Monom32> p_nf;

  std::vector<Poly<Monom32>> F {
    x1 + _1,
    x2 + _1,
    x3 + _1,
    x4 + _1
  };

  p_nf = normalform(p, F);

  REQUIRE(p_nf.isZero());
}

TEST_CASE("NormalForm 2 PolyZDD", "[normalform2-polyzdd]") {
  ZDD<Monom32> x1(1), x2(2),
               x3(3), x4(4), _1;
  _1.setOne();

  ZDD<Monom32> p = x1*x2*x3 + x1*x2*x4 + x1*x3*x4 + x3;
  ZDD<Monom32> p_nf;

  std::vector<ZDD<Monom32>> F {
    x1 + _1,
    x2 + _1,
    x3 + _1,
    x4 + _1
  };

  p_nf = normalform(p, F);

  REQUIRE(p_nf.isZero());
}

TEST_CASE("NormalForm 3 PolyList", "[normalform3-polylist]") {
  Poly<Monom32> x1(1), x2(2),
                x3(3), x4(4), _1;
  _1.setOne();

  Poly<Monom32> p = x2*x3*x4 + _1;
  Poly<Monom32> p_nf;

  std::vector<Poly<Monom32>> F {
    x1 + x2 + x3 + x4,
    x1*x2 + x2*x3 + x1*x3 + x3*x4,
    x1*x2*x3 + x1*x2*x4 + x1*x3*x4 + x2*x3*x4,
    x1*x2*x3*x4 + _1,
    x2 + x4
  };

  p_nf = normalform(p, F);

  REQUIRE(p_nf == x3*x4 + _1);
}

TEST_CASE("NormalForm 3 PolyZDD", "[normalform3-polyzdd]") {
  ZDD<Monom32> x1(1), x2(2),
               x3(3), x4(4), _1;
  _1.setOne();

  ZDD<Monom32> p = x2*x3*x4 + _1;
  ZDD<Monom32> p_nf;

  std::vector<ZDD<Monom32>> F {
    x1 + x2 + x3 + x4,
    x1*x2 + x2*x3 + x1*x3 + x3*x4,
    x1*x2*x3 + x1*x2*x4 + x1*x3*x4 + x2*x3*x4,
    x1*x2*x3*x4 + _1,
    x2 + x4
  };

  p_nf = normalform(p, F);

  REQUIRE(p_nf == x3*x4 + _1);
}

TEST_CASE("NormalForm 4 PolyZDD", "[normalform4-polyzdd]") {
  ZDD<Monom32> x1(1), x2(2),
               x3(3), x4(4), _1;
  _1.setOne();

  ZDD<Monom32> p = x1 + x2;
  ZDD<Monom32> p_nf;

  std::vector<ZDD<Monom32>> F {
    x2 + x4,
    x4 + _1
  };

  p_nf = normalform(p, F);

  REQUIRE(p_nf == x1 + _1);
}

TEST_CASE("NormalForm 4 PolyList", "[normalform4-polylist]") {
  Poly<Monom32> x1(1), x2(2),
                x3(3), x4(4), _1;
  _1.setOne();

  Poly<Monom32> p = x1 + x2;
  Poly<Monom32> p_nf;

  std::vector<Poly<Monom32>> F {
    x2 + x4,
    x4 + _1
  };

  p_nf = normalform(p, F);

  REQUIRE(p_nf == x1 + _1);
}
