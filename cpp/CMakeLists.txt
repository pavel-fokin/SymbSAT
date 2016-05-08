PROJECT (symbsat)

CMAKE_MINIMUM_REQUIRED(VERSION 2.6)

# SET(CMAKE_CXX_COMPILER "/usr/bin/clang++")
SET(CMAKE_CXX_FLAGS "-std=c++11")

ADD_DEFINITIONS(-Wall)

SET(BUILD_TEST TRUE)

IF (BUILD_TEST)
  FIND_LIBRARY (CPPUNIT cppunit)
  FIND_PATH (CPPUNIT_HEADERS cppunit/TestRunner.h)
  IF (CPPUNIT AND CPPUNIT_HEADERS)
    MESSAGE("-- Looking for Cppunit - found")
  ELSE (CPPUNIT AND CPPUNIT_HEADERS )
    MESSAGE( FATAL_ERROR "-- Looking for Cppunit - not found")
  ENDIF (CPPUNIT AND CPPUNIT_HEADERS )
  ADD_SUBDIRECTORY (tests)
ENDIF (BUILD_TEST)

ADD_LIBRARY(boolpoly STATIC
    monom.h
    monom.cpp
    poly.h
    poly.cpp
    zdd.h
    zdd.cpp
    gb.h
    gb.cpp
)

ADD_EXECUTABLE(cnfread cnfread.cpp)

TARGET_LINK_LIBRARIES( cnfread 
  boolpoly
)

