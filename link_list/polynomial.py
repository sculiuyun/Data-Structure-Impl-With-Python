#!/usr/bin/env python
# encoding: utf-8

"""
一元多项式的表示及其加,减,乘运算
P(x) = p0+p1*X+p2*X^2+...+pn*X^n
1.多项式P(x)由n+1个系数组成,在计算机中可以使用线性表P来表示:
    P=(p0,p1,p2,...pn)
2.设Q(x)是一个m次多项式,同样地可以用线性表Q来表示:
    Q=(q0,q1,q2,...qn)
3.为了不失一般性,多项式P(x)表示如下:
    P =((p0,q0),(p1,q1),(p2,q2)...(pn,qn))
"""

from link_list_simple import SimpleLinkList

class PolyNode(object) :
    "多项式节点"
    def __init__(self, coef, expo) :
        self.coef = coef    #系数
        self.expo = expo    #指数

class Polynomial(object) :
    "多项式类"
    def __init__(self) :
        """
        init.
        """
        self.polylist = SimpleLinkList()

    def insert(self, coef, expo) :
        """
        往多项式链表中加入一项.按指数的大小顺序插入
        """
        node = PolyNode(coef, expo)
        if self.polylist.empty() :
            #多项式链表为空
            self.polylist.append(node)
        else :
            length = self.polylist.size()
            for pos in xrange(length) :
                item = self.getitem(pos)
                if item.expo > expo :
                    self.polylist.insert(node,position=pos)
                    break
            else :
                self.polylist.append(node)

    def size(self) :
        """
        返回多项式的项数.
        """
        return self.polylist.size()

    def display(self) :
        """
        显示多项式.
        """
        pass

    def plus(self, other) :
        """
        多项式加法...参数other是另一个多项式的链表表示
        """
        _sum_ = SimpleLinkList()            #表示两个多项式和的链表
        pos_self = 0
        pos_other = 0
        length_self = self.polylist.size()
        length_other = other.size()
        while pos_self < length_self and pos_other < pos_other :
            #从两个相加的多项式链表中取出各个多项式数据项
            item_self = self.polylist.getitem(pos_self)
            item_other = other.getitem(pos_other)
            length_sum = _sum_.size()
            #self.polylist中的指数较小
            if item_self.expo < item_other.expo :
                _sum_.append(item_self)
                pos_self += 1
            #other中的指数较小
            elif item_self.expo > item_other.expo :
                _sum_.append(item_other)
                pos_other += 1
            #两个指数相同
            else :
                sum_coef = item_self.coef + item_other.coef
                temp_item = PolyNode(sum_coef, item_self.expo)
                _sum_.append(temp_item)
                pos_self += 1
                pos_other += 1
        while pos_self < length_self :
            #将self.polylist的剩余数据项放入结果链表中
            _sum_.append(item_self)
            pos_self += 1
        while pos_other < length_other :
            #将other的剩余数据项放入结果链表中
            _sum_.append(item_other)
            pos_other += 1
        return _sum_

    def sub(self, other) :
        """
        多项式减法.P(x)-Q(x) = P(x) + (-Q(x))
        """
        other = self.get_opposite(other)
        self.plus(other)

    def mul(self, other) :
        """
        多项式乘法.
        """
        _product_ = SimpleLinkList()            #用于存放乘积的多项式链表
        pos_self = 0
        length_self = self.polylist.size()
        length_other = other.size()

        while pos_self < length_self :
            item_self = self.polylist.getitem(pos_self)
            pos_other = 0
            temp_list = SimpleLinkList()
            while pos_other < length_other :
                item_other = other.getitem(pos_other)
                temp_coef = item_self.coef * item_other.coef
                temp_expo = item_self.expo + item_other.expo
                temp_item = PolyNode(temp_coef, temp_expo)
                temp_list.append(temp_item)
                pos_other += 1
            #此处需要实现plus(self,operand1,operand2)
            _product_ = self.plus(_product_,temp_list)
            pos_self += 1
        return _product_


    def get_opposite(self,destination) :
        """
        对多项式的每一个系数取相反数.参数destination是要操作的多项式链表
        """
        pos = 0
        length = destination.size()
        while pos < length :
            item = destination.getitem(pos)
            item.coef = -item.coef
            destination.setitem(item,pos)
            pos += 1
        return destination







