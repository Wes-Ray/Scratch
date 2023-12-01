cmake_minimum_required(VERSION 3.0)

project(HelloWorld)

file(GLOB_RECURSE sources src/*c)
file(GLOB_RECURSE data resources/*)

add_executable(HelloWorld ${sources} ${data})

target_include_directories(HelloWorld)