# _*_ coding:utf-8 _*_


import os

devices = os.popen("adb devices").read()
print(devices)
print(devices[1])


