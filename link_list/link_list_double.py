#!/usr/bin/env python
# encoding: utf-8

"""
双向链表
"""

from list_interface import BaseList

class DoubleLinkListNode(object) :
    "双向链表的节点类"
    def __init__(self,value) :
        self.key = value
        self.before = None
        self.after = None

class DoubleLinkList(BaseList) :
    "SimpleLinkList"
    def append(self,element) :
        """
        insert a node which key is element.
        """
        pass

    def front(self,element) :
        """
        将元素插入在链表开头
        """
        pass

    def insert(self,element,position=None) :
        """
        insert element in to the list at the position of position, 0 based
        position : 0--self.count
        """
        pass

    def remove(self,element) :
        """
        delete the node which key is element.(just delete the first one)
        """
        pass

    def getitem(self,position) :
        """
        find the element which index is position
        """
        pass

    def setitem(self,element,position) :
        """
        set the node(index is position) key to element .
        """
        pass

    def size(self) :
        """
        return the size of the list.
        """
        pass

    def display(self) :
        """
        display list.
        """
        pass

    def find(self,element) :
        """
        find the position of the element first appear,if not find in the list ,return -1
        """
        pass

    def empty(self) :
        """
        if list is empty ,return True,else return False.
        """

