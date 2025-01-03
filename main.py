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

myTree.createHead()
line_Collections = [None] * myTree.numFronds

for i in range(myTree.numFronds):
    
    frondSet0 = LineCollection(myTree.spines[i], linewidths=1, color='purple')
    frondSet1 = LineCollection(myTree.leaves[i, 0], linewidths=1, color='orange')
    frondSet2 = LineCollection(myTree.leaves[i, 1], linewidths=1, color='purple')

    ax.add_collection(frondSet0)
    ax.add_collection(frondSet1)
    ax.add_collection(frondSet2)



# line_collection1 = LineCollection(half_lines1, linewidths=1, color='green')
# line_collection2 = LineCollection(half_lines2, linewidths=1, color='red')
# line_collection3 = LineCollection(spine_lines, linewidths=1, color='blue')

# ax.add_collection(line_collection1)
# ax.add_collection(line_collection2)
# ax.add_collection(line_collection3)


ax.set_aspect('equal')
plt.show()

# plt.show()