import pymysql

db = pymysql.connect("127.0.0.1", "root", "root", "mysql", charset='utf8')
sql = "select user ,host from user;"
# 使用cursor()方法获取操作游标
cursor = db.cursor()
# 使用execute方法执行SQL语句
cursor.execute(sql)
result = cursor.fetchall()

# for q1 in result():
#     print(q1)

import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()

import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.axis([0, 6, 0, 20])
plt.show()

import numpy as np
import matplotlib.pyplot as plt


def f(t):
    return np.exp(-t) * np.cos(2 * np.pi * t)


t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure(1)
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(212)
plt.plot(t2, np.cos(2 * np.pi * t2), 'r--')
plt.show()

#     pylab.plot_date(q1[0], q1[1], 'o')
# # dates1 = [q1[0],for q1 in result]
# # num1 = [q1[1] for q1 in result]
# # pylab.plot_date(dates1,num1,'o')
# pylab.show()
