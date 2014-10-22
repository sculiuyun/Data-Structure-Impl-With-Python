#!/usr/bin/env python
# encoding: utf-8

class BaseQueue(object) :
    "BaseQueue"
    def enqueue(self,element) :
        """
        put an element into queue.
        """
        raise NotImplementedError()

    def dequeue(self) :
        """
        delete and return the head of the queue
        """
        raise NotImplementedError()

    def head(self) :
        """
        return the head of the queue.
        """
        raise NotImplementedError()

    def empty(self) :
        """
        if the queue is empty , return True, else return False.
        """
        raise NotImplementedError()

    def size(self) :
        """
        return the size of queue.
        """
        raise NotImplementedError()






