#include <iostream>
#include <queue>
#include <stack>
#include <map>
using namespace std;

string i_addBinary_(string a, string b) {
    int len_a = a.size();
    int len_b = b.size();
    if (len_a > len_b) {
        for (int i =0; i< (len_a-len_b); ++i)
            b = '0'+b;
        len_b = len_a;
    }
    if (len_a < len_b) {
        for (int i =0; i< (len_b-len_a); ++i)
            a = '0'+a;
        len_a = len_b;
    }
    string res = "";
    int carry = 0;
    for (int i =(len_a-1); i >= 0; --i) {
        if (a[i] == '1' && b[i] == '1') {
            if (carry == 1)
                res = '1'+ res;
            else {
                res = '0' + res;
                carry = 1;
            }
        }
        else if (a[i] == '1' || b[i] == '1') {
            if (carry == 1) {
                res = '0' + res;
            } else {
                res = '1' + res;
                carry = 0;
            }
        }
        else {
            if (carry == 1)
                res = '1' + res;
            else
                res = '0' + res;
            carry = 0;
        }
    }

    if (carry ==1)
        res = '1' + res;
    return res;
}

string addBinary(string a, string b)
{
    string s = "";

    int c = 0, i = a.size() - 1, j = b.size() - 1;
    while(i >= 0 || j >= 0 || c == 1)
    {
        c += i >= 0 ? a[i --] - '0' : 0;
        c += j >= 0 ? b[j --] - '0' : 0;
        s = char(c % 2 + '0') + s;
        c /= 2;
    }

    return s;
}

string toNumber(const string& word, char*  map) {
    string s ="";
    for (char c : word) {
        char t = map[c - 'a'];
        if (s.find(t) == string::npos)
            s += t;
    }
    return s;
}
bool isInside(const string &str, int k, const string &subStr) {
    int i=0;
    while(i<subStr.size()) {
        if (str[k] != subStr[i]) {
            return false;
        }
        ++i;
        ++k;
        if (k > str.size())
            return false;
    }
    return true;
}
bool inString_(const string &str, string &subStr) {
    for (int i=0; i<str.size(); ++i) {
        if (!isInside(str, i, subStr)) {
            continue;
        } else {
            return true;
        }
    }
    return false;
}
bool inString(const string &str, string &subStr) {
    for (char c : subStr) {
        if (str.find(c) == string::npos)
            return false;
    }
    return true;
}
vector<string> getWords(const string& number, vector<string> *words, char *map) {
    vector<string> allwords;
    for (string& w : *words) {
        string wn = toNumber(w, map);
        if (inString(number, wn)) {
            allwords.push_back(w);
        }
    }
    return allwords;
}

int main() {
    char map[] = {'2','2','2','3','3','3','4','4','4','5','5','5','6','6','6','7','7','7','7','8','8','8','9','9','9','9'};
    string number = "3662277";
    vector<string> words = {"foo","bar","baz","foobar","emo","cap","car","cat"};
    vector<string> words_in_Number = getWords(number, &words, map);
    return 0;
}
