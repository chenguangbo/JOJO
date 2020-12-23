import numpy as np
import matplotlib.pyplot as plt

mu = 100
sigma = 2000
x = mu + sigma * np.random.randn(200)
plt.hist(x, bins=20)
plt.show()
