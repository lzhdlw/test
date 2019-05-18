# _*_ coding:utf-8 _*_



value = 1
num = 1
while value > 0.3:
    value = pow(0.9, num)
    print(num,":", value)
    num += 1


value = 1
num = 1
while value < 3:
    value = pow(1.1, num)
    print(num,":", value)
    num += 1