#!/usr/bin/env python
# encoding: utf-8

class BaseStack(object) :
    "BaseStack"
    def push(self,item) :
        """
        push an item into stack
        """
        raise NotImplementedError()

    def pop(self) :
        """
        pop the item at the top of stack.
        """
        raise NotImplementedError()

    def top(self) :
        """
        visite the top elements of stack.
        """
        raise NotImplementedError()

    def empty(self) :
        """
        if the Stack is empty ,return True,else return False
        """
        raise NotImplementedError()

    def size(self) :
        """
        return the size of stack
        """
        raise NotImplementedError()

