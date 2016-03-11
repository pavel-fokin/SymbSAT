INCLUDE_DIRECTORIES(../)

ADD_EXECUTABLE( unittest
    unittest.cpp
    test_monom.cpp
)

TARGET_LINK_LIBRARIES( unittest
    cppunit
    boolpoly
)
