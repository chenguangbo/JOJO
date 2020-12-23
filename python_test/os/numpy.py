import numpy as np
import matplotlib.pyplot as plt

# text = np.loadtxt('test.txt')
# print(text)

c = np.arange(10)
print(c)
# print(c + c)

a = c.reshape(5, 2)

print(a)
ey = np.eye(4, 4, 0)
print(ey)
print(np.linspace(1, 10, 5))  # 开始 结束 个数

print('----------------------------------------')

x = np.linspace(0, 10, 5)
y = np.linspace(0, 10, 5)
xv, yv = np.meshgrid(x, y)
# print(xv)
# print(yv)
# plt.plot(xv, yv, '^')
plt.plot(xv, yv, '*')
plt.show()
