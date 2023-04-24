//
// Created by Trader on 4/12/2019.
//

#ifndef ENRICHEDTRADES_TRADE_H
#define ENRICHEDTRADES_TRADE_H

struct Trade
{
    char side;
    int fill_size;
    double fill_price;
    std::string local_time;
    std::string symbol;
    std::string event_type;
    std::string fill_exchange;
};

#endif //ENRICHEDTRADES_TRADE_H
