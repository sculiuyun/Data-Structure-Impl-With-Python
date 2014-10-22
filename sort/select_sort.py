#!/usr/bin/env python
# encoding: utf-8

#简单选择排序的第i趟是从数组中选择第i小的元素,并将元素放在第i位上

def select_sort(data_array,n) :
    for i in range(n-1) :
        low_index = i    #记录data_array[i...n-1]中最小元素的下标
        for j in range(i+1,n) :
            if data_array[j] <data_array[low_index] :
                low_index = j
        swap(data_array,i,low_index)

def swap(data_array, low, high) :
    temp = data_array[low]
    data_array[low] = data_array[high]
    data_array[high] = temp

data=[10,9,8,7,6,5,4,3,2,1]
select_sort(data,10)
for i in range(10) :
    print data[i],
