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
