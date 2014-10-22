#!/usr/bin/env python
# encoding: utf-8

#排列的生成算法
#1.序数法
#(1)规则:设n个元素为1,2,...,n.
#(2)特点:n元排列<-->n-1位变进制数.
#(3)对应规则:
#序列(an-1,an-2,...,a1)<-->排列(p)＝(p1p2p3...pn)，
#其中ai为排列（p）中数i＋1所在位置后面比i＋1小的数的个数，
#即排列(p)中从数i＋1开始向右统计不大于i的数的个数
#(4)实例:
#排列--->数: n=4
#(p)=(3124)  <-->  (a3a2a1)=(020)
#数--->排列
#(a3a2a1)=(111)  <-->  (p)=(2341)
#数735233220 --->排列 35A8649712
#排列 3, 5, 7, 9, A, 8, 6, 4, 2, 1 -->  数 5 5 4 4 3 3 2 2 1
#例如:4元排列的生成
#a3a2a1从000到321,分别写出对应的排列序列即可.

#==>>字典序法,算法如下:
#将所有n元排列按照"字典顺序"排成队.初始排序:12.....n
#利用当前排列(p)=(p1,p2,....,pn)求下一个排列:
#(1)求满足关系式pk-1<pk的k的最大值设为i,即i=max{k|pk-1<pk}
#(2)求满足pi-1<pk的k的最大值,设为j,即j=max{k|pi-1<pk}
#(3)pi-1与pj互换位置得(q)=(q1,q2,q3,...,qn)
#(4)将(q)=(q1,q2...qi-1,qi,qi+1...qn)中的qi,qi+1...qn部分的顺序逆转,得到新排序q1,q2...qi-1,qn...,qi+1,qi
#例:设p1,p2,p3,p4=3421:i=2,j=2,p1与p2交换得q1q2q3q4=4321,321逆转得到下一个排列4123
#本质是不断在变换an-1,an-2...,a1
class Permutation_Dict_Order() :
    "字典序法生成排列"
    def __init__(self,arrange_list) :
        """init"""
        self.arrange_list = arrange_list

    def permutation(self,arrange_list) :
        #0.打印序列
        self.display(arrange_list)
        #1.求满足关系式pk-1<pk的k的最大值设为i,即i=max{k|pk-1<pk}
        #  此处取的下标
        i=self.get_max_i(arrange_list)
        if i==0 :
            return
        #2.求满足pi-1<pk的k的最大值,设为j,即j=max{k|pi-1<pk}
        #  此处取下标
        j=self.get_max_j(arrange_list,i)
        #3.pi-1与pj互换位置得(q)=(q1,q2,q3,...,qn)
        self.swap(arrange_list,i-1,j)
        #4.将(q)=(q1,q2...qi-1,qi,qi+1...qn)中的qi,qi+1...qn部分的顺序逆转
        self.reverse(arrange_list,i)
        self.permutation(arrange_list)

    def get_max_i(self,arrange_list) :
        """
        #1.求满足关系式pk-1<pk的k的最大值设为i,即i=max{k|pk-1<pk}
        """
        i = 0
        length = len(arrange_list)
        for index in range(length-1) :
            if arrange_list[index] < arrange_list[index+1] :
                i = index+1
        return i

    def get_max_j(self,arrange_list,i) :
        """
        #2.求满足pi-1<pk的k的最大值,设为j,即j=max{k|pi-1<pk}
        """
        j = 0
        length = len(arrange_list)
        temp = i - 1
        temp_value = arrange_list[temp]
        for index in range(temp,length) :
            if temp_value < arrange_list[index] :
                j = index
        return j

    def swap(self,arrange_list,i,j) :
        """
        #3.pi-1与pj互换位置
        """
        temp = arrange_list[i]
        arrange_list[i] = arrange_list[j]
        arrange_list[j] = temp

    def reverse(self,arrange_list,i) :
        """
        #4.将(q)=(q1,q2...qi-1,qi,qi+1...qn)中的qi,qi+1...qn部分的顺序逆转
        """
        length = len(arrange_list)
        low = i
        high = length-1
        mid = (low+high)/2
        while low <= mid and high>=mid :
            temp = arrange_list[high]
            arrange_list[high] = arrange_list[low]
            arrange_list[low] = temp
            low += 1
            high -= 1

    def display(self,arrange_list) :
        """打印序列"""
        length = len(arrange_list)
        for index in range(length) :
            print arrange_list[index],
        print

#邻位互换生成算法
#初始排列:1234.....n(当一个数上方的箭头所指向的一侧相邻的数比该数小时,则该数
#处于活动状态)
#(1)若排列(p)=(p1p2...pn)中无一数处于活动状态,则停止,否则转(2)
#(2)求所有处于活动状态的数中的最大者,设为k,k和它的箭头所指的一侧的相邻数互换位置,转(3)
#(3)令比k大的所有数的箭头改变方向,转(1).

class Element(object) :
    def __init__(self,data,direction) :
        self.data = data    #数值
        self.direction = direction    #箭头方向,0表示向左,1表示向右

class Permutation(object) :
    "邻位互换生成算法"
    def __init__(self,arrange_list) :
        """init"""
        self.arrange_list = arrange_list

    def permutation(self,arrange_list) :
        """邻位互换生成算法"""
        #打印序列
        self.display(arrange_list)
        index = self.find_max_active(arrange_list)
        if index == -1 :
            return
        k = arrange_list[index].data
        self.swap(arrange_list,index)
        self.change_direction(arrange_list,k)
        self.permutation(arrange_list)

    def find_max_active(self,arrange_list) :
        """
        #1,#2-1
        寻找处于活动状态的数中的最大数.
        返回:若没有处于活动状态的数,返回-1;否则返回处于活动状态的数的最大数的下标
        """
        length = len(arrange_list)
        max_num = 0          #用于保存当前最大的处于活动状态的数字
        max_num_index = -1    #处于活动状态的最大的数的下标
        for index in range(length) :
            if arrange_list[index].direction == 0 :    #箭头指向左边
                if index != 0 :                        #不是第一个元素
                    if arrange_list[index-1].data < arrange_list[index].data :
                        #箭头所指的一侧相邻的数比该数小,则该数处于活动状态
                        if arrange_list[index].data > max_num :
                            #保存当前的最大处于活动状态的数字
                            max_num = arrange_list[index].data
                            max_num_index = index
            elif arrange_list[index].direction == 1 :  #箭头指向右边
                if index != length-1 :
                    if arrange_list[index+1].data < arrange_list[index].data :
                        #箭头所指的一侧相邻的数比该数小,则该数处于活动状态
                        if arrange_list[index].data > max_num :
                            #保存当前最大处于活动状态的数字
                            max_num = arrange_list[index].data
                            max_num_index = index
        return max_num_index


    def swap(self,arrange_list,index) :
        """
        #2-2
        互换arrange_list中与下标为index的数的箭头所知一侧相邻的数
        """
        swap_index = index
        if arrange_list[index].direction == 1 :
            #箭头指向右边
            swap_index = index+1
        else :
            #箭头指向左边
            swap_index = index-1
        temp_data = arrange_list[swap_index].data
        temp_direction = arrange_list[swap_index].direction

        arrange_list[swap_index].data = arrange_list[index].data
        arrange_list[swap_index].direction = arrange_list[index].direction

        arrange_list[index].data = temp_data
        arrange_list[index].direction = temp_direction

    def change_direction(self,arrange_list,k) :
        """
        #3
        令所有比k大的数转变箭头方向
        """
        length = len(arrange_list)
        for index in range(length) :
            if arrange_list[index].data > k :
                if arrange_list[index].direction == 0 :
                    arrange_list[index].direction = 1
                else :
                    arrange_list[index].direction = 0

    def display(self,arrange_list) :
        """打印出一个排列"""
        length = len(arrange_list)
        for index in range(length) :
            print arrange_list[index].data,
        print

#组合生成算法
#规律:低位累加,逐位前移
#(1)设组合C1C2....Cr满足C1<C2<...<Cr,则Cr<=n,Cr-1<=n-1,...,,C1<=n-r+1
#   即Ci<=n-r+i,i=1,2,3,...,r
#(2)当Cj<n-r+j时,令i=max{j|Cj<n-r-j},并令Dk=Ck,1<=k<i;Di=Ci+1;Dk=Dk-1+1,i<k<=r
#得新组合D1D2...Dr,若每个Cj=n-r+j,则已经到达最后一个组合,生成完毕.
#算法:
#初始组合:(12...r)
#当前组合:c1c2...cr
#(1)若i=max{j|Cj<n-r+j}存在,转(2),否则停止;
#(2)Ci<--Ci + 1;
#(3)Cj<--Cj-1 + 1,j=i+1,i+2,...,r.输出(C1C2...Cr),转(1)
class Combination(object) :
    "组合生成算法"
    def __init__(self,n,r) :
        """init"""
        self.n = n
        self.r = r

    def combination(self,arrange_list) :
        """生成组合"""
        #0.打印序列
        self.display(arrange_list)
        #1.i=max{j|Cj<n-r+j}
        i=self.get_max_i(arrange_list)
        if i == -1 :
            return
        #2.Ci<--Ci + 1;
        arrange_list[i] += 1
        #3.Cj<--Cj-1 + 1,j=i+1,i+2,...,r.等价于Ci + 1 --> Ci+1
        self.do_copy(arrange_list,i)
        self.combination(arrange_list)

    def get_max_i(self,arrange_list) :
        """
        #1.i=max{j|Cj<n-r+j},i为下标,j从1开始
        """
        length = len(arrange_list)
        max_j = -1
        for index in range(length) :
            temp = self.n - self.r + index + 1
            if arrange_list[index] < temp :
                max_j = index
        return max_j

    def do_copy(self,arrange_list,i) :
        """
        #3.Cj<--Cj-1 + 1,j=i+1,i+2,...,r.
        Ci + 1 --> Ci+1
        """
        for index in range(i,self.r-1) :
            arrange_list[index+1] = arrange_list[index] + 1

    def display(self,arrange_list) :
        """打印组合序列"""
        length = len(arrange_list)
        for index in range(length) :
            print arrange_list[index],
        print

if __name__ == "__main__" :
    """
    data = []
    elem1 = Element(1,0)
    elem2 = Element(2,0)
    elem3 = Element(3,0)
    elem4 = Element(4,0)
    data.append(elem1)
    data.append(elem2)
    data.append(elem3)
    data.append(elem4)
    arrange = Permutation(data)
    arrange.permutation(arrange.arrange_list)
    print "Dict Order:"
    data2 = [1,2,3,4]
    test = Permutation_Dict_Order(data2)
    test.permutation(test.arrange_list)
    """
    print "Combination:"
    comb = Combination(10,5)
    comb.combination([1,4,6,7,8])





