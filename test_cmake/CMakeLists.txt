
# TODO:
# - Reuse CMakeCache.txt to speed up finding compilers etc
# - Problem: CMake modules often find library files, instead of reporting a
#   prefix. E.g., FindLAPACK reports "Accelerate.framework;-lm;ldl".

# Can't use CMake script mode because many find modules need a compiler
project(FindPackage)
cmake_minimum_required(VERSION 3.12)

# Configure the find with CMake variables on the command line

find_package(${FIND_MODULE})

# Extract variables
# - Write to an output file, ideally to CMakeCache.txt, and read from Python

# Skip generation by emitting an error
message(SEND_ERROR "Done finding ${FIND_MODULE}. This is not an error.")
