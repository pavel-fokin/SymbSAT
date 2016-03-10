PROJECT (symbsat)

CMAKE_MINIMUM_REQUIRED(VERSION 2.6)

INCLUDE_DIRECTORIES(${PROJECT_BINARY_DIR})

SET(CMAKE_CXX_COMPILER "/usr/bin/clang++-3.6")
SET(CMAKE_CXX_FLAGS "-std=c++11")

ADD_DEFINITIONS(-Wall)

ADD_LIBRARY(boolpoly STATIC
    monom.h
    monom.cpp
    poly.h
    poly.cpp
)

ADD_EXECUTABLE(main main.cpp)

TARGET_LINK_LIBRARIES( main
    boolpoly
)
