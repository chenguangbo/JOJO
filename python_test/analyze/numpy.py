import numpy as np

rand = np.random.randint(1, 100, 10)
print(rand)

print(rand.max())
print(rand.min())
print(np.max(rand))
print(np.min(rand))

print(rand[3::3])

# 第一个冒号是从哪个位置开始  第二个冒号是 步长
print(rand[::-1])

