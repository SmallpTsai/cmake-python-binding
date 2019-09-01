cmake_minimum_required (VERSION 3.8)    # must be 3.8 or higher to support swig
project (demo)

# default to "Release" mode if not specified

if(NOT CMAKE_BUILD_TYPE) 
    set(CMAKE_BUILD_TYPE Release)
endif(NOT CMAKE_BUILD_TYPE)
message(STATUS "CMAKE_BUILD_TYPE = ${CMAKE_BUILD_TYPE}")

# env setting

set(EXECUTABLE_OUTPUT_PATH ${CMAKE_BINARY_DIR}/bin)
set(LIBRARY_OUTPUT_PATH ${CMAKE_BINARY_DIR}/lib)

# language
set(CMAKE_C_STANDARD 11)
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -fPIC")

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -DDEBUG -Wall -O0 -g -Wno-unknown-pragmas")
set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} -DNDEBUG -Wall -O3")

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fPIC -DUSE_ASIO -std=c++11")

set(PUBLIC_INCLUDE_DIR ${PROJECT_SOURCE_DIR}/inc)
set(SRC_DIR ${PROJECT_SOURCE_DIR}/src)
set(PYSRC_DIR ${PROJECT_SOURCE_DIR}/pysrc)

# optional package
# find_package(OpenSSL)
# find_package(ZLIB)

# include the subdirectory
add_subdirectory (src)
add_subdirectory (inc)
add_subdirectory (pysrc)


