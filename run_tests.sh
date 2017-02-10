#!/bin/bash

echo "Build and Run Tests"

echo "C++ Tests"
echo "========="

if [ -d "build" ]; then
    rm -r build
fi
mkdir build
mkdir build/cov
pushd build
export GCOV_PREFIX="`pwd`/cov"
export GCOV_PREFIXSTRIP=20
cmake ../symbsat-cpp
make -j8
tests/unittest
tests/catch_tests
popd
find -name *.gcno -exec cp {} build/cov \; &>/dev/null
find -name *.gcda -exec cp {} build/cov \; &>/dev/null
pushd build/cov
gcov -o . -s ../../symbsat-cpp * &>/dev/null
popd

echo
echo "Python Tests"
echo "============"
pushd symbsat-py
python3 -m unittest tests/test_*.py
popd
