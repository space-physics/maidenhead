cmake_minimum_required(VERSION 3.14...3.25)
project(Maidenhead LANGUAGES Fortran)

enable_testing()

if(CMAKE_Fortran_COMPILER_ID STREQUAL "GNU")
  add_compile_options(-fno-backtrace -fimplicit-none)
endif()

add_library(maidenhead OBJECT src/maidenhead.f90)

add_executable(main app/main.f90)
target_link_libraries(main PRIVATE maidenhead)

add_test(NAME to_location COMMAND main GG52qj)
set_property(TEST to_location PROPERTY PASS_REGULAR_EXPRESSION "(-27.60[0-9]+[ ]+-48.62[0-9]+)")

add_test(NAME to_maiden COMMAND main -27.60 -48.62)
set_property(TEST to_maiden PROPERTY PASS_REGULAR_EXPRESSION "GG52qj")
