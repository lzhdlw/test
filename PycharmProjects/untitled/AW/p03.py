# _*_ coding:utf-8 _*_

"""
题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
"""

num_1 = 1
flag = False
while True:
    for num_2 in range(1, num_1):
        if num_1**2 - 268 == num_2**2 - 100:
            print("num_1:{0}\nnum_2:{1}".format(num_1, num_2))
            print("Result:", num_2**2 - 100)
            flag = True
            break
    if not flag:
        num_1 += 1
    else:
        break

print("*" * 20)
# Answer2:
import math
num = 1
while True:
    x = int(math.sqrt(num + 100))
    y = int(math.sqrt(num + 100 + 168))

    if (num + 100 == x**2) and (num + 100 + 168 == y**2):
        print("num:", num)
        break
    else:
        num += 1

print("*" * 20)

# Answer3:
for i in range(10000):
    # 转化为整型值
    x = int(math.sqrt(i + 100))
    y = int(math.sqrt(i + 268))
    if(x * x == i + 100) and (y * y == i + 268):
        print (i)
        break
