INCLUDE_DIRECTORIES(../)

ADD_EXECUTABLE( unittest
    unittest.cpp
    test_monom.cpp
    test_poly.cpp
    test_gb.cpp
)

TARGET_LINK_LIBRARIES( unittest
    cppunit
    boolpoly
)
