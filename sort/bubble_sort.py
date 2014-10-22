#!/usr/bin/env python
# encoding: utf-8

#冒泡排序的基本思想是:将序列中的第一个元素与第二个元素进行比较,如果前者大于后
#者,则两个元素交换位置,否则不交换,再将第二个元素和第三个元素比较,依次类推,
#直到第n-1个元素与第n个元素比较;

def bubble_sort(data_array, n) :
    for i in range(1,n) :
        for j in range(n-i) :
            if data_array[j] > data_array[j+1] :
                swap(data_array, j, j+1)

def swap(data_array, low, high) :
    temp = data_array[low]
    data_array[low] = data_array[high]
    data_array[high] = temp

data_array = [10,9,8,7,6,5,4,3,2,1]
length = len(data_array)
bubble_sort(data_array, length)
for i in range(length) :
    print data_array[i],
