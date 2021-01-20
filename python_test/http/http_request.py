# coding=utf-8
import requests as req
import json
import urllib

url = "http://localhost:80/ironman/open/live/to_live"
kv = json.dumps({"wd": "你好百度", "q": "ww", 'type': '1', 'userId': '123','liveId':'534'})
# rep_get = req.post(url, params=kv)
# rep_get.encoding = "utf-8"
# print(rep_get.text)


session = req.session()
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'Content-Type': 'application/json', 'User-Agent': user_agent, 'appId': '80',
           'adminToken': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdHVJZCI6Ijg5IiwiZXhwIjoxNjExNzE0OTUyLCJ1c2VySWQiOiI4OSIsImlhdCI6MTYxMTExMDE1Mn0.pJpeGDC_bMHeNFdRRziG62KUX0ha1Y3H9vf8NkMaHV8'}
# headers = {'Content-Type': 'application/json'}
result = session.post(url, data=kv, headers=headers)

print(result)
print(result.content.decode())
