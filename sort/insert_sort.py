#!/usr/bin/env python
# encoding: utf-8

#直接插入排序是一种简单的排序算法,其基本思想就是将第一个元素看成有序的子序列
#再依次将第二个记录起逐个插入到这个有序序列之中.

def insert_sort(data_array,n) :
    for i in range(1,n) :
        #将第i趟直接插入排序
        elem = data_array[i]
        j = i-1
        while j >= 0 and elem < data_array[j] :
            data_array[j+1] = data_array[j]
            j -= 1
        data_array[j+1] = elem
#        print "第%d趟排序结果" % i,
#        for i in range(10) :
#            print data[i],
#        print


data=[10,9,8,7,6,5,4,3,2,1]
insert_sort(data,10)
for i in range(10) :
    print data[i],
