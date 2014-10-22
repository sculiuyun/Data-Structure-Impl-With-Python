#!/usr/bin/env python
# encoding: utf-8

"""
堆排序
堆排序(heap sort)是一种基于选择排序的的先进排序方法,只需要一个元素的辅助存储空间.
1.堆
对于有n个元素的序列(elem[0],elem[1],....,elem[n]),当且仅当满足一下条件,称为堆:
    (1).elem[i]<=elem[2i+1] and elem[i]<=elem[2i+2]
    (2).elem[i]>=elem[2i+1] and elem[i]>=elem[2i+2]
    上面第一组关系定义的堆称为小顶堆,第二种关系定义的堆称为大顶堆.如果将序列
    看成完全二叉树,则堆的定义表明完全二叉树所有非终端节点值均不大于(或不小于)
    其左右孩子的值.
2.堆排序
对于大顶堆,堆顶元素最大,在输出堆顶元素之后,如果能使剩下的n-1个元素重新构建成一个
堆,则可以得到次大的元素如此继续可以得到一个有序的序列,这中排序方法称为堆排序
实现堆排序需要实现如下算法:
    1.将一个无序序列构建成一个堆.
    2.在输出堆顶元素之后,调整剩余元素成为一个新的堆.
3.输出堆顶元素后,调整剩余元素成为一个新堆的实现:
    设输出堆顶元素后,用堆中最后一个元素代替,这时,根节点的左右子树均为大顶堆,
    首先与堆顶元素的最大的左右孩子值进行交换,然后对子树进行堆调整,直至叶节点
    或遇到调整后仍是堆时.
4.从无序序列建立初始堆:
    从一个无序序列建立初始堆的过程实际上就是不断"筛选"的过程,如序列看成是
    一个完全二叉数,从最后一个非终端节点(下标:(n-2)/2)元素开始进行筛选.
    0-base下标,如果节点i存在孩子:
        2i+1 为左孩子数组下标
        2i+2 为右孩子数组下标
补充:
    若对于含n个节点的完全二叉树,按照从上到下,从左到右的次序进行1--n的编号,对于完全二叉树中的
    任一编号为n的节点,简称节点i,有以下关系:
    1.若i=1,则i是二叉树的根,无双亲节点;若i>1,则i/2为双亲节点.
    2.若2i>n,则节点i无左孩子,否则,节点2i为左孩子;
    3.若2i+1>n,则节点i无右孩子,否则节点2i+1为右孩子
"""
#以下以大顶堆为例
def heap_modify(data_array, low, high) :
    """
    调整成堆
    说明:data_array[low,...,high]中除了data_array[low]以外都满足堆的定义,
    调整data[low]使data_array[low,...,high]成为一个大顶堆
    """
    modify = low    #modify为被调整的节点下标
    index = low * 2 + 1    #左孩子节点,base-0
    while index <= high :    #存在孩子节点
        #index=high:表明存在左孩子,不存在右孩子;
        #index<high:表明存在左孩子和右孩子
        if index < high and data_array[index] < data_array[index+1] :
            #右孩子更大,index指向右孩子
            index += 1
        if data_array[modify] >= data_array[index] :
            #已经是大顶堆
            break
        #交换该节点与两个孩子节点中较大孩子的值
        swap(data_array,modify,index)
        modify = index

def swap(data_array,index1,index2) :
    temp = data_array[index1]
    data_array[index1] = data_array[index2]
    data_array[index2] = temp

def heap_sort(data_array,n) :
    """堆排序"""
    #最后一个非终端节点(下标:(n-2)/2)元素
    index = (n-2)/2
    while index >= 0 :
        #将data_array[0,...,n-1]调整成大顶堆
        heap_modify(data_array, index, n-1)
        index -= 1    #从右向左,从下到上,逐层调整
    for i in range(n-1,0,-1) :
        swap(data_array,0,i)
        #调整data_array[0,...,i-1]为大顶堆
        heap_modify(data_array,0,i-1)

data=[10,9,8,7,6,5,4,3,2,1]
heap_sort(data,10)
for i in range(10) :
    print data[i],
























