#include <vector>
#include <cstdio>
#include <string>
#include <iostream>
#include <set>
#include <vector>
#include <sstream>
#include <map>

using namespace std;

void trim(char *w)
{
    int i = 0;
    while (i < 5)
    {
        if (w[i] >= 'A' && w[i] <= 'Z')
        {
            ++i;
        } else {
            break;
        }
    }
    w[i] = '\0';
}

#pragma pack(1)
struct update_header_t {
    uint16_t  length;
    char   type;
    update_header_t() : length(0), type(0){}
    bool isTrade() const
    {
        return type == 'T';
    }
    void convert()
    {
        length = __bswap_16(length);
    }
};

struct update_t {
    char  symbol[5];
    uint16_t trade_size;
    uint64_t trade_price;
    update_t() : symbol(""), trade_size(0), trade_price(0){}
    void convert()
    {
        trade_size = __bswap16(trade_size);
        trade_price = __bswap64(trade_price);
    }
};

struct packet_header_t {
    uint16_t length;
    uint16_t num_market_updates;
    packet_header_t() :length(0), num_market_updates(0){}
    void convert()
    {
        length = __bswap16(length);
        num_market_updates = __bswap16(num_market_updates);
    }
};

struct packet_t {
    packet_header_t header;
    std::vector<update_t> updates;
    void logTrades(FILE *oFile)
    {
        for (auto update : updates)
        {
            if (update.symbol[4] >= 'A' && update.symbol[4] <= 'Z')
            {
                char symbol[6];
                sprintf(symbol, "%s", update.symbol);
                symbol[5] = '\0';
                fprintf(oFile, "%d %s @ %.2f\n", update.trade_size*100, symbol, (double)(update.trade_price)/10000.0);
            } else {
                trim(update.symbol);
                fprintf(oFile, "%d %s @ %.2f\n", update.trade_size*100, update.symbol, (double)(update.trade_price)/10000.0);
            }
        }
    }
};

void getTradeFromFile(char *inFileName, char *oFileName)
{
    FILE *pFile, *oFile;
    pFile = fopen(inFileName, "rb");
    oFile = fopen(oFileName, "w");

    if ( pFile == nullptr)
    {
        perror ("error opening file");
    } else {
        while (!feof(pFile))
        {
            packet_t packet;
            size_t s = sizeof(struct packet_header_t);
            fread(&packet.header, s, 1, pFile);
            packet.header.convert();
            for (int i = 0; i < packet.header.num_market_updates; ++i)
            {
                update_header_t u_header;
                fread(&u_header, sizeof(struct update_header_t), 1, pFile);
                u_header.convert();
                if (u_header.isTrade())
                {
                    update_t update;
                    fread(&update, sizeof(struct update_t), 1, pFile);
                    update.convert();
                    packet.updates.push_back(update);
                    fseek(pFile, u_header.length-18, SEEK_CUR);
                } else {
                    fseek(pFile, u_header.length-3, SEEK_CUR);
                }
            }
            packet.logTrades(oFile);
        }
        fclose(oFile);
        fclose(pFile);
    }
}
std::string  hackerrankInString(std::string s) {

    std::string searchWord{"hackerrank"};
    auto i{0};
    auto j{0};

    while (i < searchWord.size()) {
        while (j < s.size()) {
            if (s[j] == searchWord[i]) {
                std::cout << "i: " << i << " -- " << searchWord[i] << " |  j: " << j << " -- " << s[j] << "\n";
                if (i == (searchWord.size()-1))
                    return "YES";
                ++i;
                ++j;
                break;
            }
            ++j;
        }
    }
    return "NO";
}

string  wir(vector<string> ballot) {

    set<pair<int, string>> i;
    map<string, int> elts;
    for (auto e : ballot)
        elts[e]++;

    for (auto e : elts)
        i.insert(pair<int, string>(e.second, e.first));

    for (auto e : i)
        cout << e.first << " " << e.second << "\n";
    set<pair<int, string>>::reverse_iterator r{i.rbegin()};
    return r->second;
}

vector<string> weightedUniformStrings(string s, vector<int> queries) {
    set<int> into;
    map<char, int> apbt = {
            {'a', 1}, {'b', 2}, {'c', 3}, {'d', 4}, {'e', 5}, {'f', 6}, {'g', 7},
            {'h', 8}, {'i', 9}, {'j', 10}, {'k', 11}, {'l', 12}, {'m', 13}, {'n', 14},
            {'o', 15}, {'p', 16}, {'q', 17}, {'r', 18}, {'s', 19}, {'t', 20}, {'u', 21},
            {'v', 22}, {'w', 23}, {'x', 24}, {'y', 25}, {'z', 26}
    };

    char prev{0};
    auto count {1};

    for (auto c : s) {
        if (prev == c) {
            ++count;
            into.insert(apbt[c]*count);
        }
        else {
            count = 1;
            into.insert(apbt[c]);
        }
        prev = c;
    }

    auto i{0};
    vector<string> results(queries.size());
    for (auto q : queries)
        results[i++] = into.find(q) != into.end() ? "Yes" : "No";

    return results;
}

int main()
{
    /*/std::string s{"hereiamstackerrank"};

    //vector<string> v = {"ale", "mich", "harr", "dave", "mich", "vict", "harr", "ale", "mar", "mar"};
    string s{"abccddde"};
    vector<int> queries = {1,3,12,5,9,10};
    vector<string> v =  weightedUniformStrings(s, queries);
    for (auto e : v)
        cout << e;
    //std::cout << hackerrankInString(s) << "\n";

    */
    char ifilename[] = "/home/Trader/C++/iTest/input.dat";
    char ofilename[] = "/home/Trader/C++/iTest/output.txt";
    getTradeFromFile(ifilename, ofilename);

    return 0;
}