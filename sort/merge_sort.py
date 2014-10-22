#!/usr/bin/env python
# encoding: utf-8

#归并排序
#归并排序是一种简单易懂的高级排序方法.这里的归并是将两个有序的序列合并成一个
#新的有序序列,设初始序列中有n个元素,归并排序的基本思想是,将序列看成n个有序的
#子序列,每个序列的长度为一,然后两两归并,得到n/2个长度为2的或者1的有序子序列
#然后两两归并,......,这样重复下去,直到得到一长度为n的有序子序列,这种排序方法
#称为2-路归并.

def merge(data_array, low, mid, high) :
    temp = []    #临时序列
    i = low
    j = mid + 1
    while i <= mid and j <= high :
        if data_array[i] < data_array[j] :
            temp.append(data_array[i])
            i += 1
        else :
            temp.append(data_array[j])
            j += 1
    while i <= mid :
        temp.append(data_array[i])
        i += 1
    while j <= high :
        temp.append(data_array[j])
        j += 1
    #将排序后的复制回去
    for index in range(low,high+1) :
        data_array[index] = temp[index-low]

#归并排序
def merge_sort(data_array, low, high) :
    if low < high :
        mid = (low + high) / 2
        merge_sort(data_array, low, mid)
        merge_sort(data_array, mid+1, high)
        merge(data_array, low, mid, high)

data_array = [10,9,8,7,6,5,4,3,2,1]
length = len(data_array)
merge_sort(data_array, 0, length-1)
for i in range(length) :
        print data_array[i],















