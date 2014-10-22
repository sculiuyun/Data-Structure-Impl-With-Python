#!/usr/bin/env python
# encoding: utf-8

"""
简单计算器:用于进行简单的整型四则运算
"""

from stack_v2 import Stack

class Calculator(object) :
    "Calculator"
    def __init__(self, expression) :
        """
        init.
        """
        self.expression = expression

    def calculator(self) :
        """
        calculator.
        """
        if self.is_invalid() :    #输入的表达式合法
            operand = Stack()        #操作数栈
            operator = Stack()       #操作符栈
            operator.push('=')       #在操作符栈中压入一个'='
            length = len(self.expression)
            temp = 0
            for index in xrange(length) :
                charactor = self.expression[index]
                if self.is_operand(charactor) :        #操作数
                    pass
                elif self.is_operator(charactor) :     #操作符
                    if temp != index :
                        operand.push(self.expression[temp:index])    #将操作数入栈
                        temp = index + 1
                    if charactor == '=' and operator.top() == '=':   #如果读入等号,且操作符栈顶操作符为'=',则返回结果
                        result = operand.pop()
                        return result
                    else :
                        if self.precede(operator.top(),charactor) == '>':
                            #栈顶操作符的优先级大于当前读入的操作符的优先级
                            #这种情况下:从操作数栈中弹出两个操作数(left,right),从operator栈中弹出操作符theta,
                            #形成运算指令:left theta right,结果如栈operand
                            #将当前操作符入栈
                            right_operand = int(operand.pop())
                            left_operand = int(operand.pop())
                            theta = operator.pop()
                            temp_result = self.operate(left_operand,theta,right_operand)
                            operand.push(temp_result)
                            if charactor != '=' :
                                operator.push(charactor)
                            else :
                                while operator.top() != "=" :
                                    right_operand = int(operand.pop())
                                    left_operand = int(operand.pop())
                                    theta = operator.pop()
                                    temp_result = self.operate(left_operand,theta,right_operand)
                                    operand.push(temp_result)
                        else :
                            #栈顶操作符的优先级小于当前读入的操作符的优先级,将操作符入栈
                            operator.push(charactor)
                else :
                    print "you have input an invalid charactor : %s" % self.expression[index]
                    return
            return operand.top()
        else :
            return

    def is_operator(self,charactor) :
        """
        判断一个字符是否是操作符
        """
        operator = ['+','-','*','/','(',')','=']
        if charactor in operator :
            return True
        else :
            return False

    def is_operand(self,charactor) :
        """
        判断一个字符是否是数字
        """
        digit = ['0','1','2','3','4','5','6','7','8','9']
        if charactor in digit :
            return True
        else :
            return False

    def precede(self,operator,cur_operator) :
        """
        比较当前读取的操作符和操作符栈栈顶操作符的优先级.
        =:优先级最低
        +,-:优先级中
        *,/:优先级高
        """
        operator_map = {'=': 0,'+': 2,'-': 2,'*': 3,'/': 3}

        if operator_map[operator] >= operator_map[cur_operator] :
            #栈顶操作符的优先级大于读入的操符号的优先级
            #这种情况下:从操作数栈中弹出两个操作数(left,right),从operator栈中弹出操作符theta,
            #形成运算指令:left theta right,结果如栈operand
            #将当前操作符入栈
            return '>'
        else :
            return '<'

    def is_invalid(self) :
        """
        验证用户输入的表达式的合法性,由于是不包括括号的四则运算,则只考虑数字和操作符交替出现
        """
        length = len(self.expression)
        if length == 0 :
            print "the length of the expression should > 0"
            return False
        else :
            after = True
            #after作为标记,当after=True的时候,表示下个只能出现数字;当after=False的时候,下一个可以是数字,也可以是操作符
            for index in xrange(length) :
                #主要检查数字,字符是否交替出现,并且以字符开始
                charactor = expression[index]
                if after is True :
                    if not self.is_operand(charactor) :
                        print "the expression you input is invalid"
                        return False
                    else :
                        after = False
                else :
                    if self.is_operand(charactor) :
                        after = False
                    elif self.is_operator(charactor) :
                        after = True
                    else :
                        print "the expression can only contains operator and operand."
                        return False
        return True

    def operate(self,left,theta,right) :
        """
        计算运算表达式 : left theta right
        """
        if theta =='+' :
            return left + right
        elif theta == '-' :
            return left - right
        elif theta == '*' :
            return left * right
        elif theta == '/' :
            return left / right

