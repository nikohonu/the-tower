cmake_minimum_required(VERSION 3.28)
project(the-tower)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

file(GLOB_RECURSE SRCFILES "src/*.cpp")

add_subdirectory(subprojects/SDL)
add_subdirectory(subprojects/SDL_image)

add_executable(the-tower ${SRCFILES})

target_link_libraries(the-tower SDL3::SDL3 SDL3_image-shared)
