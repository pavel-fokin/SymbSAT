PROJECT (symbsat)

CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

ADD_DEFINITIONS(-std=c++14 -Wall --coverage -g)
# ADD_DEFINITIONS(-std=c++14 -O3)

# We want to generate files with extension *.gcno but not with *.cpp.gcno
SET(CMAKE_CXX_OUTPUT_EXTENSION_REPLACE 1)

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

ADD_EXECUTABLE(satsolver satsolver.cpp)

TARGET_LINK_LIBRARIES( satsolver
  gcov
)
