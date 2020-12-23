import numpy as np
import matplotlib.pyplot as plt

N = 5
y = [1,-5, 7, 10, 9]
index = np.arange(N)
pl = plt.bar(x=index, height=y, align='center',color='blue')
plt.show()
