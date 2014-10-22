#!/usr/bin/env python
# encoding: utf-8

#题目描述
"""
假设这有两个分别由字母组成的字符串A和字符串B,字符串B的字母数比字符串A少一些.
什么方法能快速地查找出B中的所有字母是不是都在字符串A中?也就是说,判断字符串B
是否是字符串A的真子集.为了简化,我们规定输入的字母只包含大写字母.
比如，如果是下面两个字符串：
String 1: ABCDEFGHLMNOPQRS
String 2: DCGSRQPO
答案是true，即String2里的字母在String1里也都有，或者说String2是String1的真子集。

如果是下面两个字符串：
String 1: ABCDEFGHLMNOPQRS
String 2: DCGSRQPZ
答案是false，因为字符串String2里的Z字母不在字符串String1里。
"""
#解法1:暴力轮询
#针对String2中的没一个字符,一一与string1中的每个字符依次轮询比较,看它是否在
#string1中.
def compare_1(string_one,string_two) :
    for item in string_two :
        if item in string_one :
            pass
        else :
            return False
    return True

#解法2:巧用hashtable
def compare_2(string_one,string_two) :
    #辅助数组
    hash_temp = [0]*26
    for char in string_one :
        index = ord(char) - ord('A')
        hash_temp[index] += 1
    for char in string_two :
        index = ord(char) - ord('A')
        if not hash_temp[index] :
            return False
    return True

#解法3:素数相乘
"""
    假设有一个仅由字母组成字串，让每个字母与一个素数对应，从2开始，往后类推，
A对应2，B对应3，C对应5，......。遍历第一个字串，把每个字母对应素数相乘。
最终会得到一个整数。
    利用上面字母和素数的对应关系，对应第二个字符串中的字母，然后轮询，
用每个字母对应的素数除前面得到的整数。如果结果有余数，说明结果为false。
如果整个过程中没有余数，则说明第二个字符串是第一个的子集了（判断是不是真子
集，可以比较两个字符串对应的素数乘积，若相等则不是真子集）。
思路总结如下：
1. 按照从小到大的顺序，用26个素数分别与字符'A'到'Z'一一对应。
2. 遍历长字符串，求得每个字符对应素数的乘积。
3. 遍历短字符串，判断乘积能否被短字符串中的字符对应的素数整除。
4. 输出结果。
"""
#此方法风险较大,会有溢出的危险
def compare_3(string_one,string_two) :
    prime_number = (2, 3, 5, 7,
                    11, 13, 17, 19,
                    23, 29, 31, 37,
                    41, 43, 47, 53,
                    59, 61, 67, 71,
                    73, 79, 83, 89,
                    97, 101)
    product = 1
    for char in string_one :
        index = ord(char) - ord('A')
        product *= prime_number[index]
    for char in string_two :
        index = ord(char) - ord('A')
        if product % prime_number[index] :
            return False
    return True

