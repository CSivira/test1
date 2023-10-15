cmake_minimum_required(VERSION 3.5)
project(Vector3D)

# Compilation
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED YES)
set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# Source files and libraries paths
set(SRC_DIR ${CMAKE_CURRENT_SOURCE_DIR}/src)
set(HDR_DIR ${CMAKE_CURRENT_SOURCE_DIR}/include)
set(TEST_DIR ${CMAKE_CURRENT_SOURCE_DIR}/test)
set(SOURCES
    ${SRC_DIR}/main.cpp
    ${SRC_DIR}/vector3D.cpp
)

add_executable(${PROJECT_NAME} ${SOURCES})
target_include_directories(${PROJECT_NAME} PRIVATE ${SRC_DIR})
target_include_directories(${PROJECT_NAME} PRIVATE ${HDR_DIR})