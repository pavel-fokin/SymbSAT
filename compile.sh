#!/bin/bash

if [ -d "build" ]; then
    rm -r build
fi

mkdir build
pushd build

cmake ../symbsat-cpp
make -j8
