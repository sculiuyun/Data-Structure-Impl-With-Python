#!/usr/bin/env python
# encoding: utf-8

"""
Graph = {
        'vertex.value' :{
            visited : False,
            neighbour : [edge,]
        }
    }
"""

from Graph import Vertex,Edge,DirectedGraph

#有向无环图(Directed Acyclic Graph,DAG)是一个无环的有向图
#判断一个有向图是否是有环图的简单方法是拓扑排序,也可以采用深度有限搜索算法进行判断

def indegree(graph) :
    """计算图graph中各个顶点的入度"""
    indeg = {}
    temp_graph = graph.get_attribute()
    #初始化各顶点的入度为0
    for vertex in temp_graph :
        indeg[vertex] = 0
    for vertex in temp_graph :
        #节点的邻接表
        neighbours = temp_graph[vertex]['neighbour']
        for edge in neighbours :
            start, end, weight = edge.get_attribute()
            indeg[end] += 1
    return indeg

#构造拓扑序列的方法
#(1).在有向图中选择任意一个没有前驱的顶点输出;
#(2).在图中删除该顶点以及所有以它为起点的边;
#(3).重复上述步骤(1)(2),直到全部顶点都已经输出,此时其定点输出即为一个拓扑有序序列;
#    或者直到图中没有无前驱的节点为止,此情形表示图中存在环.
def top_sort(graph) :
    """若有向图graph无回路,返回g的顶点的一个拓扑序列"""
    #return: 若图graph无回路,则返回一个拓扑序列;否则返回None
    order = []                 #存储拓扑序列
    indeg = indegree(graph)    #计算各个节点的入度
    queue = []           #队列,可以从之前的写的数据结构导入,也可以用list代替
    temp_graph = graph.get_attribute()
    for vertex in temp_graph : #将入度为0的节点入队
        if indeg[vertex] == 0 :
            queue.append(vertex)
    while len(queue) > 0 :
        vertex = queue.pop(0)  #删除队首元素
        order.append(vertex)   #将节点添加到拓扑序列中
        #遍历vertex的邻接节点,将各邻接节点的入度减一
        neighbours = temp_graph[vertex]['neighbour']
        for edge in neighbours :
            start, end, weight = edge.get_attribute()
            indeg[end] -= 1
            if indeg[end] == 0 :
                queue.append(end)
    if len(order) < len(temp_graph) :
        return None
    else :
        return order

if __name__ == "__main__" :
    vertexs = [Vertex('A'),Vertex('B'),Vertex('C'),Vertex('D'),Vertex('E'),Vertex('F')]
    edges = [Edge('A','B',1),Edge('A','F',1),Edge('B','C',1),Edge('F','C',1),Edge('F','E',1),Edge('C','D',1),Edge('D','E',1),Edge('A','B',3)]
    graph = DirectedGraph(vertexs, edges)
    #indegree = indegree(graph)
    #for key in indegree :
    #    print key,indegree[key]
    order = top_sort(graph)
    for vertex in order :
        print vertex,











