//
// Created by Trader on 4/12/2019.
//

#ifndef ENRICHEDTRADES_CACHE_H
#define ENRICHEDTRADES_CACHE_H

#include <unordered_map>

struct Cache
{
    long processed_trades;
    long total_volume;
    std::unordered_map<long, int> sizes;
    std::unordered_map<std::string, long> shares;
    std::unordered_map<std::string, double> notionals;
    std::unordered_map<std::string,
    std::unordered_map<std::string, long>> per_exchange_volumes;
    std::unordered_map<std::string,
    std::unordered_map<std::string, long>> symbols;

};
#endif //ENRICHEDTRADES_CACHE_H
