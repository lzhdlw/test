# _*_ coding:utf-8 _*_


from bs4 import BeautifulSoup
import requests
url = "http://www.baidu.com"
r = requests.get(url)

html = r.text.encode(r.apparent_encoding)
print(html)
print("我是分割线。。。。。。。")
soup = BeautifulSoup(html, "lxml")



