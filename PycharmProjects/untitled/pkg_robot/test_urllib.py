# _*_ coding:utf-8 _*_


from urllib import request, parse


url = "http://www.baidu.com"
r = request.urlopen(url)
if r.status == 200:
    print(dir(r))
    print("code:", r.code)
    print("begin:", r.begin())
    print("getcode:", r.getcode())
    print("geturl:", r.geturl())
    print("length:", r.length)
    print("status:", r.status)
    print("getheaders:", r.getheaders())

