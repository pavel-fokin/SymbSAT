#include <cppunit/extensions/HelperMacros.h>
#include <cppunit/config/SourcePrefix.h>

#include "gb.h"

class TestGB: public CppUnit::TestFixture {
    CPPUNIT_TEST_SUITE(TestGB);

    CPPUNIT_TEST(testBuchberger1);

    CPPUNIT_TEST_SUITE_END();
public:
    void setUp() {}
    void tearDown() {}

    void testBuchberger1();
};

CPPUNIT_TEST_SUITE_REGISTRATION(TestGB);

void TestGB:testBuchberger1() {
    CPPUNIT_ASSERT(true);
}
