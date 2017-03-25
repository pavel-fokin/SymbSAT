#include <cppunit/extensions/HelperMacros.h>
#include <cppunit/config/SourcePrefix.h>

#include "monom.h"

class TestMonomT: public CppUnit::TestFixture {
    CPPUNIT_TEST_SUITE(TestMonomT);

    CPPUNIT_TEST(testConstructor);
    CPPUNIT_TEST(testOrdering);
    CPPUNIT_TEST(testMul);
    CPPUNIT_TEST(testIsDivisible);
    CPPUNIT_TEST(testDiv);
    CPPUNIT_TEST(testIsRelativelyPrime);
    CPPUNIT_TEST(testGetVars);

    CPPUNIT_TEST_SUITE_END();
public:
    void setUp() {}
    void tearDown() {}

    void testConstructor();
    void testOrdering();
    void testMul();
    void testIsDivisible();
    void testDiv();
    void testIsRelativelyPrime();
    void testGetVars();
};

CPPUNIT_TEST_SUITE_REGISTRATION(TestMonomT);

void TestMonomT::testConstructor() {
    Monoms::Monom64 x0(0), x1(1), x2(2);
}

void TestMonomT::testOrdering() {
    Monoms::Monom64 a(0), b(1), c(2), ab(a*b);
    Monoms::Monom64 _0, _1;
    _1.setOne();

    CPPUNIT_ASSERT(!(a < b));
    CPPUNIT_ASSERT(b < a);
    CPPUNIT_ASSERT(c < a);
    CPPUNIT_ASSERT(!(b < c));
    CPPUNIT_ASSERT(b < ab);
}

void TestMonomT::testMul() {
    Monoms::Monom64 a(0), b(1), c(2), abc;
    Monoms::Monom64 _0, _1;
    _1.setOne();

    abc = a*b*c;

    CPPUNIT_ASSERT(abc == a*b*c);

    CPPUNIT_ASSERT(a*b == b*a);
    CPPUNIT_ASSERT(a*a == a);

    b = a * _1;
    CPPUNIT_ASSERT(a == b);

    b = _1 * a;
    CPPUNIT_ASSERT(a == b);

    b = a * _0;
    CPPUNIT_ASSERT(b.isZero());

    b = _0 * a;
    CPPUNIT_ASSERT(b.isZero());
}

void TestMonomT::testIsDivisible() {
    Monoms::Monom64 a(0), b(1), ab;
    Monoms::Monom64 _0, _1;
    _1.setOne();

    // CPPUNIT_ASSERT(!a.isdivisible(_0));
    // a/1 = a True
    CPPUNIT_ASSERT(a.isdivisible(_1));
    // a/b = 0 False
    CPPUNIT_ASSERT(!a.isdivisible(b));
    // 1/b = 0 False
    CPPUNIT_ASSERT(!_1.isdivisible(b));

    ab = a*b;
    CPPUNIT_ASSERT(ab.isdivisible(a));
    CPPUNIT_ASSERT(ab.isdivisible(b));
}

void TestMonomT::testDiv() {
    Monoms::Monom64 a(0), b(1), c(2);
    Monoms::Monom64 ab(a*b), bc(b*c), abc(a*b*c);
    Monoms::Monom64 _0, _1;
    _1.setOne();

    // b = a/_1;
    // a == a/_1;
    CPPUNIT_ASSERT_EQUAL(a, a/_1);

    // a/b == _0;
    CPPUNIT_ASSERT_EQUAL(_0, a/b);

    // ab/b == a;
    CPPUNIT_ASSERT_EQUAL(a, ab/b);
    // ab/a == b;
    CPPUNIT_ASSERT_EQUAL(b, ab/a);
    // abc/ab == c;
    CPPUNIT_ASSERT_EQUAL(c, abc/ab);
    // ab/bc == 0;
    CPPUNIT_ASSERT_EQUAL(_0, ab/bc);
}

void TestMonomT::testIsRelativelyPrime() {
    Monoms::Monom64 a(0), b(1), ab(a*b);
    Monoms::Monom64 _0, _1;
    _1.setOne();

    CPPUNIT_ASSERT(a.isrelativelyprime(a));
    CPPUNIT_ASSERT(a.isrelativelyprime(_1));
    CPPUNIT_ASSERT(a.isrelativelyprime(b));
    CPPUNIT_ASSERT(!ab.isrelativelyprime(b));
}

void TestMonomT::testGetVars() {
    Monoms::Monom64 a(0), b(1), c(2), d(3);
    Monoms::Monom64 abd(a*b*d);

    std::vector<int> vars {0,1,3};
    CPPUNIT_ASSERT(abd.getVars() == vars);
}
