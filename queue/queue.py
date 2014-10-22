#!/usr/bin/env python
# encoding: utf-8

from queue_interface import BaseQueue
"""
用list实现队列
"""
class Queue(BaseQueue) :

    def __init__(self) :
        """
        init a queue.
        """
        self.queue = []

    def enqueue(self,element) :
        """
        put element into queue.
        """
        self.queue.append(element)

    def dequeue(self) :
        """
        delete and return the head of the queue.
        """
        item = self.queue[0]
        self.queue = self.queue[1:]
        return item

    def head(self) :
        """
        return the head of queue.
        """
        return self.queue[0]

    def empty(self) :
        """
        if the queue is empty ,return True,else return False.
        """
        length = len(self.queue)
        return length == 0

    def size(self) :
        """
        return the size of queue.
        """
        return len(self.queue)

