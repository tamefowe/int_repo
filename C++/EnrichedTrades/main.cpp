#include <iostream>
#include "DataProcessor.h"

int main() {
    auto input_file{"/home/Trader/C++/iTest/input.dat"};
    auto output_file{"/home/Trader/C++/Trade/enrichedTrades.csv"};
    Processor processor(input_file, output_file);
    processor.processData();
    processor.getSummary();
    return 0;
}