cmake_minimum_required(VERSION 3.1)
project(main)

#Set Source Code Path
set(SRC_PATH src)
set(${PROJECT_NAME}_SRC
   ${SRC_PATH}/video.cpp
)
SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -pthread")

#Include opencv
find_package(OpenCV 4 REQUIRED)
include_directories(${OpenCV_INCLUDE_DIRS})

#Executable
add_executable( ${PROJECT_NAME} ${${PROJECT_NAME}_SRC} )
target_link_libraries( ${PROJECT_NAME} ${OpenCV_LIBS} )

