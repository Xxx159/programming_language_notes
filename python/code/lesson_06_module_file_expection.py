'''
#-----------------------------------模块-----------------------------------------------
#import
#from ... import     导入模块中的指定部分
#from ... import *  导入模块中的所有项目
# import sys
#
#
# print('命令行参数如下：')
# for i in sys.argv:
#     print(i)
#
# print('\n\nPython路径为：',sys.path,'\n')
#
# from os import environ
# from math import *
#
#
# print(environ)
# print(pi,e)
#
# if __name__ == '__main__':
#    print('程序自身在运行')
# else:
#    print('我来自另一模块')


#-----------------------------------包-----------------------------------------------
# import bag_b.bag.bag as t
# t.mypt(12345687856)
# t.welcome()

# import bag_b.bag.bag
# bag_b.bag.bag.welcome()

# from bag_b.bag.bag_a import myadd
# myadd(2,6)

# from bag_b.bag import *
# bag_a.myadd(12,14)
# bag.welcome()
'''


#-----------------------------------------------文件-------------------------------------
#open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
#file必须，文件路径（相对或绝对）   mode可选，文件打开模式    设置缓冲   一般UTF-8  报错级别  区分换行   传入的file参数类型
'''
#                              Opening Files
#                                     ||
#                                     ||
#                     reading         V             Reading and Writing
#                 ===================For?===================================
#                ||                   ||                                   ||
#                ||           Writing||                                    ||
#                V                   ||                                    ||
#                r                  ||                                     ||
#         初始位置：开始             ||                                      ||
#                                  ||                                       ||
#                                  V                                        V
#                  ============Truncate?============           ============Truncate?============
#                 ||     Yes                  No   ||         ||     Yes                  No   ||
#                 V                                V          V                                V
#                 w                               a           w+               ============Initial Position===========
#                                          开始位置：最后                       ||    Begein                       End||
#                                                                             V                                     V
#                                                                             r+                                   a+
#
# f = open('F:/xx_python_projects_library/pycharm_pro/bag_b/bag/file_test.txt','a')
# # f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )
# # f.write('hello this is a test for file')
# f.write('python is nohtyp')
# f.close()

# f1 = open('bag_b/bag/file_test1.txt','r')
# # x = f1.readline()
# x = f1.readlines()
# # x = f1.read()
# print(x)
# f1.close()

# f2 = open('bag_b/bag/file_test1.txt','r')
# for i in f2:
#     print(i)
f2 = open('bag_b/bag/file_test1.txt','r')
# print(f2.tell)
print(f2.seek(30))
print(f2.read(1))
f2.close()
'''

# import pickle
#
# # 使用pickle模块将数据对象保存到文件
# data1 = {'a': [1, 2.0, 3, 4+6j],
#          'b': ('string', u'Unicode string'),
#          'c': None}
#
# selfref_list = [1, 2, 3]
# selfref_list.append(selfref_list)
#
# output = open('bag_b/data.pkl', 'wb')
#
# # Pickle dictionary using protocol 0.
# pickle.dump(data1, output)
#
# # Pickle the list using the highest protocol available.
# pickle.dump(selfref_list, output, -1)
#
# output.close()
#
# #=============================
# import pprint, pickle
#
# #使用pickle模块从文件中重构python对象
# pkl_file = open('bag_b/data.pkl', 'rb')
#
# data1 = pickle.load(pkl_file)
# pprint.pprint(data1)
#
# data2 = pickle.load(pkl_file)
# pprint.pprint(data2)
#
# pkl_file.close()

#----------------------------------------------错误异常---------------------------------------
#异常捕获
#1.try/expect
# while True:
#     try:
#         x = int(input("请输入一个数字: "))
#         print(x)
#         break
#     except ValueError:
#         print("您输入的不是数字，请再次尝试输入！")
import sys

# try:
#     f = open('myfile.txt')
#     s = f.readline()
#     i = int(s.strip())
# except OSError as err:
#     print("OS error: {0}".format(err))
# except ValueError:
#     print("Could not convert data to an integer.")
# except:
#     print("Unexpected error:", sys.exc_info()[0])
#     raise

#2.try/except...else

# for arg in sys.argv[1:]:
#     try:
#         f = open(arg, 'r')
#     except IOError:
#         print('cannot open', arg)
#     else:
#         print(arg, 'has', len(f.readlines()), 'lines')
#         f.close()

#3.try/except...else...finally
# def hi():
#     print('hi,python!')
#
# try:
#     hi()
# except AssertionError as error:
#     print(error)
# else:
#     try:
#         with open('file.log') as file: #关键词 with 语句就可以保证诸如文件之类的对象在使用完之后一定会正确的执行他的清理方法:
#             read_data = file.read()
#     except FileNotFoundError as fnf_error:
#         print(fnf_error)
# finally:
#     print('这句话，无论异常是否发生都会执行。')


#抛出异常 raise [Exception [, args [, traceback]]]
#raise 唯一的一个参数指定了要被抛出的异常。它必须是一个异常的实例或者是异常的类（也就是 Exception 的子类）。
# x = 10
# if x > 5:
#     raise Exception('x 不能大于 5。x 的值为: {}'.format(x))
# try:
#     raise NameError('HiThere')
# except NameError:
#     print('An exception flew by!')
#     raise

#assert
'''
if not expression:
    raise AssertionError
等价于
assert expression
'''
# import sys
# assert ('linux'  in sys.platform), "改代码只能在 Linux 下执行"
assert True
assert False