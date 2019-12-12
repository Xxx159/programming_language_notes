#--------------------------------迭代器-----------------------------------------------
'''
迭代器是python最强大的功能之一，是访问集合元素的一种方式。
迭代器是一个可以记住遍历位置的对象。迭代器对象从集合的第一个元素开始访问，直到所有元素被访问完结束。
迭代器只能往前不会后退。
'''
#遍历/迭代
# for i in range(1,20):
#     print(i,end=' ')

#遍历迭代器
# list1 = [1,2,3,4,5,'hello']
# it2 = iter(list1)
# # print(next(it))
# for x in it2:
#     print('hi',x,end=" ")
#
# for x in it2 :
#     print ( x , end = ' ' )

# print('\n------------------------')
# next() 函数遍历迭代器
# while True :
#     try :
#         print ( next ( it2 ) )
#     except StopIteration :
#         break
# print('\n------------------------')

# import sys  # 引入 sys 模块
# list = [1, 2, 3, 4]
# it = iter(list)  # 创建迭代器对象
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit()

#创建一个迭代器
'''
把一个类作为一个迭代器使用需要在类中实现两个方法 __iter__() 与 __next__() 。
__iter__() 方法返回一个特殊的迭代器对象， 这个迭代器对象实现了 __next__() 方法并通过 StopIteration 异常标识迭代的完成。
__next__() 方法（Python 2 里是 next()）会返回下一个迭代器对象。
创建一个返回数字的迭代器，初始值为 1，逐步递增 1：
'''
#
# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self
#
#     def __next__(self):
#         if self.a <= 20:
#             x = self.a
#             self.a += 1
#             return x
#         else:
#             raise StopIteration
#
#
# myclass = MyNumbers()
# myiter = iter(myclass)
#
# for x in myiter:
#     print(x,end=' ')
#
# print('\n------------------')

#--------------------------------------------生成器-------------------------------------
#迭代器实现斐波那契数列
# class Fibonacci:
#     def __init__(self,n):
#         self.a = 0
#         self.b = 1
#         self.n = n
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.n > 0:
#             x = self.b
#             self.b += self.a
#             self.a = x
#             self.n -= 1
#             return x
#         else:
#             raise StopIteration

# f = Fibonacci(10)
# print([j for j in f])


#生成器实现斐波那契数列
import sys

def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
           return
        yield a
        a, b = b, a + b
        counter += 1

f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成

while True:
    try:
        print(next(f), end=" ")
        # print('hi')
    except StopIteration:
        sys.exit()

