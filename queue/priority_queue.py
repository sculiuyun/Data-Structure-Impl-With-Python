#!/usr/bin/env python
# encoding: utf-8

#优先队列(priority queue):是一种数据结构,其中元素的固有顺序决定了对基本操作的
#执行结果,优先队列有两种类型:最小优先队列和最大优先队列.
#优先队列:即在普通队列的 ADT 上加了一重逻辑，让符合某种条件的元素优先出队。
#一般以数值大小为条件，所以也分为最大化优先队列和最小化优先队列。

#堆是一种特殊的数据结构.它是一棵二叉树,元素必须从左至右填入最后一层,然后再创
#建新一层.因此堆满足很多有趣的性质:
#(1).若堆的元素个数为N,则高度不超过[log N]+1.
#(2).堆可以用数组表示.在这种情况下,节点N的父节点在N/2处,左字节点在N*2处,
#右子节点在N*2+1处.

#可以使用大顶堆实现最大优先队列,用小顶堆实现最小优先队列

#为了保证传入对象同样可以使用,可以进行比较,可以考虑传入函数作为参数

class MaxPriorityHeapQueue(object) :
    "用大顶堆实现最大优先队列"
    def __init__(self,queue) :
        self.queue = queue        #存储数据的数组
        self.size = len(queue)    #队列的长度
        self.build_heap()

    def build_heap(self) :
        """
        该函数主要用来开始阶段将用户输入的数组初始化成堆
        用数组表示的n个元素的堆中,最后一个非终端节点的下标是(n-2)/2
        """
        #建堆
        index = (self.size-2)/2
        while index >= 0 :
            #将self.queue[0,...,n-1]调整成大顶堆
            #从右向左,从下到上,逐层调整
            self.modify_heap(index, n-1)
            index -= 1

    def modify_heap(self, low, high) :
        """
        删除或者添加元素后,重新调整成堆
        操作结果:self.queue[low,...,high]中的记录除了elem[low]之外都满足堆定义.
        调整self.queue[low],使得self.queue[low,...,high]成为一个大顶堆
        """
        modify = low    #modify为被调整节点的下标
        index = low * 2 +1    #self.queue[low]节点的左孩子节点
        while index <= high :
            #index=high:表明存在左孩子,不存在右孩子
            #index<high:表明存在左孩子和右孩子
            if index < high and self.queue[index] < self.queue[index+1] :
                #存在右孩子,并且左孩子小于右孩子
                index += 1
            if self.queue[modify] >= self.queue[index] :
                #已经是大顶堆
                break
            self.swap(modify,index)
            #调整节点下标,指向下一个要被调整的节点
            modify = index

    def swap(self,low, high) :
        temp = self.queue[low]
        self.queue[low] = self.queue[high]
        self.queue[high] = temp


    def size(self) :
        """求优先队列的长度"""
        return self.size

    def empty(self) :
        """判断优先队列是否为空"""
        return self.size == 0

    def enqueue(self, elem) :
        """
        元素入队
        首先,将要入队的元素elem置于堆的末尾位置self.size.
        然后,将其与双亲节点进行比较,使其移动到正确的位置上
        """
        self.queue.append(elem)
        self.size += 1
        index = self.size - 1
        parent = (self.size - 2)/2    #找到新插入节点的父节点的下标
        while parent >= 0 :
            if elem <= self.queue[parent] :
                break
            else :
                self.swap(index,parent)    #交换,数值大的往树的上层移动
                index = parent
                parent = (parent - 1)/2    #此处用的是数组下标,所以-1


    def dequeue(self) :
        """
        元素出队,返回队首元素
        首先将要最后一个元素和堆顶元素互换,然后删除最后一个元素.
        最后,重新调整使self.queue成为一个新的大顶堆
        """
        swap(0,self.size-1)
        ret = self.queue.pop()
        self.modify_heap(0,size-1)

    def get_head(self) :
        """获取队首元素"""
        return self.queue[0]

    def display(self) :
        for index in range(self.size) :
            print self.queue[index],
        print

if __name__ == "__main__" :
    test = MaxPriorityHeapQueue([])
    test.enqueue(1)
    test.display()
    test.enqueue(3)
    test.display()
    test.enqueue(5)
    test.display()
    test.enqueue(2)
    test.display()
    test.enqueue(10)
    test.display()














