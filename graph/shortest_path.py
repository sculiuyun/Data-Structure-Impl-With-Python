#!/usr/bin/env python
# encoding: utf-8

from Graph import Edge,Vertex,DirectedGraph

#无权无向图的最短路径
#有权无向图的最短路径

"""
Graph = {
    'vertex.value' :{
        visited : False,
        neighbour : [edge,]
    }
}
"""
#单源最短路径
#单源最短路径问题是指给定一个带权有向网net的源点,求v到net中其他顶点的最短路径.
#如果(v0,v1,...,vk,vj)是最短路径,则(v0,v1,...,vk)也是最短路径,要存储v0到vj的
#最短路径path[j],只需存储此路径上vj的前一个顶点vk即可,也就是可以表示成path[j]=k,
#事实上,现在路由器中的路由算法就采用了种方法存储从一个节点到另一个网络节点的路由路径的.

#Dijkstra提出了一种按最短路径长度递增的次序逐次生成最短路径的算法,其特点是首先求出最短的
#一条最短路径,然后再求长度次短的一条最短路径,依此类推求出其他最短路径.

#设集合U存放已经求得最短路径的端点,设源端点为Vs,在初始状态下U={Vs},然后每求得一条最短路径,
#就将路径上的端点加入到U中,直到 U=V(V是图中所有顶点的集合)

#用dist存储当前找到的从源点Vs到其他各顶点的最短路径的长度,其初态是:
#如果存在边<Vs,Vi>,则dist[i]=weight(s,i)

#Dijkstra算法的思路
#(1)构造dist的初始值如下:
#dist[i]=0,Vi=Vs; dist[i]=NAN,<Vs,Vi>不属于E； dist[i]=weight(s,i),<Vs,Vi>属于E
#路径path的值:path[i]=s,<Vs,Vi>属于E; path[i]=-1,<Vs,Vi>不属于E;
#此处path[i] = -1表示还没有求出最短路径,path[i]表示路径上的一个顶点.
#(2)选择Vj,使得dist[j]=min{dist[j] | Vj属于V-U},将Vj加入U中;
#(3)修改从Vs到V-U中任意一顶点Vk当前所求得的最短路径,如果
#   dist[j]+weight(j,k) < dist[k]
#   则dist[k] = dist[j]+weight(j,k)
#     path[k] = j
#(4)重复(2)(3)共n-1次,此时将求出从Vs到其余各顶点的最短路径

#权值必须是正的

def dijkstra(graph,v_s) :
    """使用Dijkstra算法计算图graph中顶点v_s到其他顶点的最短路径"""
    dist = {}    #用于存储当前找到的从源点v_s到其他各顶点的最短路径的长度
    path = {}    #用于存储路径上的上一个顶点,-1表示还没有求出最短路径
    temp_graph = graph.get_attribute()
    #1.初始化dist,path,u_vertex
    dist[v_s] = 0
    for item in temp_graph :
        if item != v_s :
            dist[item] = graph.get_weight(v_s,item)
            if dist[item] <10000 :
                path[item] = v_s    #path[i]=s表示路径的上一个顶点
            else :
                path[item] = -1     #path[item]=-1表示还没有求出最短路径
    #设置顶点v_s的访问标志visited为True
    graph.visite(v_s)
    vertex_num = graph.get_vertex_num()
    #重复步骤(2)(3) vertex_num-1次,求出所有从v_s点出发到其余各点的最短路径
    for index in range(1,vertex_num) :
        #2.选择Vj,使得dist[j] = min{dist[j] | Vj属于V-U},将Vj加入U
        vertexs_unvisited = graph.get_unvisited_vertexs()    #位访问过的节点,即V-U
        min_val = 10000
        temp_vertex = v_s    #记录当前dis[v]最小的顶点
        for vertex in vertexs_unvisited :
            if dist[vertex] < min_val :
                temp_vertex = vertex
                min_val = dist[vertex]
        graph.visite(temp_vertex)
        #3.更新当前最短路径及距离,修改从Vs到V-U中任一顶点的最短路径,如果
        #  dist[j]+weight[j,k] < dist[k]
        #  则新的Vs到Vk的当前求的的最短路径为(Vs,...,Vj,Vk),修改dist[k]及path[k]如下:
        #  dist[k] = dist[j] + weight[j,k]
        #  path[k] = j
        for item in vertexs_unvisited :
            if item != temp_vertex :
                new_dist = dist[temp_vertex] + graph.get_weight(temp_vertex,item)
                if new_dist < dist[item] :
                    dist[item] = new_dist
                    path[item] = temp_vertex
    return path

#Floyd算法求的是所有节点之间的最短路径,并且可以处理权值为负的边,时间复杂度为O(n^3)
#定义Dk,i,j为从vi只使用v1,v2,...,vk作为中间顶点的最短路径的权.
#Floyd算法的基本思想是动态规划:
#(1).求出顶点Vi和Vj不经过任何顶点的最短路径,路径的长度就是二者之间边的权重,
#    表示为:P(0,i,j)=C(i,j).
#(2).当求出P(k-1,i,j)后,即Vi到Vj经过V1到Vk-1中的某些顶点的最短路径.
#    则:Vi到Vj的中间经过V1到Vk中某些顶点的最短路径P(k,i,j)

if __name__ == "__main__" :
    vertexs = [Vertex('v0'),Vertex('v1'),Vertex('v2'),Vertex('v3'),Vertex('v4')]
    edges = [Edge('v0','v1',100),Edge('v0','v4',10),Edge('v0','v2',30),Edge('v2','v1',60),Edge('v2','v3',60),Edge('v3','v1',10),Edge('v4','v3',50)]
    graph = DirectedGraph(vertexs, edges)
    order = dijkstra(graph,'v0')
    print order
















