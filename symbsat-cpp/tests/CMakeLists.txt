INCLUDE_DIRECTORIES(../)

ADD_EXECUTABLE( unittests
    catch.hpp
    unittests.cpp
    test_monom.cpp
    test_poly.cpp
    test_zdd.cpp
    test_polyfuncs.cpp
    test_gb.cpp
)

TARGET_LINK_LIBRARIES( unittests
    gcov
)
