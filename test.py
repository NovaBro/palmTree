import matplotlib.pyplot as plt
import numpy as np


x = np.arange(1, 11, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, x * 0)
plt.show()