PROJECT (symbsat)

CMAKE_MINIMUM_REQUIRED(VERSION 3.1)

# ADD_DEFINITIONS(-std=c++14 -Wall --coverage -g)
ADD_DEFINITIONS(-std=c++17 -Wall -O3)

# We want to generate files with extension *.gcno but not with *.cpp.gcno
SET(CMAKE_CXX_OUTPUT_EXTENSION_REPLACE 1)

# SET(BUILD_COV TRUE)
SET(BUILD_TEST TRUE)

IF (BUILD_TEST)
  ADD_SUBDIRECTORY (tests)
ENDIF (BUILD_TEST)

ADD_EXECUTABLE(satsolver satsolver.cpp)
ADD_EXECUTABLE(gbsolver gbsolver.cpp)

# TARGET_LINK_LIBRARIES( satsolver
#   gcov
# )
