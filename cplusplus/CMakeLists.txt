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


# Google Test
include(FetchContent)
FetchContent_Declare(
    googletest 
    URL https://github.com/google/googletest/archive/03597a01ee50ed33e9dfd640b249b4be3799d395.zip
)
FetchContent_MakeAvailable(googletest)

enable_testing()

option(BUILD_TEST "Build the unit tests" ON)

if(BUILD_TEST)
  set(TEST_SOURCES
      ${SRC_DIR}/vector3D.cpp
      ${TEST_DIR}/test.cpp
  )

  add_executable(${PROJECT_NAME}_test ${TEST_SOURCES})
  target_include_directories(${PROJECT_NAME}_test PRIVATE ${SRC_DIR})
  target_include_directories(${PROJECT_NAME}_test PRIVATE ${HDR_DIR})
  target_include_directories(${PROJECT_NAME} PRIVATE ${TEST_DIR})

  target_link_libraries(
    ${PROJECT_NAME}_test
    GTest::gtest_main
  )

  include(GoogleTest)
  gtest_discover_tests(${PROJECT_NAME}_test)

  set_target_properties(${PROJECT_NAME}_test PROPERTIES RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/test)
endif()