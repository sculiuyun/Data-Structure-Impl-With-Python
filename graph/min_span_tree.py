#!/usr/bin/env python
# encoding: utf-8

from Graph import Edge,Vertex,UnDirectedGraph
#最小生成树算法
#Kruskal MST Algorithm
#Initially,let T <--空集 be the empty graph on V
#Examine the edges in E in increasing order of weight
#  ->if an edge connects two unconnected component of T,then add the edge to T.
#  ->else,discard the edge and continue
#Terminate when there is only one connected component.(Or you can continue through all the edges)

#1.记Graph中有v个顶点,e条边
#2.新建图Graph-new,Graph-new中拥有原图中相同的e个顶点,但是没有边
#3.将原图Graph中的所有e个边按权值从小到大排序
#4.遍历排序后的边,判断边是否连接了两个不同的分支,是的话,合并这两个分支,这条边也属于最小生成树,否则,继续循环

def kruskal(graph) :    #Kruskal最小生成树算法
    #0.定义要返回的边列表[(start,end,weight),]
    ret = []
    #1.建立最小生成树的分支,对少个顶点建多少个分支分支中没有边
    temp = {}
    temp_graph = graph.get_attribute()
    for key in temp_graph :
        temp[key] = key
    #2.将边按权重升序排列
    #2.1.遍历图,得到所有的边列表
    edge_list = []    #edge_list = [(start, value, weight),]
    for key in temp_graph :
        neighbours = temp_graph[key]['neighbour']
        length = len(neighbours)
        for index in range(length) :
            start, end, weight = neighbours[index].get_attribute()
            edge_list.append((start, end, weight))
    #2.2.利用库函数对edge_list进行排序
    edge_list.sort(key = lambda edge : edge[2])
    #3.遍历边的升序序列,判断边是否连接了两个不同的分支,是的话,合并分支,这条边也属于最小生成树中的边
    #以全局变量X定义节点集合，即类似{'A':'A','B':'B','C':'C','D':'D'},
    #如果A、B两点联通，则会更改为{'A':'B','B':'B",...},即任何两点联通之后，两点的值value将相同。
    for edge in edge_list :
        start, end, weight = edge
        if temp[start] != temp[end] :
            ret.append((start,end,weight))
            for key in temp :
                #最后修改temp[end] = temp[start]
                if key is not end and temp[key] == temp[end] :
                    temp[key] = temp[start]
            temp[end] = temp[start]
        else :
            continue
    return ret

#Prim算法基本思想:按逐个将顶点连通的方式来构造最小生成树
#从连通的网络N={V,E}中那个的某一个顶点u0出发,选择与它关联的具有最小权值的边(u0,v),
#将其顶点加入到生成树的集合中.以后每一步从一个顶点在U中,而另一个顶点不在U中的各条边中,
#选择权值最小的边(u,v),把该边加入到生成树的边集TE中,把它的定点加入到集合U中.
#如此重复执行,直到网络中的所有定点都加入到生成树的顶点集合中为止.

#假设G(V,E)是一个具有n个顶点的带权无向连通图,T(U,TE)是G的最小生成树,其中U是T的
#顶点集,TE是T的边集,则构造G的最小生成树T的步骤如下:
#(1).初始状态,TE为空,U={v0},v0属于V
#(2).在所有的u属于U,v属于V-U的边(u,v)属于E中找出一条代价最小的边(u',v'),并入TE,
#    同时将v'并入U
#(3)重复执行(2) n-1 次,直到U=V为止
def prim(graph) :
    #0.最小生成树的边集ret和图graph的所有顶点列表
    ret = []
    vertexs = graph.get_vertexs()
    length = len(vertexs)
    temp_graph = graph.get_attribute()
    #1.选择任意一个顶点,加入到生成树定点集合中,此处选择第一个顶点
    graph.visite(vertexs[0])
    visited_vertexs = [vertexs[0]]
    #2.在所有的u属于U,v属于V-U的边(u,v)属于E中找出一条代价最小的边(u',v'),并入TE,同时将v'并入U
    #2.1.进行n-1次操作,每次操作找出一条满足步骤2中条件的边
    for count in range(length-1) :
        #2.2.遍历已经访问过的的顶点
        min_weight_edge = Edge('A','B',100000)    #记录最小权值的边
        for item in visited_vertexs :
            #2.3.遍历每个i顶点的邻接表,找出权值最小的边,加入到最小生成树的边集中
            neighbours = temp_graph[item]['neighbour']    #获取该节点的邻接点列表
            for edge in neighbours :
                start, end, weight = edge.get_attribute()
                #end未访问过
                if end not in visited_vertexs :
                    if weight < min_weight_edge.weight :
                        min_weight_edge.set_attribute(start,end,weight)
        graph.visite(min_weight_edge.end)
        visited_vertexs.append(min_weight_edge.end)
        ret.append(min_weight_edge.get_attribute())
    return ret

if __name__ == "__main__" :
    vertexs = [Vertex('A'),Vertex('B'),Vertex('C'),Vertex('D'),Vertex('E'),Vertex('F')]
    edges = [Edge('A','B',1),Edge('A','F',1),Edge('B','C',2),Edge('F','C',3),Edge('F','E',3),Edge('C','D',5),Edge('D','E',3)]
    graph = UnDirectedGraph(vertexs, edges)
    kruskal_min = kruskal(graph)
    for item in kruskal_min :
        print item,
    print
    prim_min = prim(graph)
    for elem in prim_min :
        print elem,






