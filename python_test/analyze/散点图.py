import numpy as np
import matplotlib.pyplot as plt

N = 1000
x = np.random.random(N)
y = x + np.random.random(N) * 0.3
plt.scatter(x, y, s=10, c='r', marker='.', alpha=0.5)
plt.show()
