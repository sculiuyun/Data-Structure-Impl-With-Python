#!/usr/bin/env python
# encoding: utf-8

from stack_interface import BaseStack

class StackNode(object) :
    """
    Representation of a node in a stack.
    """
    def __init__(self,value) :
        """
        creat a new node with key value.
        """
        self.key = value
        self.disconnect()

    def disconnect(self) :
        self.after = None

class Stack(BaseStack) :
    """
    linked stack
    """
    def __init__(self) :
        """
        init.
        """
        self.bottom = None
        self._top = None
        self.count = 0

    def push(self,element) :
        """
        push element to the top of stack.
        """
        new_node = StackNode(element)
        if self._top is None :
            self.bottom = new_node
            self._top = new_node
        else :
            new_node.after = self._top
            self._top = new_node
        self.count += 1

    def pop(self) :
        """
        pop the item on the top of the stack.
        """
        if self.empty() :
            print "the stack is empty"
            return
        else :
            node = self._top
            self._top = self._top.after
            node.disconnect()
            self.count -= 1
            return node.key

    def top(self) :
        """
        visite the top elements of stack.
        """
        return self._top.key

    def empty(self) :
        """
        if the Stack is empty ,return True,else return False
        """
        return self.size() == 0

    def size(self) :
        """
        return the size of stack.
        """
        return self.count

