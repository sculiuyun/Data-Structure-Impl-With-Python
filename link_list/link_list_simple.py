#!/usr/bin/env python
# encoding: utf-8

"""
单向链表实现
"""

from list_interface import BaseList

class SimpleLinkListNode(object) :
    "单向链表的节点类"
    def __init__(self,value) :
        self.key = value
        self.after = None

class SimpleLinkList(BaseList) :
    "SimpleLinkList"
    def __init__(self) :
        """ init """
        self.root = None
        self.count = 0

    def append(self,element) :
        """
        insert a node which key is element.
        """
        new_node = SimpleLinkListNode(element)
        if self.root is None :
            self.root = new_node
        else :
            temp = self.root
            while temp.after is not None :
                temp = temp.after
            temp.after = new_node
        self.count += 1

    def front(self,element) :
        """
        将元素插入在链表开头
        """
        new_node = SimpleLinkListNode(element)
        if self.root is None :
            self.root = new_node
        else :
            temp =self.root
            self.root = new_node
            new_node.after = temp
        self.count += 1

    def insert(self,element,position=None) :
        """
        insert element in to the list at the position of position, 0 based
        position : 0--self.count
        """
        if position is not None :
            if not isinstance(position, int) :        #验证参数类型
                raise TypeError('invalid index type,it should be type of int')
            else :
                if position < 0 or position > self.count:        #验证参数范围(0-->self.count)
                    raise IndexError('index should not less than 0')
                elif position == 0 :
                    self.front(element)
                else :
                    new_node = SimpleLinkListNode(element)
                    if self.root is None :
                        self.root = new_node
                    else :
                        temp = self.root
                        for index in xrange(position-1) :
                            temp = temp.after
                            print "nimei"
                        temp_after = temp.after       #原来position位置的节点
                        temp.after = new_node         #position-1位置节点的after指向新节点
                        new_node.after = temp_after   #新节点的after指向原position位置的节点
                    self.count += 1
        else :        #若没有提供位置参数,则将其插入到末尾
            self.append(element)


    def remove(self,element) :
        """
        delete the node which key is element.(just delete the first one)
        """
        temp = self.root
        if temp is None :
            return
        if temp.key == element :    #第一个元素是要删除的元素
            temp_after = temp.after
            temp.after =None
            self.root = temp_after
            self.count -= 1
        else :
            while temp.after is not None :
                if temp.after.key == element :
                    temp_after = temp.after           #temp_after就是要删除的节点
                    temp.after = temp.after.after
                    temp_after = None
                    self.count -= 1
                else :
                    temp = temp.after


    def getitem(self,position) :
        """
        find the element which index is position
        """
        if not isinstance(position, int) :
            raise TypeError('invalid index type')
        if position < 0 or position >= self.count :
            raise IndexError('index out of range')
        temp = self.root
        for index in xrange(position) :
            temp = temp.after
        return temp.key

    def setitem(self,element,position) :
        """
        set the node(index is position) key to element .
        """
        if not isinstance(position, int) :
            raise TypeError('invalid index type')
        if position < 0 or position >= self.count :
            raise TypeError('index out of range')
        temp = self.root
        for index in xrange(position) :
            temp = temp.after
        temp.key = element

    def size(self) :
        """
        return the size of the list.
        """
        return self.count

    def display(self) :
        """
        display list.
        """
        node = self.root
        while node is not None :
            print " ", node.key ,
            node = node.after

    def find(self,element) :
        """
        find the position of the element first appear,if not find in the list ,return -1
        """
        temp = self.root
        position = 0
        while temp is not None :
            if element == temp.key :
                break
            temp = temp.after
            position += 1
        else :         #这个else用于匹配while
            position = -1
        return position


    def empty(self) :
        """
        if list is empty ,return True,else return False.
        """
        return self.size() == 0


