import urllib

d = dir(urllib)
print(d)
# result = urllib3.response("https:www.baidu.com")
# print(result)

d.urlopen("aa")
result2 = urllib.urlopen("http//:www.baidu.com").read()
print(result2)