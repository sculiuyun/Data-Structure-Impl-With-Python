#!/usr/bin/env python
# encoding: utf-8

"""
识别表达式中括号括号(,),[,],{,}是否配对出现.
算法思想:使用堆栈,从左到右一次扫描字符串expression:
    如果读入的字符为"(","[","{",则字符入栈.
    如果读入的是")","]","}",如果栈空,则不匹配;
        否则如果站顶的括号与之不匹配,则不匹配.
    如果读入的字符是其他字符,则继续读入.
    扫描完字符之后,如果堆栈为空,则表示匹配,否则左右括号不匹配.
"""
from stack_v2 import Stack

class Match(object) :
    "Match"
    def __init__(self,expression) :
        """
        init.
        """
        self.expression = expression

    def match(self) :
        """
        判断表达式中的括号是否配对出现.
        """
        stack = Stack()
        length = len(expression)
        for index in xrange(length) :
            temp = expression[index]
            if temp =='(' or temp =='[' or temp == '{' :
                #如果读入的字符是"(","[","{",则进栈
                stack.push(temp)
            elif temp == ')' :
                if stack.empty() :
                    return False
                elif '(' == stack.top() :
                    stack.pop()
                else :
                    return False
            elif temp == ']' :
                if stack.empty() :
                    return False
                elif '[' == stack.top() :
                    stack.pop()
                else :
                    return False
            elif temp == '}' :
                if stack.empty() :
                    return False
                elif '}' == stack.top() :
                    stack.pop()
                else :
                    return False
        if stack.empty() :
            return True
        else :
            return False




