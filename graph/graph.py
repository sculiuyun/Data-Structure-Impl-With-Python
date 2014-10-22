#!/usr/bin/env python
# encoding: utf-8

"""
Representing Graphs : Adjacency Lists
-->用邻接表表示图
Array Adj of |V| linked lists
In python : Adj = dictionary of list/tuple values vertex = any hashable object
比如说，这有一张简单的图：

　A -> B
　A -> C
　B -> C
　B -> D
　C -> D
　D -> C
　E -> F
　F -> C

这个图有6个节点(A-F)和8个弧。它可以通过下面的Python数据结构来表示：
graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}
"""

from queue.queue import Queue

class DirectedGraph(object) :

    def __init__(self) :
        self.Adj = {}
        self.visited = {}

    def itervertics(self) :
        """
        以任意的顺序迭代出该图的所有节点
        """
        return self.Adj.iterkeys()

    def add_vertex(self, u) :
        """
        向图中添加顶点.
        A vertex can be any hashable ogject, eg,an interger or a tuple.
        """
        if u in self.Adj :
            raise 'vertex %r already in graph' % u
        #set为集合类型,集合中不会出现重复的元素
        self.Adj[u] = set()

    def remove_vertex(self, u) :
        """
        remove specified vertex from the graph.
        """
        #remove incoming edges to the vertex
        for key in self.Adj.keys() :
            if u in Adj[key] :
                Adj[key].remove(u)
        #remove all outgoing edges from the vertex
        del self.Adj[u]

    def add_edge(self, u, v) :
        """
        add an edge from vertex u to vertex.
        """
        #vertex u is not in Adj
        if u not in self.Adj :
            self.add_vertex(u)
        self.Adj[u].add(v)
        if v not in self.Adj :
            self.add_vertex(v)

    def remove_edge(self, u, v) :
        """
        remove the edge from u to v.
        """
        if v not in self.Adj[u] :
            raise 'the edge from u to v not exist.'
        self.Adj[u].remove(v)

    def neighbors(self, u) :
        """
        return the set of neighbors of(vertex adjacent to) u.
        """
        return self.Adj[u]

    def find_path(self,start,end,path=[]) :
        """
        find a path from start to end.
        """
        path = path +[start]
        if start == end :
            return path
        if not self.Adj.has_key(start) :
            return None
        for node in self.Adj[start] :
            if node not in path :
                newpath = self.find_path(node,end,path)
                if newpath :
                    return newpath
        return None

    def find_all_paths(self,start,end,path=[]) :
        path = path + [start]
        if start == end :
            return [path]
        if not self.Adj.has_key(start) :
            return []
        paths=[]
        for node in self.Adj[start] :
            if node not in path :
                newpaths = self.find_all_paths(node,end,path)
                for newpath in newpaths :
                    paths.append(newpath)
        return paths

    def find_shortest_path(self,start,end,path) :
        path = path+[start]
        if start == end :
            return path
        if not self.Adj.has_key(start) :
            return None
        shortest = None
        for node in self.Adj[start] :
            if node not in path :
                newpath = find_shortest_path(node,end,path)
                if newpath :
                    if not shortest or len(newpath) < len(shortest) :
                        shortest = newpath
        return shortest

    def critical_path(self) :
        """
        关键路径.
        与AOV相对应的是AOE(activity on edge)网,边表示活动的网,AOE是一种边带
        有权值的有向无环图,用顶点来表示事件(event),边表示活动,边上的权值表示
        活动持续的时间,AOE网通常用来计算工程的最短完成时间.
        """
        pass













