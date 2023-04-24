//
// Created by Trader on 2/20/2021.
//
#ifndef STRING_CPP
#define STRING_CPP


#include <iostream>
#include <map>
#include <stack>
using namespace std;

bool isValid(string s) {
    map<char,char> m = {{')','('}, {'}','{'}, {']','['}};
    stack<char> stk;
    char top;

    for (int i =0; i < s.size(); ++i) {
        if (m.find(s[i]) != m.end()) {
            if (not stk.empty()) {
                top = stk.top();
                stk.pop();
            } else {
                top = '#';
            }
            if (top != m[s[i]])
                return false;
        } else {
            stk.push(s[i]);
        }
    }
    return  stk.empty();
}

int longestValidParentheses(string s) {
    int l = s.size();
    if (l == 0)
        return 0;
    int maxLength = 0;
    int left = 0;
    int right = 0;
    for (int i=0; i<l; ++i) {
        if (s[i] == '(')
            ++left;
        else
            ++right;
        if (right > left)
            left = right = 0;
        if (left == right)
            maxLength = max(maxLength,right+left);
    }
    left = right = 0;
    for (int i=(l-1); i>=0; --i) {
        if (s[i] == ')')
            ++right;
        else
            ++left;
        if (left > right)
            left = right = 0;
        if (left == right)
            maxLength = max(maxLength,right+left);
    }
    return maxLength;
}

string addBinary_(string a, string b) {
    int len_a = a.size();
    int len_b = b.size();

    if (len_a > len_b) {
        for (int i =0; i< (len_a-len_b); ++i)
            b = '0'+b;
    }
    if (len_a < len_b) {
        for (int i =0; i< (len_b-len_a); ++i)
            a = '0'+a;
    }
    string res = "";
    int carry = 0;
    for (int i =(len_a); i >= 0; --i) {
        if (a[i] == '1' && b[i] == '1') {
            if (carry == 1)
                res = '1'+ res;
            else {
                res = '0' + res;
                carry = 1;
            }
        }
        if (a[i] == '1' || b[i] == '1') {
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
int fiain_() {
    //string s = "(([(({[}))]))";
    //string s = "()";
    //string s = "()[]{}";
    //string s = "(]";
    //string s = "([)]";
    //string s = "{[]}";
    //cout << (isValid(s) ? "YES" : "NO") << endl;

    string a = "101001101";
    string b = "1010110";
    string st = addBinary_(a, b);
    return 0;
}

#endif