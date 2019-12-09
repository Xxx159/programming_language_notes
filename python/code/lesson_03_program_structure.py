#================================知识点==========================================
#顺序，选择（条件分支），循环
#嵌套
#break continue
#三元操作符
#-------------------------------------------------------------------------------


#------------------------------条件语句------------------------------------------
'''
分段函数求值

        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)
"""
import time

x = float(input('x = '))
start1 = time.clock()#time.time()
if x > 1:
    y = 3 * x - 5
else:
    if x >= -1:
        y = x + 2
    else:
        y = 5 * x + 3
print('f(%.2f) = %.2f' % (x, y))
end1 = time.clock()#time.time()
print(end1-start1)

#Flat is better than nested.

x = float(input('x = '))
start2 = time.time()
if x > 1:
    y = 3 * x - 5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3
print('f(%.2f) = %.2f' % (x, y))
end2 = time.time()
print(end2-start2)
'''

#------------------------------循环语句------------------------------------------
''' 
n = 100
i = 0
sum = 0
while i <= n:
    #sum = sum + i
    sum += i
    i += 1
print('1到100的总和:%d',sum)

# import time
# #无限循环CTRL+C结束
# while True:
#     print('死循环，CTRL+C结束')
#     time.sleep(2)

j = 0
while j < 3:
    print('测试')
    j += 1
else:
    print('大于等于3')

#break 语句可以跳出 for 和 while 的循环体。如果你从 for 或 while 循环中终止，任何对应的循环 else 块将不执行。
#continue 语句被用来告诉 Python 跳过当前循环块中的剩余语句，然后继续进行下一轮循环。
list1 = [1,2,3,4,5]
for i in list1:
    if i==3:
        print('遇到三')
        #break
        #continue
    print('循环总数',list1)
else:
    print('没有循环数据了')
print('循环结束')
pass #不做任何事情，一般用做占位语句
'''

#------------------------------三元操作符------------------------------------------
'''
a = 1
b = 2
print('为真时的结果：正确')if a > b else print('为假时的结果：错误')
'''