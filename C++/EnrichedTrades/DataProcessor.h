//
// Created by Trader on 4/12/2019.
//

#ifndef ENRICHEDTRADES_DATAPROCESSOR_H
#define ENRICHEDTRADES_DATAPROCESSOR_H

#include "Cache.h"
#include "Trade.h"
#include <vector>
#include <memory>
#include <exception>

using namespace std;

vector<string> get_headers();

double find_median(const unordered_map<long, int>&);

class InvalidDataException: public exception
{
    runtime_error _err;
public:
    explicit InvalidDataException(const char *m) : _err(m) {}
    const char *what() const noexcept(true) override {return _err.what();};
};

class Processor
{
private:
    string _input_file;
    string _output_file;
    shared_ptr<Cache> _cache;

    static Trade _parse(string const &);
    static bool _isTradeValid(const Trade&);
    string _enrichTrade(const Trade&);

public:
    Processor(string, string);
    ~Processor() = default;
    Processor(const Processor&) = delete;
    Processor& operator=(const Processor&) = delete;

    void getSummary() const;
    void processData();
};
#endif //ENRICHEDTRADES_DATAPROCESSOR_H
