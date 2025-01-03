import matplotlib as mltb
import matplotlib.contour
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

import numpy as np

import palmTree as pt

myTree = pt.palmTree()
x1, y1, half_lines1, half_lines2, spine_lines = myTree.createLeaf()

# print(spine_lines)

fig, ax = plt.subplots(figsize=(5, 5))

ax.plot(x1, y1, color = 'none')
line_collection1 = LineCollection(half_lines1, linewidths=1, color='green')
line_collection2 = LineCollection(half_lines2, linewidths=1, color='red')
line_collection3 = LineCollection(spine_lines, linewidths=1, color='blue')

# print(half_lines1)
ax.add_collection(line_collection1)
ax.add_collection(line_collection2)
ax.add_collection(line_collection3)

# ax.plot(x2, y2)
# ax.plot(x3, y3)
ax.set_aspect('equal')

plt.show()

# plt.show()