import pymysql
import numpy as np
import json

import os

path = 'C:\\clazz_student_202012181933.sql'
# sl = open(path, 'rt')
# print(sl)
# print(sl.read())
#
#
# print(sl.read())
#
# listdir = os.listdir(path)
# filepath = os.getcwd()
# allfile = []
# for file in listdir:
#     allfile.append(filepath + '\\' + file)
# print(allfile)

db = pymysql.connect("127.0.0.1", "ironman", "123456", "123456", charset='utf8')
cursor = db.cursor()


def insert(sql):
    # 使用cursor()方法获取操作游标
    # 使用execute方法执行SQL语句
    try:
        print(sql)
        cursor.execute(sql)
        db.commit()
        print("执行成功: " + sql)
    except Exception as e:
        print(e)


def ins():
    with open(path, encoding='utf-8', mode='r') as f:
        # 读取整个sql文件，以分号切割。[:-1]删除最后一个元素，也就是空字符串
        sql_list = f.read().split(';')[:-1]
        i = 0
        for x in sql_list:
            # 判断包含空行的
            if '\n' in x:
                # 替换空行为1个空格
                x = x.replace('\n', ' ')
            i += 1;
            # if i > 273234:
            # sql语句添加分号结尾
            sql_item = x + ';'
            insert(sql_item)


ins()
