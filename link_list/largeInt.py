#!/usr/bin/env python
# encoding: utf-8

"""
任意大整数的阶乘
"""

from link_list_simple import SimpleLinkList

class LargeInt(object) :

    def __init__(self,num) :
        self.num = num

    def plus(self, num1, num2) :     #num1,num2为SimpleLinkList
        """
        计算大数加法
        """
        carry = 0                    #进位
        pos1 = num1.size()-1
        pos2 = num2.size()-1
        _sum_ = SimpleLinkList()
        while pos1 >= 0 and pos2>=0 :
            #从个位开始求和
            digit1 = int(num1.getitem(pos1))
            digit2 = int(num2.getitem(pos2))
            temp = digit1+digit2+carry
            temp_sum = temp % 10
            _sum_.insert(temp_sum, 0)
            carry = temp/10
            pos1 -= 1
            pos2 -=1
        while pos1 >= 0 :
            digit1 = int(num1.getitem(pos1))
            temp = digit1+carry
            temp_sum = temp % 10
            _sum_.insert(temp_sum, 0)
            carry = temp/10
            pos1 -= 1
        while pos2 >= 0 :
            digit2 = int(num2.getitem(pos2))
            temp = digit2+carry
            temp_sum = temp % 10
            _sum_.insert(temp_sum, 0)
            carry = temp/10
            pos2 -= 1
        if carry > 0 :
            _sum_.insert(carry, 0)

        return _sum_

    def mult(self, num1, num2) :
        """
        计算大数乘法
        """
        length = num1.size()
        pos = length-1
        _sum_ = SimpleLinkList()
        while pos >= 0 :
            digit = int(num1.getitem(pos))
            _sum_ = self.plus(_sum_, self.pow10(self._help(num2,digit),length-pos-1))
            pos -= 1
        return _sum_

    def _help(self,num1,digit) :
        length = num1.size()
        _sum_ = SimpleLinkList()
        for i in xrange(digit) :
            _sum_ = self.plus(num1,_sum_)
        return _sum_

    def pow10(self,num1,times) :
        for i in xrange(times) :
            num1.append(0)
        return num1

    def fib(self) :
        """
        利用大数乘法计算阶乘
        """
        result = SimpleLinkList()
        result.append(1)
        for i in xrange(1,self.num+1) :
            _next_ = self.int_to_list(i)
            result = self.mult(_next_, result)
        return result

    def int_to_list(self,number) :
        number = str(number)
        _link_ = SimpleLinkList()
        length = len(number)
        for i in xrange(length) :
            _link_.append(number[i])
        return _link_


if __name__ == "__main__" :
    while True :
        print
        num =raw_input("Enter a number :")
        p = LargeInt(int(num))
        _result_ = p.fib()
        _result_.display()




