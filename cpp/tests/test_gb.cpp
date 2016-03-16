#include <cppunit/extensions/HelperMacros.h>
#include <cppunit/config/SourcePrefix.h>

#include "gb.h"

class TestGB: public CppUnit::TestFixture {
    CPPUNIT_TEST_SUITE(TestGB);

    CPPUNIT_TEST(testBuchberger1);
    CPPUNIT_TEST(testBuchberger3);
    CPPUNIT_TEST(testBuchberger7);

    CPPUNIT_TEST_SUITE_END();
public:
    void setUp() {}
    void tearDown() {}

    void testBuchberger1();
    void testBuchberger3();
    void testBuchberger7();
};

CPPUNIT_TEST_SUITE_REGISTRATION(TestGB);

void TestGB::testBuchberger1() {
    Monom m_x1(1), m_x2(2),
          m_x3(3), m_x4(4), m_one(0);

    Poly x1(m_x1), x2(m_x2),
         x3(m_x3), x4(m_x4), _1(m_one);

    std::vector<Poly> F {
        x1 + x2 + x3 + x4,
        x1*x2 + x2*x3 + x1*x3 + x3*x4,
        x1*x2*x3 + x1*x2*x4 + x1*x3*x4 + x2*x3*x4,
        x1*x2*x3*x4 + _1
    };

    auto G = buchberger(F, 4);

    for (auto& p: G)
        std::cout << p << std::endl;

    CPPUNIT_ASSERT(true);
}

void TestGB::testBuchberger3() {
    Monom m_x1(1), m_x2(2), m_one(0);

    Poly x1(m_x1), x2(m_x2), _1(m_one);

    std::vector<Poly> F {
        x1*x2 + x1,
        x1*x2 + x2
    };

    auto G = buchberger(F, 2);

    for (auto& p: G)
        std::cout << p << std::endl;

    CPPUNIT_ASSERT(true);
}

void TestGB::testBuchberger7() {
    Monom m_x1(1), m_x2(2), m_x3(3), m_one(0);

    Poly x1(m_x1), x2(m_x2), x3(m_x3), _1(m_one);

    std::vector<Poly> F {
        x1*x2*x3,
        x1*x2*x3 + x1*x2,
        x1*x2*x3 + x1*x3,
        x1*x2*x3 + x1*x2 + x1*x3 + x1,
        x1*x2*x3 + x2*x3,
        x1*x2*x3 + x1*x2 + x2*x3 + x2,
        x1*x2*x3 + x1*x3 + x2*x3 + x3,
        x1*x2*x3 + x1*x2 + x1*x3 + x1 + x2*x3 + x2 + x3 + _1
    };

    auto G = buchberger(F, 3);

    for (auto& p: G)
        std::cout << p << std::endl;
}
