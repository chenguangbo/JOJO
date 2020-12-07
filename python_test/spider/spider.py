#!/usr/bin/python
# -*- coding: UTF-8 -*-


import requests
import bs4
from bs4 import BeautifulSoup
import pprint
import json
import pymysql
import numpy as np


def download(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("获取出错")
    return response.text


# html = download("http://www.cscaa.org.cn/")
# html = download("http://www.people.com.cn/")
# html = download("http://www.youth.cn/")
html = download("https://www.huya.com/l")
html = download("https://www.douyu.com/directory/all")

print(html)


def parse_single_html(html):
    soup = BeautifulSoup(html, "html.parser")
    al = soup.find_all("a")
    links = []
    """
    @:return list({"title","link"})
    """
    for aa in al:
        # node = aa.find("href")

        text = aa.get_text()
        # print(aa)
        # print(text,aa.get_text("href"))
        link = ""

        if aa.get_text("href") != "":
            # print("==============="+aa.get_text("href"))
            try:
                link = str(aa["href"])
            except Exception:
                print(aa.get_text("href"))
        if link == '/':
            continue
        data = {"title": text, "link": link}
        # print(data)
        links.append(data)
    return links


result = parse_single_html(html)

json_text = json.dumps(result, ensure_ascii=False, indent=2)
with open("json.text", "w", encoding='utf-8') as json_w:
    json_w.write(json_text)


def get_connection():
    db = pymysql.connect("123", "root", "123", "mysql", charset='utf8')
    sql = "select * from user;"
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    return cursor


print(json_text)

# cursor = get_connection()


data = np.array(json_text)
list1 = data.tolist()

s = json.loads('{"name":"test", "type":{"name":"seq", "parameter":["1", "2"]}}')

# print(json_text['title'])
#
# print(list1)
j = json.loads(json_text)

print(j)


#

def mysql_insert():
    db = pymysql.connect("127.0.0.1", "root", "123456", "side", charset='utf8')
    cursor = db.cursor()
    sql = "insert into spider (title,link)values(%s,%s)"
    for i in range(0, len(j)):
        param = []
        # print(j[i]['title'], j[i]['link'])
        param.append((j[i]['title'], j[i]['link']))
        # cursor.executemany(sql, param)
        print(param)
        val = ((j[i]['title'], j[i]['link']))
        cursor.execute(sql, val)
        # cursor.execute(sql, param)
        db.commit()
    db.close()


def mysql_insert2():
    db = pymysql.connect("127.0.0.1", "root", "", "side", charset='utf8')
    cursor = db.cursor()
    sql = "insert into spider_2 (title,link)values(%s,%s)"
    param = []
    for i in range(0, len(j)):
        param.append((j[i]['title'], j[i]['link']))

    print(param)
    cursor.executemany(sql, param)
    db.commit()
    db.close()


mysql_insert2()

#     # time.sleep(1)
#     # print("i ===== "+i)
#     print("++++++++++++++++")
#     print(i["name"])
# values = (list1[i][0],list1[i][1])
