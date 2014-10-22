#!/usr/bin/env python
# encoding: utf-8

#快速排序
#快速排序的基本思想是任选序列中的一个数据元素作为枢轴,用它和剩余的元素进行比
#较,将所有比它小的元素都排在它的前面,将所有比它大的元素都排在它的后面,经过一
#趟排序后,可按此元素所在位置为界,将序列划分成两个部分,在对这两个部分重复上述
#过程直到每一部分都只剩一个元素为止.

def partition(data_array, low, high) :
    """
    将枢轴移动到适当的位置,要求在枢轴之前的元素不大于枢轴,
    枢轴之后的元素不小于枢轴.
    """
    while low < high :
        while low < high and data_array[high] >= data_array[low] :
            #data_array[low]为枢轴,使high右边的元素不小于data_array[low]
            high -= 1
        swap(data_array, low, high)
        while low < high and data_array[low] <= data_array[high] :
            #data_array[high]为枢轴,使low左边的元素不大于data_array[high]
            low += 1
        swap(data_array, low, high)
    #返回枢轴的位置
    return low

def swap(data_array, low, high) :
    temp = data_array[low]
    data_array[low] = data_array[high]
    data_array[high] = temp

def quick_sort(data_array, low, high) :
    if low < high :
        pivot = partition(data_array, low, high)
        quick_sort(data_array, low, pivot-1)
        quick_sort(data_array, pivot+1, high)

data_array = [10,9,8,7,6,5,4,3,2,1]
length = len(data_array)
quick_sort(data_array, 0, length-1)
for i in range(length) :
    print data_array[i],






