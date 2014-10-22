#!/usr/bin/env python
# encoding: utf-8

"""
1.左旋转字符串
定义字符串的左旋转操作:把字符串前面的若干个字符移动到字符串的尾部.
如把字符串 abcdef 左旋转 2 位得到字符串 cdefab。请实现字符串左旋转的函数，
要求对长度为 n 的字符串操作的时间复杂度为 O(n)，空间复杂度为 O(1)。
"""
#解法一:暴力移位法
#移动一位
def left_shift_one(op_list) :
    length = len(op_list)
    temp = op_list[0]        #保存第一个字符
    for index in xrange(length-1) :
        op_list[index] = op_list[index+1]
    op_list[length-1] = temp

#移动m位
def left_shift_m(op_list,m) :
    while m>0 :
        left_shift_one(op_list)
        m -= 1

#解法二:三步旋转法
#对于这个问题,换一个角度思考:
#将一个字符串分成X和Y两个部分,在每部分字符串上定义反转操作,如X^T,即把X的所有
#字符反转(如,X="abc",那么X^T="cba"),那么就可以得出以下的结论:
#(X^TY^T)^T=YX.显然解决了字符串的反转问题.
#例如字符串"abcdef",若要让def翻转到abc的前头,只需要一下三个步骤:
#1.首先分为两个部分,X:abc,Y:def;
#2.将X反转,X->X^T,即得到abc->cba;同样将Y反转;
#3.反转上述得到的结果字串X^TY^T,即字串cbafed给予反转,得到cdafed->defabc

def reverse(op_list,start,end) :
    while start < end :
        temp = op_list[start]
        op_list[start] = op_list[end]
        op_list[end] = temp
        start += 1
        end -= 1

def left_shift(op_list,m) :
    if m < 0:
        raise Exception('m is less than 0')
    length = len(op_list)
    m %= length    #若要左移大于n位,那么效果和%n是等价的
    reverse(op_list,0,m-1)
    reverse(op_list,m,length-1)
    reverse(op_list,0,length-1)


