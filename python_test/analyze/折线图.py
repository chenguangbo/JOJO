import numpy as np
import matplotlib.pyplot as plt

# arrange = np.arange(-10, 10, 1)
# print(arrange)
# plt.plot(arrange)
# plt.show(arrange)

x = np.linspace(-100, 100, 10000)
y = x ** 3
plt.plot(x, y)
plt.show()
