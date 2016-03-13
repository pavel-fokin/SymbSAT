#include <cppunit/extensions/HelperMacros.h>
#include <cppunit/config/SourcePrefix.h>

#include "poly.h"

class TestPoly: public CppUnit::TestFixture {
    CPPUNIT_TEST_SUITE(TestPoly);

    CPPUNIT_TEST(testConstructor);
    CPPUNIT_TEST(testAdd);
    CPPUNIT_TEST(testMul);

    CPPUNIT_TEST_SUITE_END();
public:
    void setUp() {}
    void tearDown() {}

    void testConstructor();
    void testAdd();
    void testMul();
};

CPPUNIT_TEST_SUITE_REGISTRATION(TestPoly);

void TestPoly::testConstructor() {
    Monom a(1), b(2), c(3);
    Poly p1, p2(a), p3({c, a, b});

    std::vector<Monom> monoms {b, c, a};
    Poly p4(monoms);

    CPPUNIT_ASSERT(true);
}

void TestPoly::testAdd() {
    Monom a(1), b(2);
    Poly p_a(a), p_b(b), p_ab, p_aa;

    p_ab = p_a + p_b;
    p_aa = p_a + p_a;
    CPPUNIT_ASSERT(p_aa.isZero());
}

void TestPoly::testMul() {
    Monom a(1), b(2), c(3);

    Poly p_a(a), p_b(b), p_c(c), p_abc;

    p_abc = p_a + p_b + p_c;
    p_abc = p_abc*c;
}
