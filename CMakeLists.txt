cmake_minimum_required(VERSION 3.15)
project(Maidenhead LANGUAGES Fortran)

enable_testing()

if(CMAKE_Fortran_COMPILER_ID STREQUAL GNU)
  add_compile_options(-fno-backtrace)
endif()

add_library(maidenhead OBJECT maidenhead.f90)

add_executable(test_maidenhead test_maidenhead.f90)
target_link_libraries(test_maidenhead PRIVATE maidenhead)
