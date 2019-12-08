#================================知识点==========================================
#1.变量
#2.基本数据类型：数字，字符串，元组，列表，字典，集合
#3.运算符
#特色
"""
推导式comprehensions（又称解析式），是Python的一种独有特性。
推导式是可以从一个数据序列构建另一个新的数据序列的结构体。 共有三种推导，在Python2和3中都有支持：
列表(list)推导式
字典(dict)推导式
集合(set)推导式
"""

#==================================多个变量赋值========================================
# a,b,c = 1,2,3
# print(a,b,c)
#
# d=e=f=100
# print(d,e,f)


#=========================================Number数字=======================================
"""
#支持int,float,bool,complex
# a,b,c,d = 2, 1.2, False, 2+3j
# print(type(a),type(b),type(c),type(d))

#数字类型转换
# a = 1.1
# print(int(a))
#数字运算 + - * / //  % **
#数学函数
# print(abs(-4))
#import math
# print(math.ceil(3.4))
#随机函数
# import random
# print(random.choice(range(100)))
#数学常量
#print(math.pi,math.e)
#三角函数
#print(math.cos(math.pi/2))
"""

#=========================================String字符串=====================================
#字符串用'或"来创建
str1 = 'I am a string'
str2 = "python ii nohtyp!"
#字符串的访问：索引
#print(str1[0],str2[3:8],str1[1:6:2])
#字符串的增(复制，连接)删改(替换，截取，分割)查
# print(str1.find('ing',3,len(str1)))
# print(str1.rfind('a',1,len(str1)))
# #print(str2.index('qq',3,len(str1)))
# print(str2.rindex('o',1,len(str1)))
# print(str1.count('a'))
# print(str2.replace('o','ooooo*ooooo',3))
# print(str2.split(" ",1))
#isalpha,isdigit,isalnum,isspace
#captalize,title,startswith,endswith,lower,upper,ljust,rjust,center,lstrip,rstrip,strip,join
#转义字符使用反斜杠转义 记住撇捺 正斜杠/  反斜杠\
# 转义字符	描述
# \(在行尾时)	续行符
# \\	反斜杠符号
# \'	单引号
# \"	双引号
# \a	响铃
# \b	退格(Backspace)
# \000	空
# \n	换行
# \v	纵向制表符
# \t	横向制表符
# \r	回车
# \f	换页
# \oyy	八进制数，yy 代表的字符 例如：\o12 代表换行，其中 o 是字母，不是数字 0
# \xyy	十六进制数，yy代表的字符 例如：\x0a代表换行
# \other	其它的字符以普通格式输出

#字符串运算
print(
    str1+str2,
    str1*2,
    str1[2],
    str1[3:6],
    'o' in str1,
    'a' not in str1,
    r'\n',
    R'\n'
)
#字符串格式化输出
print ("我叫 %s 今年 %d 岁!" % ('小明', 10))


"""
  符   号	描述
      %c	 格式化字符及其ASCII码
      %s	 格式化字符串
      %d	 格式化整数
      %u	 格式化无符号整型
      %o	 格式化无符号八进制数
      %x	 格式化无符号十六进制数
      %X	 格式化无符号十六进制数（大写）
      %f	 格式化浮点数字，可指定小数点后的精度
      %e	 用科学计数法格式化浮点数
      %E	 作用同%e，用科学计数法格式化浮点数
      %g	 %f和%e的简写
      %G	 %f 和 %E 的简写
      %p	 用十六进制数格式化变量的地址
    格式化操作符辅助指令:

符号	功能
*	定义宽度或者小数点精度
-	用做左对齐
+	在正数前面显示加号( + )
<sp>	在正数前面显示空格
#	在八进制数前面显示零('0')，在十六进制前面显示'0x'或者'0X'(取决于用的是'x'还是'X')
0	显示的数字前面填充'0'而不是默认的空格
%	'%%'输出一个单一的'%'
(var)	映射变量(字典参数)
m.n.	m 是显示的最小总宽度,n 是小数点后的位数(如果可用的话)
f-string
f-string 是 python3.6 之后版本添加的，称之为字面量格式化字符串，是新的格式化字符串的语法。
之前我们习惯用百分号 (%):
"""
"""
str3 = "我就测试一下f-string"
print(f'hello {str3}')

x = 1
print(f'{x+1}')   # Python 3.6 输出结果2

#x = 3
#print(f'{x+1=}')   # Python 3.8 输出结果'x+1=4'

#字符编码 Unicode ASCii
"""

#=========================================List列表==========================================
'''
# list1 = ['hello','python',2019,2020]
# list2 = [1,2,3,4,5,6,7,8,9]
# print(
#     list1[0],
#     list2[3:5]
# )
# list2[0] = 'first'
# print(list2)
# del list2[5]
# print(list2)
# print(
#     len(list2),
#     list1 + list2,
#     list1 *4,
#     4 in list2,
# )
for q in [10,11,12]:
    print(q)
list3 = [[1,2,3],[4,5,6],7]
print(list3[1][0])

#list的方法
#list3.fuc()增删改查
'''


#=========================================Tuple元组=========================================
"""
#元组中的元素值是不允许修改
tuple1 = (1,2,3,4,5)
tuple2 = (1,)
tuple3 = (1)
tuple4 = 1,2,3,'a','b'
print(type(tuple2),type(tuple3),type(tuple4))
print(tuple1[0],tuple1[1:2])
print(tuple1+tuple2)
#元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组
# print(tuple2)
# del tuple2
# print(tuple2)
print(
    len(tuple1),
    tuple2+tuple4,
    ('hi')*2,
    2 in tuple1,
    [i for i in tuple1]
)
#tuple1.fuc()
"""

#=========================================Set集合===========================================


#=========================================Dictionary字典=====================================


#===================================运算符===================================================
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
'''python3.8支持
if (n := len(a)) > 10:
    print(f"List is too long ({n} elements, expected <= 10)")
'''
#位运算符
# & | ^异或运算 ~ << >>

#逻辑运算
#and or not

#成员运算
#in not in

#身份运算
# is,not is
"""

#----------------------------------------列表推导式，字典推导式，集合推导式--------------
"""
#1、使用[]生成list
#基本格式：[表达式 for 变量 in 列表]    或者  [表达式 for 变量 in 列表 if 条件]
#求(x,y)其中x是0-5之间的偶数，y是0-5之间的奇数组成的元祖列表
res1=[(x, y) for x in range(5) if x % 2 == 0 for y in range(5) if y % 2 == 1]
print(res1)
#2、使用()生成generator
res2 = (i for i in range(30) if i % 3 is 0)
print(res2)

#字典推导式
#大小写key合并
mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
mcase_frequency = {
    k.lower(): mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0)
    for k in mcase.keys()
    if k.lower() in ['a','b']
}
print(mcase_frequency)
#快速跟换key和value
res4 = {u:v for v,u in mcase.items()}
print(res4)

#集合推导式
squared = {x**2 for x in [1, 1, 2]}
print(squared)
"""