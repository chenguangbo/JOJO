# coding=utf-8
import requests as req

url = "https://www.baidu.com"
kv = {"wd": "你好百度",  "q": "ww"}
rep_get = req.get(url, params=kv)
rep_get.encoding = "utf-8"
print(rep_get.text)

# resp = req.get("https://www.baidu.com")
# print(resp.text)
