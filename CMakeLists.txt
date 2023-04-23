cmake_minimum_required(VERSION 3.24)
project(Adaptive_Partition_Sort)

set(CMAKE_CXX_STANDARD 14)

include_directories(cpp/AdaptivePartitionSort_Cpp)

add_executable(Adaptive_Partition_Sort
        cpp/AdaptivePartitionSort_Cpp/APS.cpp
        cpp/AdaptivePartitionSort_Cpp/APS.h
        cpp/AdaptivePartitionSort_Cpp/Array.cpp
        cpp/AdaptivePartitionSort_Cpp/Array.h
        cpp/AdaptivePartitionSort_Cpp/IntroSort.cpp
        cpp/AdaptivePartitionSort_Cpp/IntroSort.h
        cpp/AdaptivePartitionSort_Cpp/Main.cpp
        cpp/AdaptivePartitionSort_Cpp/TimSort.cpp
        cpp/AdaptivePartitionSort_Cpp/TimSort.h)
