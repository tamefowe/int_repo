//
// Created by Trader on 2/20/2021.
//
#include <iostream>

void swap_(int* arr, int i, int j) {
    int t = arr[i];
    arr[i] = arr[j];
    arr[j] = t ;
}

void move_all_zeros_(int * arr, int length) {
    int j = length-1;
    int i = 0;
    while (arr[j] == 0) {
        --j;
    }
    while (i < j) {
        if (arr[i] == 0) {
            swap_(arr, i, j);
            --j;
        }
        ++i;
    }
}

void swap(int * a, int * b ) {
    int t = *a;
    *a = *b;
    *b = t;
}


void move_all_zeros(int * arr, int length) {
    int* s = arr;
    int *e = arr+length-1;
    while (*e == 0) {
        --e;
    }
    while (s < e) {
        if (*s == 0) {
            swap(s,e);
            --e;
        }
        ++s;
    }
}

int fmain_() {
    int arr[] = {1, 0, 0, 2, 5, 0};
    int length = sizeof(arr)/sizeof(arr[0]);
    //move_all_zeros_(arr, length);
    move_all_zeros(arr, length);
    return 0;
}