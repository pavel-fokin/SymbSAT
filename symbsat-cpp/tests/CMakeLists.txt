INCLUDE_DIRECTORIES(../)

ADD_EXECUTABLE( unittest
    unittest.cpp
    test_monom.cpp
    test_poly.cpp
    test_gb.cpp
    test_zdd.cpp
)
TARGET_LINK_LIBRARIES( unittest
    boolpoly
    cppunit
    gcov
)

ADD_EXECUTABLE( catch_tests
    catch.hpp
    catch_tests.cpp
    catch_test_monomt.cpp
    catch_test_polyt.cpp
    catch_test_zddt.cpp
    test_polyfuncs.cpp
    test_gbt.cpp
)

TARGET_LINK_LIBRARIES( catch_tests
    boolpoly
    gcov
)
