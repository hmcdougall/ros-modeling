# Install script for directory: /home/robot0/catkin_ws/src/ackermann_vehicle/ackermann_vehicle_gazebo

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/robot0/catkin_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/robot0/catkin_ws/build/ackermann_vehicle/ackermann_vehicle_gazebo/catkin_generated/installspace/ackermann_vehicle_gazebo.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ackermann_vehicle_gazebo/cmake" TYPE FILE FILES
    "/home/robot0/catkin_ws/build/ackermann_vehicle/ackermann_vehicle_gazebo/catkin_generated/installspace/ackermann_vehicle_gazeboConfig.cmake"
    "/home/robot0/catkin_ws/build/ackermann_vehicle/ackermann_vehicle_gazebo/catkin_generated/installspace/ackermann_vehicle_gazeboConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ackermann_vehicle_gazebo" TYPE FILE FILES "/home/robot0/catkin_ws/src/ackermann_vehicle/ackermann_vehicle_gazebo/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/ackermann_vehicle_gazebo" TYPE PROGRAM FILES "/home/robot0/catkin_ws/build/ackermann_vehicle/ackermann_vehicle_gazebo/catkin_generated/installspace/ackermann_controller")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ackermann_vehicle_gazebo" TYPE DIRECTORY FILES
    "/home/robot0/catkin_ws/src/ackermann_vehicle/ackermann_vehicle_gazebo/config"
    "/home/robot0/catkin_ws/src/ackermann_vehicle/ackermann_vehicle_gazebo/launch"
    )
endif()

