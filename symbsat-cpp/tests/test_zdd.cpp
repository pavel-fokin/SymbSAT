#include <cppunit/extensions/HelperMacros.h>
#include <cppunit/config/SourcePrefix.h>

#include "zdd.h"

class TestZDD: public CppUnit::TestFixture {
    CPPUNIT_TEST_SUITE(TestZDD);
    CPPUNIT_TEST(testConstructor);
    CPPUNIT_TEST(testMonomIterator);
    CPPUNIT_TEST(testZDDEqual);
    CPPUNIT_TEST(testZDDAdd);
    CPPUNIT_TEST(testZDDMul);

    CPPUNIT_TEST_SUITE_END();
public:
    void setUp() {}
    void tearDown() {}

    void testConstructor();
    void testMonomIterator();
    void testZDDEqual();
    void testZDDAdd();
    void testZDDMul();
};

CPPUNIT_TEST_SUITE_REGISTRATION(TestZDD);

void TestZDD::testConstructor() {

    ZDD z;
    CPPUNIT_ASSERT(z.isZero());

    ZDD z1(1), z2(2);
    CPPUNIT_ASSERT( !(z1 == z2) );

    ZDD z3(z1);
    CPPUNIT_ASSERT( z1 == z3 );

    ZDD z4 = z2;
    CPPUNIT_ASSERT( z4 == z2 );

    ZDD z5(5), z6;
    CPPUNIT_ASSERT( !(z5 == z6) );

    z5 = z6;
    CPPUNIT_ASSERT( z5 == z6 );
}

void TestZDD::testMonomIterator() {
    ZDD z1(1), z2(2);
    ZDD z3 = z1*z2 + z2;

    ZDD::MonomConstIterator it(z3);

    while(!it) {
        ++it;
    }

    CPPUNIT_ASSERT(true);
}

void TestZDD::testZDDEqual() {
    ZDD a(1), b(2), c(3), d(4);

    CPPUNIT_ASSERT( a == a );
    CPPUNIT_ASSERT( b == b );
    CPPUNIT_ASSERT( !(a == b) );

    ZDD p1 = a + b;
    ZDD p2 = a + b;
    CPPUNIT_ASSERT( p1 == p2 );

    ZDD p3 = a + b;
    ZDD p4 = a + b + c;
    CPPUNIT_ASSERT( !(p3 == p4) );
}

void TestZDD::testZDDAdd() {
    ZDD a(1), b(2), c(3), d(4);

    ZDD p1 = a + a + b + b;

    CPPUNIT_ASSERT(p1.isZero());

    ZDD p2 = a + c + c + d;

    CPPUNIT_ASSERT_EQUAL(a + d, p2);
}

void TestZDD::testZDDMul() {
    ZDD a(1), b(2), c(3), d(4);

    ZDD p1 = a*a;

    CPPUNIT_ASSERT_EQUAL(a, p1);

    ZDD p2 = (a + b + c + d) * b*c;
    CPPUNIT_ASSERT_EQUAL(a*b*c + b*c*d, p2);

    ZDD p3 = (a*b + b + c) * a;
    CPPUNIT_ASSERT_EQUAL(a*c, p3);
}
