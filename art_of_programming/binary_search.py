#!/usr/bin/env python
# encoding: utf-8

def binary_search(array,length,value) :
    left = 0
    right = length - 1
    while left <= right :
        middle = left + (right - left)/2
        if array[middle] > value :
            right = middle - 1
        elif (array[middle] < value) :
            left = middle +1
        else :
            return middle
    return -1
