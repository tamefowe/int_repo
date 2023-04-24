cmake_minimum_required(VERSION 3.13)
project(EnrichedTrades)

set(CMAKE_CXX_STANDARD 14)

add_executable(EnrichedTrades main.cpp Cache.h DataProcessor.cpp DataProcessor.h Trade.h)