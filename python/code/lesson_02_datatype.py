#================================知识点==========================================
#1.变量
#2.基本数据类型：数字，字符串，元组，列表，字典，集合
#3.运算符

#================================================================================
#多个变量赋值
# a,b,c = 1,2,3
# print(a,b,c)
#
# d=e=f=100
# print(d,e,f)

#Number数字
#支持int,float,bool,complex
# a,b,c,d = 2, 1.2, False, 2+3j
# print(type(a),type(b),type(c),type(d))

#String字符串
#List列表
#Tuple元组
#Set集合
#Dictionary字典

#运算符
#运算符优先级
"""
运算符	描述
**	指数 (最高优先级)
~ + -	按位翻转, 一元加号和减号 (最后两个的方法名为 +@ 和 -@)
* / % //	乘，除，求余数和取整除
+ -	加法减法
>> <<	右移，左移运算符
&	位 'AND'
^ |	位运算符
<= < > >=	比较运算符
== !=	等于运算符
= %= /= //= -= += *= **=	赋值运算符
is is not	身份运算符
in not in	成员运算符
not and or	逻辑运算符
"""
#算术运算符
# a = 4
# b = 5
# print(
#     a+b,
#     a-b,
#     a/b,
#     a%b,
#     a**b,
#     a//b,
#     -a//b)

#python比较运算符
# a = 1
# b = 2
# print(
#     a == b,
#     a != b,
#     a > b,
#     a < b,
#     a >= b,
#     a <= b)

#python赋值运算符 :=海象运算符
# a = 1
# b = 2
# c = 0
# print(c)
# += -= *= /= %= **= //=
"""python3.8支持
if (n := len(a)) > 10:
    print(f"List is too long ({n} elements, expected <= 10)")
"""
#位运算符
# & | ^异或运算 ~ << >>

#逻辑运算
#and or not

#成员运算
#in not in

#身份运算
#is not is