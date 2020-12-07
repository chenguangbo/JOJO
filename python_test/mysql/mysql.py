#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time

import numpy as np
import pymysql

db = pymysql.connect("127.0.0.1", "root", "123456", "mysql", charset='utf8')
sql = "select * from user;"
# 使用cursor()方法获取操作游标
cursor = db.cursor()
# 使用execute方法执行SQL语句
cursor.execute(sql)
result = cursor.fetchall()
print(result)
data = np.array(result)
list1 = data.tolist()
for i in range(0, len(list1)):
    # time.sleep(1)
    print(list1[i])

print("123")
