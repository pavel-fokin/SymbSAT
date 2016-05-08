#include <cppunit/extensions/HelperMacros.h>
#include <cppunit/config/SourcePrefix.h>

#include "zdd.h"

class TestZDD: public CppUnit::TestFixture {
    CPPUNIT_TEST_SUITE(TestZDD);
    CPPUNIT_TEST(testConstructor);
    CPPUNIT_TEST(testMonomIterator);

    CPPUNIT_TEST_SUITE_END();
public:
    void setUp() {}
    void tearDown() {}

    void testConstructor();
    void testMonomIterator();
};

CPPUNIT_TEST_SUITE_REGISTRATION(TestZDD);

void TestZDD::testConstructor() {
    ZDD z1(1), z2(2);
    ZDD z3(z1);
    ZDD z4 = z2;

    std::cout << "zdd\n";

    CPPUNIT_ASSERT(true);
}

void TestZDD::testMonomIterator() {
    ZDD z1(1), z2(2);
    ZDD z3 = z1*z2 + z2;

    ZDD::MonomConstIterator it(z3);

    while(!it) {
        std::cout << it.monom() << "\n";
        ++it;
    }


    CPPUNIT_ASSERT(true);
}
