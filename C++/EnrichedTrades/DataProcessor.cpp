//
// Created by Trader on 4/12/2019.
//

#include "DataProcessor.h"
#include <iostream>
#include <fstream>
#include <algorithm>
#include <cstdio>
#include <map>
#include <iomanip>
#include <sstream>
#include <numeric>
#include <cstdlib>
#include <climits>
#include <locale>

using namespace std;

Processor::Processor(string input_file, string output_file)
        : _input_file(move(input_file)), _output_file(move(output_file))
{
    _cache = make_shared<Cache>();
    _cache->processed_trades = 0;
    _cache->total_volume = 0;
    _cache->shares = {{"Bought", 0}, {"Sold", 0}};
    _cache->notionals = {{"Bought", 0.00}, {"Sold", 0.00}};
}


double find_median(const unordered_map<long, int> &sizes)
{
    vector<long> all_trades;

    for (auto  x : sizes)
        for (auto i = 0; i < x.second; ++i)
            all_trades.push_back(x.first);

    sort(begin(all_trades), end(all_trades));

    auto n = all_trades.size();

    if (n % 2 != 0)
        return static_cast<double>(all_trades[n/2]);

    return static_cast<double>(all_trades[(n-1)/2] + all_trades[n/2])/2.0;
}

void Processor::getSummary() const
{
    string per_exchange_volume_str;
    map<string, unordered_map<string, long>> out(begin(_cache->per_exchange_volumes), end(_cache->per_exchange_volumes));
    for (auto const &e : out) {
        map<string, long> in(begin(e.second), end(e.second));
        for (auto const &f : in) {
            char buff[20];
            setlocale(LC_NUMERIC, "");
            sprintf(buff, "%s %s: %ld\n", e.first.c_str(), f.first.c_str(), f.second);
            per_exchange_volume_str += string(buff);
        }
    }

    int median_trade_size = static_cast<int>(find_median(_cache->sizes));

    map<string, long> symbol_sizes;
    for (auto const &e : _cache->symbols) {
        symbol_sizes[e.first] = 0;
        for (auto const &f : e.second)
            symbol_sizes[e.first] += f.second;
    }

    vector<pair<string, long>> pairs;
    for (auto const &e : symbol_sizes)
        pairs.emplace_back(e);
    sort(end(pairs), end(pairs),
            [=](pair<string, long>& a, pair<string, long>& b) ->bool {return a.second > b.second;});

    string most_active_symbol_str;
    int count = 10;
    for (auto const &e : pairs) {
        if (count) {
            char buff[10];
            setlocale(LC_NUMERIC, "");
            sprintf(buff, "%s(%ld), ", e.first.c_str(), e.second);
            most_active_symbol_str += string(buff);
            --count;
        } else {
            break;
        }
    }
    most_active_symbol_str.pop_back();
    most_active_symbol_str.pop_back();

    auto average_size = static_cast<int>(static_cast<float>(_cache->total_volume)/static_cast<float>(_cache->processed_trades));
    cout.imbue(locale(""));
    cout << "\n\nTrade Summary" << "\n----------------------\n\n"
         << "Processed Trades: " << _cache->processed_trades << "\n\n"
         << "Shares Bought: " << _cache->shares["Bought"] << "\n"
         << "Shares Sold: " << _cache->shares["Sold"] << "\n"
         << "Total Volume: " << _cache->total_volume << "\n"
         << "Notional Bought: $" << setprecision(10) <<_cache->notionals["Bought"] << "\n"
         << "Notional Sold: $" << setprecision(10) << _cache->notionals["Sold"] << "\n\n"
         << "Per Exchange Volumes: \n" << per_exchange_volume_str << "\n"
         << "Average Trade Size: " << average_size << "\n"
         << "Median Trade Size: " << median_trade_size << "\n\n"
         << "10 Most Active Symbols: " << most_active_symbol_str << "\n";

}

Trade Processor::_parse(const string &trade_str)
{
    string elt;
    stringstream line_stream(trade_str);
    Trade trade = {0, -1, -1.0, "", "", "", ""};
    auto i{0};
    char* ptr;

    try
    {
        while (getline(line_stream, elt, ','))
        {
            if (i == 0)
                trade.local_time = elt;
            if (i == 1)
                trade.symbol = elt;
            if (i == 2)
                trade.event_type = elt;
            if (i == 3)
                trade.side = elt[0];
            if (i == 4) {
                trade.fill_size = strtol(elt.c_str(), &ptr, 0);
                if (ptr == elt.c_str() || *ptr != '\0' || trade.fill_size == INT_MIN || trade.fill_size == INT_MAX)
                    throw InvalidDataException("invalid trade fill size!");
            }
            if (i == 5) {
                trade.fill_price = strtod(elt.c_str(), &ptr);
                if (ptr == elt.c_str() || *ptr != '\0' ||
                    trade.fill_price == numeric_limits<double>::max() ||
                    trade.fill_size == numeric_limits<double>::min())
                    throw InvalidDataException("invalid trade fill price!");
            }
            if (i == 6)
                trade.fill_exchange = elt;
            ++i;
        }
        return trade;
    }
    catch(InvalidDataException& i)
    {
        cerr << i.what() << "\n";
    }
}

bool Processor::_isTradeValid(const Trade &trade)
{
    if (trade.event_type != "TRADE") {
        cerr << "Invalid trade event type: " << trade.event_type << "!\n";
        return false;
    }

    if (trade.local_time.empty()    ||
        trade.fill_exchange.empty() ||
        trade.fill_price    == 0.00 ||
        trade.fill_size     == 0    ||
        trade.side          == 0    ||
        trade.event_type.empty()    ||
        trade.symbol.empty()) {
        cerr << "Missing trade data!\n";
        return false;
    }

    string str{"sbt"};
    if (str.find(trade.side) == string::npos) {
        cerr << "Invalid trade side: " << trade.side << "\n";
        return false;
    }

    return true;
}

string Processor::_enrichTrade(const Trade &trade)
{
    ++_cache->processed_trades;
    _cache->total_volume += trade.fill_size;

    auto side = (trade.side == 'b') ? "Bought" : "Sold";
    auto other_side = (trade.side != 'b') ? "Bought" : "Sold";

    _cache->shares[side]   += trade.fill_size;
    _cache->notionals[side] += (trade.fill_size * trade.fill_price);

    if (_cache->sizes.find(trade.fill_size) == _cache->sizes.end())
        _cache->sizes[trade.fill_size] = 1;
    else
        _cache->sizes[trade.fill_size] += 1;

    if (_cache->per_exchange_volumes.find(trade.fill_exchange) == _cache->per_exchange_volumes.end()) {
        _cache->per_exchange_volumes[trade.fill_exchange][side] = trade.fill_size;
        _cache->per_exchange_volumes[trade.fill_exchange][other_side] = 0;
    } else {
        _cache->per_exchange_volumes[trade.fill_exchange][side] += trade.fill_size;
    }

    if (_cache->symbols.find(trade.symbol) == _cache->symbols.end()) {
        _cache->symbols[trade.symbol][side] = trade.fill_size;
        _cache->symbols[trade.symbol][other_side] = 0;
    } else {
        _cache->symbols[trade.symbol][side] += trade.fill_size;
    }

    char buffer[100];
    sprintf(buffer,
            "%s,%s,%s,%c,%d,%.2f,%s,%ld,%ld,%ld,%.2f,%ld,%ld,%ld,%ld,%.2f,%.2f\n",
            trade.local_time.c_str(),
            trade.symbol.c_str(),
            trade.event_type.c_str(),
            trade.side,
            trade.fill_size,
            trade.fill_price,
            trade.fill_exchange.c_str(),
            _cache->symbols[trade.symbol]["Bought"],
            _cache->symbols[trade.symbol]["Sold"],
            (_cache->symbols[trade.symbol]["Bought"] - _cache->symbols[trade.symbol]["Sold"]),
            trade.fill_size * trade.fill_price,
            _cache->per_exchange_volumes[trade.fill_exchange]["Bought"],
            _cache->per_exchange_volumes[trade.fill_exchange]["Sold"],
            _cache->shares["Bought"],
            _cache->shares["Sold"],
            _cache->notionals["Bought"],
            _cache->notionals["Sold"]
    );

    return string(buffer);
}

void Processor::processData()
{
    string line;
    Trade trade;
    ifstream  _input_handler(_input_file, fstream::binary | fstream::out);
    //ofstream  _output_handler(_output_file);

    if (_input_handler.is_open())
    {
        getline(_input_handler, line);
        vector<string> add_headers = get_headers();
        auto headers = accumulate(begin(add_headers), end(add_headers), string(","));
        //_output_handler <<  line + "," + headers  + "\n";

        while(getline(_input_handler, line))
        {

            cout << line << "\n";
            //trade = _parse(line);
            //if (_isTradeValid(trade))
             //   _output_handler << _enrichTrade(trade);
        }
        _input_handler.close();
        //_output_handler.close();
    }
    else
    {
        cerr << "Cannot open file: " << _input_file << "\n";
    }
}

vector<string> get_headers()
{
    return  {"SymbolBought", "SymbolSold", "SymbolPosition", "SymbolNotional",
                "ExchangeBought", "ExchangeSold", "TotalBought", "TotalSold",
                "TotalBoughtNotional", "TotalSoldNotional"};
}