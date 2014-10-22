#!/usr/bin/env python
# encoding: utf-8

from queue_interface import BaseQueue

class QueueNode(object) :
    """
    Representation of a node in a queue.
    """
    def __init__(self,value) :
        """
        creat a new node with key value.
        """
        self.key = value
        self.disconnect()

    def disconnect(self) :
        self.after = None

class Queue(BaseQueue) :
    "链表实现队列"
    def __init__(self) :
        """
        init.
        """
        self.front = None
        self.rear = None
        self.count = 0

    def enqueue(self,element) :
        """
        put element into queue.
        """
        new_node = QueueNode(element)
        if self.front is None :
            self.front = new_node
            self.rear = new_node
        else :
            self.rear.after = new_node
            self.rear = new_node
        self.count += 1

    def dequeue(self) :
        """
        delete and return the head of the queue.
        """
        if(self.empty()) :
            print "the queue is empty"
            return
        else :
            node = self.front
            #head指向第二个元素
            self.front = self.front.after
            node.disconnect()
            self.count -= 1
            return node

    def head(self) :
        """
        return the head of the queue.
        """
        if self.empty() :
            print "the queue is empty"
            return
        else :
            node = self.front
            return node


    def empty(self) :
        """
        if the queue is empty ,return True,else return False.
        """
        return self.size() == 0

    def size(self) :
        """
        return the size of queue.
        """
        return self.count

