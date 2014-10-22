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

class Edge(object) :
    def __init__(self, start, end, weight=0) :
        """init"""
        self.start = start    #边的起始顶点
        self.end = end        #边的终点
        self.weight = weight  #边的权值

    def get_attribute(self) :
        """获取对象的属性,以tuple的形式返回"""
        return (self.start, self.end, self.weight)

    def set_attribute(self, start, end, weight) :
        """修改(设置)对象的属性值"""
        self.start = start
        self.end = end
        self.weight = weight

class Vertex(object) :
    def __init__(self, value, visited=False) :
        """init"""
        self.value = value      #节点的值
        self.visited = visited  #节点是否被访问过(图的遍历时会用到)

    def get_attribute(self) :
        """获取对象的属性,以tuple的形式返回"""
        return (self.value, self.visited)

#无向图
class UnDirectedGraph(object) :
    "UnDirectedGraph"
    def __init__(self, vertexs=None, edges=None) :
        """
        初始化生成一个图.
        输入:vertexs为节点对象列表,edges为边对象列表.
        """
        self.graph = {}
        if vertexs is not None :
            length = len(vertexs)
            for index in range(length) :
                self.add_vertex(vertexs[index])
        if edges is not None :
            length = len(edges)
            for index in range(length) :
                self.add_edge(edges[index])

    def get_attribute(self) :
        """获取属性"""
        return self.graph

    def add_edge(self, edge) :
        """(无向图)向图中添加边,edge为边类Edge的实例"""
        #该函数的缺点:没有判断要插入的边是否存在,如果存在,只需更新权值即可
        start, end, weight = edge.get_attribute()
        if start not in self.graph :
            self.add_vertex(start)
        if end not in self.graph :
            self.add_vertex(end)
        if self.is_exist_edge(start, end, weight) :
            #如果插入的边已经存在,则更新其权值即可
            self.update_edge(start, end, weight)
            self.update_edge(end, start, weight)
        else :
            self.graph[start]['neighbour'].append(edge)
            self.graph[end]['neighbour'].append(Edge(end,start,weight))

    def update_edge(self, start, end, weight) :
        """"""
        neighbours = self.graph[start]['neighbour']
        for edge in neighbours :
            v_s, v_e, e_w = edge.get_attribute()
            if end == v_e :
                edge.set_attribute(start, end, weight)
                break

    def is_exist_edge(self, start, end, weight) :
        """用于检查(无向图)边edge是否已经存在"""
        #由于是无向图,所以只需判断一个方向是否存在
        neighbours = self.graph[start]['neighbour']
        for edge in neighbours :
            v_s, v_e, e_w = edge.get_attribute()
            if end == v_e :
                return True
        return False

    def add_vertex(self, vertex) :
        """向图中添加节点,vertex为节点类Vertex的实例"""
        value, visited = vertex.get_attribute()
        if value in self.graph :
            raise 'vertex %r already in graph' % value
        self.graph[value] = {}
        self.graph[value]['visited'] = visited
        self.graph[value]['neighbour'] = []

    def visite(self, vertex) :
        """访问节点vertex,即标记vertex的visited为True"""
        self.graph[vertex]['visited'] = True

    def get_vertexs(self) :
        """获取图的所有顶点"""
        ret = []
        for item in self.graph :
            ret.append(item)
        return ret

    def get_visited_vertexs(self) :
        """获取已经访问过的节点的集合"""
        ret = []
        for item in self.graph :
            if self.graph[item]['visited'] is True :
                ret.append(item)
        return ret

    def get_unvisited_vertexs(self) :
        ret = []
        for item in self.graph :
            if self.graph[item]['visited'] is False :
                ret.append(item)
        return ret

#有向图
class DirectedGraph(object) :
    "Graph"
    def __init__(self, vertexs=None, edges=None) :
        """
        初始化生成一个图.
        输入:vertexs为节点对象列表,edges为边对象列表.
        """
        self.graph = {}
        if vertexs is not None :
            length = len(vertexs)
            for index in range(length) :
                self.add_vertex(vertexs[index])
        if edges is not None :
            length = len(edges)
            for index in range(length) :
                self.add_edge(edges[index])

    def get_attribute(self) :
        """获取属性"""
        return self.graph

    def add_edge(self, edge) :
        """(有向图)向图中添加边,edge为边类Edge的实例"""
        #该函数的缺点:没有判断要插入的边是否存在,如果存在,只需更新权值即可
        start, end, weight = edge.get_attribute()
        if start not in self.graph :
            self.add_vertex(start)
        if end not in self.graph :
            self.add_vertex(end)
        if self.is_exist_edge(start, end, weight) :
            self.update_edge(start, end, weight)
        else :
            self.graph[start]['neighbour'].append(edge)

    def update_edge(self, start, end, weight) :
        """"""
        neighbours = self.graph[start]['neighbour']
        for edge in neighbours :
            v_s, v_e, e_w = edge.get_attribute()
            if end == v_e :
                edge.set_attribute(start, end, weight)
                break

    def is_exist_edge(self, start, end, weight) :
        """用于检查(有向图)边edge是否已经存在"""
        neighbours = self.graph[start]['neighbour']
        for edge in neighbours :
            v_s, v_e, e_w = edge.get_attribute()
            if end == v_e :
                return True
        return False

    def add_vertex(self, vertex) :
        """向图中添加节点,vertex为节点类Vertex的实例"""
        value, visited = vertex.get_attribute()
        if value in self.graph :
            raise 'vertex %r already in graph' % value
        self.graph[value] = {}
        self.graph[value]['visited'] = visited
        self.graph[value]['neighbour'] = []

    def visite(self, vertex) :
        """访问节点vertex,即标记vertex的visited为True"""
        self.graph[vertex]['visited'] = True

    def get_vertexs(self) :
        """获取图的所有顶点"""
        ret = []
        for item in self.graph :
            ret.append(item)
        return ret

    def get_visited_vertexs(self) :
        """获取已经访问过的节点的集合"""
        ret = []
        for item in self.graph :
            if self.graph[item]['visited'] is True :
                ret.append(item)
        return ret

    def get_unvisited_vertexs(self) :
        """获取还未访问的节点的集合"""
        ret = []
        for item in self.graph :
            if self.graph[item]['visited'] is False :
                ret.append(item)
        return ret

    def get_weight(self, start, end) :
        """获取节点start到节点end之间的边的权重"""
        #初始值为一个比实际权值更大的数,如果两个节点之间没有边,则返回此数值
        weight = 10000
        neighbours = self.graph[start]['neighbour']
        for edge in neighbours :
            v_s, v_e, e_w = edge.get_attribute()
            if v_e == end :
                weight = e_w
        return weight

    def get_vertex_num(self) :
        """获取图的节点数"""
        return len(self.graph)























