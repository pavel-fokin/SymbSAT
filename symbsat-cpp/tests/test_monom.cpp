#include <cppunit/extensions/HelperMacros.h>
#include <cppunit/config/SourcePrefix.h>

#include "monom.h"

class TestMonom: public CppUnit::TestFixture {
    CPPUNIT_TEST_SUITE(TestMonom);

    CPPUNIT_TEST(testConstructor);
    CPPUNIT_TEST(testOrdering);
    CPPUNIT_TEST(testMul);
    CPPUNIT_TEST(testIsDivisible);
    CPPUNIT_TEST(testDiv);
    CPPUNIT_TEST(testIsRelativelyPrime);

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
};

CPPUNIT_TEST_SUITE_REGISTRATION(TestMonom);

void TestMonom::testConstructor() {
    Monom m1, _1(0);

    CPPUNIT_ASSERT(m1.isZero());
    CPPUNIT_ASSERT(_1.isOne());
}

void TestMonom::testOrdering() {
    Monom _0, _1(0), a(1), b(2), c(3), ab(a*b);

    CPPUNIT_ASSERT(!(a < b));
    CPPUNIT_ASSERT(b < a);
    CPPUNIT_ASSERT(c < a);
    CPPUNIT_ASSERT(!(b < c));
    CPPUNIT_ASSERT(b < ab);
}

void TestMonom::testMul() {
    Monom _0, _1(0),
          a(1), b(2), c(3),
          abc;

    b = _1*a;
    CPPUNIT_ASSERT(a == b);

    b = a*_1;
    CPPUNIT_ASSERT(a == b);

    b = a*_0;
    CPPUNIT_ASSERT(b.isZero());

    b = _0*a;
    CPPUNIT_ASSERT(b.isZero());

    CPPUNIT_ASSERT(a*b == b*a);
    CPPUNIT_ASSERT(a*a == a);

    abc = a*b*c;

    CPPUNIT_ASSERT(abc == a*b*c);
}

void TestMonom::testIsDivisible() {
    Monom _0, _1(0), a(1), b(2), ab;

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

void TestMonom::testDiv() {
    Monom _0, _1(0),
          a(1), b(2), c(3),
          ab(a*b), bc(b*c), abc(a*b*c);

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

void TestMonom::testIsRelativelyPrime() {
    Monom _0, _1(0), a(1), b(2), ab = a*b;

    CPPUNIT_ASSERT(a.isrelativelyprime(a));
    CPPUNIT_ASSERT(a.isrelativelyprime(_1));
    CPPUNIT_ASSERT(a.isrelativelyprime(b));
    CPPUNIT_ASSERT(!ab.isrelativelyprime(b));
}