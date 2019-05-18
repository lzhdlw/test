# _*_ coding:utf-8 _*_


import requests

url = "https://www.baidu.com"
r = requests.get(url)

# if not r.status_code == 200:
#     print("Error! status_code: {0}".format(r.status_code))
#     exit()
#
# print(r.encoding)
# print(r.apparent_encoding)
# r.encoding = r.apparent_encoding
# print(r.headers)
# print(len(r.text))
# print(r.request.headers)
# print(r.text)
print("text:\n", r.text.encode("utf8"))
print("headers:\n", r.headers)
print("get:\n", r.headers.get("date"))
print(r.encoding)
print(r.apparent_encoding)
print("links:\n", r.links)
print(r.url)

keyword = "name"
count_of_keyword = r.text.count(keyword)
print(count_of_keyword)
index = 0
numlist = []
for i in range(count_of_keyword):
    index = r.text.find(keyword, index+1)
    numlist.append(index)

print(numlist)
print(r.)
