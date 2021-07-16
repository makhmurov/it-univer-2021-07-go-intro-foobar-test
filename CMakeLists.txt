cmake_minimum_required(VERSION 3.0.0)
project(foobar VERSION 0.1.0 LANGUAGES C)

#include(CTest)
#enable_testing()

set(CMAKE_BUILD_TYPE RelWithDebInfo)

add_compile_definitions(_CRT_SECURE_CPP_OVERLOAD_STANDARD_NAMES=1)
add_compile_definitions(_CRT_SECURE_NO_WARNINGS=1)

add_executable(foobar foobar.c)

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)
