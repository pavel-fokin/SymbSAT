PROJECT (symbsat)

CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

ADD_DEFINITIONS(-std=c++14 -Wall --coverage -g)

# We want to generate files with extension *.gcno but not with *.cpp.gcno
SET(CMAKE_CXX_OUTPUT_EXTENSION_REPLACE 1)

SET(BUILD_TEST TRUE)

IF (BUILD_TEST)
  ADD_SUBDIRECTORY (tests)
ENDIF (BUILD_TEST)

ADD_EXECUTABLE(satsolver satsolver.cpp)

TARGET_LINK_LIBRARIES( satsolver
  gcov
)
