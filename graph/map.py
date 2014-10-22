#!/usr/bin/env python
# encoding: utf-8

import string
#实现hashtable,主要使用散列表,HashTable

class LinearMap(object) :
    "使用元组列表实现hashtable"
    def __init__(self) :
        self.items = []

    def add(self,key,value) :
        """添加一个新的键值对"""
        self.items.append((key,value))

    def get(self,key) :
        """根据key获取值"""
        for k,v in self.items :
            if k == key :
                return v
        raise KeyError

class BetterMap(object) :
    "将键值对列表打乱成更小的列表"
    def __init__(self,n=100) :
        self.maps = []
        for i in range(n) :
            self.maps.append(LinearMap())

    def find_map(self,key) :
        """找到对应散列值的(key,value)list"""
        index = hash(key) % len(self.maps)
        return self.maps[index]

    def add(self,key,value) :
        """向hash表中添加(key,value)对"""
        m = self.find_map(key)
        m.add(key,value)

    def get(self,key) :
        """根据key找对应的value"""
        m = self.find_map(key)
        return m.get(key)

class HashMap(object) :
    "HashTable"
    def __init__(self) :
        self.maps = BetterMap(2)
        self.num = 0

    def get(self,key) :
        return self.maps.get(key)

    def add(self,key,value) :
        if self.num == len(self.maps.maps) :
            self.resize()
        self.maps.add(key,value)
        self.num += 1

    def resize(self) :
        new_maps = BetterMap(self.num * 2)
        for m in self.maps.maps :
            for key,value in m.items :
                new_maps.add(key,value)
        self.maps = new_maps

def main(script) :
    m = HashMap()
    s = string.ascii_lowercase
    for k, v in enumerate(s):
        m.add(k, v)

    for k in range(len(s)):
        print k, m.get(k)

if __name__ == '__main__' :
    import sys
    main(*sys.argv)









