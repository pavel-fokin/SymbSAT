#include <cppunit/extensions/HelperMacros.h>
#include <cppunit/config/SourcePrefix.h>

#include "poly.h"

class TestPoly: public CppUnit::TestFixture {
    CPPUNIT_TEST_SUITE(TestPoly);

    CPPUNIT_TEST(testConstructor);
    CPPUNIT_TEST(testAdd);
    CPPUNIT_TEST(testMul);
    CPPUNIT_TEST(testSpoly);
    CPPUNIT_TEST(testNormalForm1);
    CPPUNIT_TEST(testNormalForm2);

    CPPUNIT_TEST_SUITE_END();
public:
    void setUp() {}
    void tearDown() {}

    void testConstructor();
    void testAdd();
    void testMul();
    void testSpoly();
    void testNormalForm1();
    void testNormalForm2();
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

void TestPoly::testSpoly() {
    Monom m_a(1), m_b(2),
          m_c(3), m_d(4), m_one(0);
    Poly a(m_a), b(m_b),
         c(m_c), d(m_d),
         _1(m_one);

    Poly s1, s2;

    s1 = spoly(a*b*c, a*b + _1);
    s2 = spoly(a*b*c + _1, a*b + _1);

}

void TestPoly::testNormalForm1() {
    Monom m_x1(1), m_x2(2),
          m_x3(3), m_x4(4), m_one(0);

    Poly x1(m_x1), x2(m_x2),
         x3(m_x3), x4(m_x4), _1(m_one);

    Poly p = x1*x2*x3 + x1*x2*x4 + x1*x3*x4 + x3;
    Poly p_nf;

    std::vector<Poly> F {
        x1 + x2 + x3 + x4,
        x1*x2 + x2*x3 + x1*x3 + x3*x4,
        x1*x2*x3 + x1*x2*x4 + x1*x3*x4 + x2*x3*x4,
        x1*x2*x3*x4 + _1
    };

    p_nf = normalform(p, F);

    // TODO x1x2x3 + x2
    std::cout << std::endl << p_nf << std::endl;
}

void TestPoly::testNormalForm2() {
    Monom m_x1(1), m_x2(2),
          m_x3(3), m_x4(4), m_one(0);

    Poly x1(m_x1), x2(m_x2),
         x3(m_x3), x4(m_x4), _1(m_one);

    Poly p = x1*x2*x3 + x1*x2*x4 + x1*x3*x4 + x3;
    Poly p_nf;

    std::vector<Poly> F {
        x1 + _1,
        x2 + _1,
        x3 + _1,
        x4 + _1
    };
    p_nf = normalform(p, F);
    std::cout << std::endl << p_nf << std::endl;
}
