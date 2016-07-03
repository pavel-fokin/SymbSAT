#include <cppunit/extensions/HelperMacros.h>
#include <cppunit/config/SourcePrefix.h>

#include "zdd.h"

class TestZDD: public CppUnit::TestFixture {
    CPPUNIT_TEST_SUITE(TestZDD);
    CPPUNIT_TEST(testConstructor);
    CPPUNIT_TEST(testConstructorMonom);
    CPPUNIT_TEST(testMonomIterator);
    CPPUNIT_TEST(testZDDLm);
    CPPUNIT_TEST(testZDDEqual);
    CPPUNIT_TEST(testZDDAdd);
    CPPUNIT_TEST(testZDDAddMonom);
    CPPUNIT_TEST(testZDDMul);
    CPPUNIT_TEST(testZDDMulMonom);

    CPPUNIT_TEST_SUITE_END();
public:
    void setUp() {}
    void tearDown() {}

    void testConstructor();
    void testConstructorMonom();
    void testMonomIterator();
    void testZDDLm();
    void testZDDEqual();
    void testZDDAdd();
    void testZDDAddMonom();
    void testZDDMul();
    void testZDDMulMonom();
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

void TestZDD::testConstructorMonom() {
    Monom a(1), b(2), c(3);
    Monom abc(a*b*c);

    ZDD z(abc);
    CPPUNIT_ASSERT_EQUAL(abc, z.lm());

    Monom m_zero;
    ZDD z_zero(m_zero);
    CPPUNIT_ASSERT(z_zero.isZero());

    Monom m_one; m_one.setVar(0);
    ZDD z_one(m_one);
    CPPUNIT_ASSERT(z_one.isOne());
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

void TestZDD::testZDDLm() {
    Monom a(1), b(2), c(3);
    Monom abc(a*b*c);

    ZDD z1(1), z2(2), z3(3);
    ZDD z4 = z1*z2*z3;

    CPPUNIT_ASSERT_EQUAL(abc, z4.lm());

    ZDD z_zero;
    CPPUNIT_ASSERT(z_zero.lm().isZero());

    ZDD z_one; z_one.setOne();
    CPPUNIT_ASSERT(z_one.lm().isOne());
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

void TestZDD::testZDDAddMonom() {
    ZDD a(1), b(2), c(3), d(4);
    Monom m_ab; m_ab.setVar(1); m_ab.setVar(2);

    ZDD p = a*b + b + c;

    ZDD r = p + m_ab;

    CPPUNIT_ASSERT_EQUAL(r, b + c);
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

void TestZDD::testZDDMulMonom() {
    ZDD a(1), b(2), c(3), d(4);
    Monom m_a; m_a.setVar(1);

    ZDD p = a*b + b + c;

    ZDD r = p * m_a;
    CPPUNIT_ASSERT_EQUAL(r, a*c);
}
