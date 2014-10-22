#!/usr/bin/env python
# encoding: utf-8

from Graph import Edge,Vertex,UnDirectedGraph

#图的遍历算法:深度优先(DFS)和广度优先(BFS)

#深度优先搜索(Depth First Search)在搜索过程中,每当访问一个节点v后,DFS将递归
#访问它的所有未被访问的到的相邻的节点,实际结果是沿着图的某一个分支进行搜索,
#直到末端位置,然后进行回溯,沿另一分支进行搜索.

def depth_first_search(graph, root=None) :
    """DFS"""
    order = []    #用于存储深度优先搜索所的序列
    temp_graph = graph.get_attribute()
    def dfs(vertex) :
        #访问该节点
        graph.visite(vertex)
        order.append(vertex)
        neighbours = temp_graph[vertex]['neighbour']
        for edge in neighbours :
            start, end, weight = edge.get_attribute()
            if temp_graph[end]['visited'] is False :
                dfs(end)
    if root is not None :
        #从root节点开始进行深度有限搜索
        dfs(root)
    #遍历剩余未访问的节点
    for node in temp_graph :
        if temp_graph[node]['visited'] is False :
            dfs(node)
    return order

#广度优先搜索类似于树的层次遍历.
#如从顶点v出发进行搜索,在访问了v之后,依次访问v未被访问的邻接点,直到图中所有被访问的顶点的邻接点都被访问完为止;
#如果这时图中还有没有被访问的节点,将选择一个未被访问的节点作为起始点继续进行搜索,直到图中所有的顶点被访问到为止.
def breadth_first_search(graph, root=None) :
    """BFS"""
    order = []    #用于存储广度优先搜索所的序列
    temp_graph = graph.get_attribute()
    queue = []
    def bfs(vertex) :
        #访问该节点
        graph.visite(vertex)
        queue.append(vertex)
        while len(queue) > 0 :
            temp = queue.pop(0)
            order.append(temp)
            neighbours = temp_graph[temp]['neighbour']
            for edge in neighbours :
                start, end, weight = edge.get_attribute()
                if temp_graph[end]['visited'] is False :
                    queue.append(end)
                    graph.visite(end)
    if root is not None :
        bfs(root)
    #遍历剩余未遍历的节点
    for node in temp_graph :
        if temp_graph[node]['visited'] is False :
            bfs(node)
    return order

if __name__ == '__main__' :
    vertexs = [Vertex('A'),Vertex('B'),Vertex('C'),Vertex('D'),Vertex('E'),Vertex('F')]
    edges = [Edge('A','B',1),Edge('A','F',1),Edge('B','C',1),Edge('F','C',1),Edge('F','E',1),Edge('C','D',1),Edge('D','E',1),Edge('A','B',3)]
    graph = UnDirectedGraph(vertexs, edges)
    order = breadth_first_search(graph,root='A')
    for vertex in order :
        print vertex,
