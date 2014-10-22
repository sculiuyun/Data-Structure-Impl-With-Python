#!/usr/bin/env python
# encoding: utf-8

class BaseList(object) :

    def append(self,element) :
        """
        insert a node which key is element.
        """
        raise NotImplementedError()

    def insert(self,element,position=None) :
        """
        insert element in to the list at the position of position, 0 based
        position : 0--self.count
        """
        raise NotImplementedError()

    def remove(self,element) :
        """
        delete the node which key is element.(just delete the first one)
        """
        raise NotImplementedError()

    def getitem(self,position) :
        """
        find the element which index is position
        """
        raise NotImplementedError()

    def setitem(self,element,position) :
        """
        set the node(index is position) key to element .
        """
        raise NotImplementedError()

    def size(self) :
        """
        return the size of the list.
        """
        raise NotImplementedError()

    def display(self) :
        """
        display list.
        """
        raise NotImplementedError()

    def find(self,element) :
        """
        find the position of the element first appear,if not find in the lis
        """
        raise NotImplementedError()

    def empty(self) :
        """
        if list is empty ,return True,else return False.
        """
        raise NotImplementedError()

