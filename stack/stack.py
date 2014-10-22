#!/usr/bin/env python
# encoding: utf-8

"""
用list模拟堆栈
"""

from stack_interface import BaseStack

class Stack(BaseStack) :

    def __init__(self) :
        """
        init a stack with []
        """
        self.stack = []
    def push(self,item) :
        """
        push an item into stack.
        """
        self.stack.append(item)
    def top(self) :
        """
        visite the top elements of stack.
        """
        index = len(self.stack)-1
        item = self.stack[index]
        return item
    def pop(self) :
        """
        pop the top elements of stack.
        """
        index = len(self.stack)-1
        item = self.stack[index]
        self.stack = self.stack[:index]
        return item
    def empty(self) :
        """
        if the stack is empty ,return True,else return False
        """
        length = len(self.stack)
        return length == 0
    def size(self) :
        """
        return the size of stack
        """
        return len(self.stack)

