import matplotlib as mltb
import matplotlib.contour
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

import numpy as np


palmCenter = 1
numFronds = 5


# =====
# Leaf Spine
# =====
leaf_length = 11
resolution = 0.01
leafCurve = 10

x1 = np.arange(palmCenter, leaf_length, resolution)
y1 = np.log10(x1) * leafCurve

y1 = x1
z = 1

# z = 1/(x1 * np.log(10)) * leafCurve
z = -1 * np.reciprocal(z)

# y1 = np.sin(x1)
# z = np.cos(x1)
# z = -1 * np.reciprocal(z)

# =====
# Leaf Length
# =====
theta = np.arctan(z)
# print(theta)
axis1 = np.sin(theta)
axis2 = np.cos(theta)

# === Shape of lower half ===
width = np.arange(-(leaf_length - 1)/2, (leaf_length - 1)/2, resolution)
width = width * width * -0.125 + 4
x2 = axis2 * width + x1
y2 = axis1 * width + y1

# === Shape of higher half ===
width = np.arange(-(leaf_length - 1)/2, (leaf_length - 1)/2, resolution)
width = width * width * 0.125 - 4
x3 = axis2 * width + x1
y3 = axis1 * width + y1


# ====
# Create Leaves
# ====
numLeavesPerSpine = 30
current_numLeavesPerSpine = (leaf_length - palmCenter)/resolution
everyOther = int(current_numLeavesPerSpine/numLeavesPerSpine)

def makePointPairs(x, y, other):
    
    numPoints = int(len(x) / other)
    newPairs = np.empty([numPoints, 2])
    for i in range(numPoints):
        newPairs[i, 0] = x[i * other]
        newPairs[i, 1] = y[i * other]
    return newPairs

points1 = makePointPairs(x1, y1, other=everyOther)
points2 = makePointPairs(x2, y2, other=everyOther)
points3 = makePointPairs(x3, y3, other=everyOther)

points1 = points1[:, np.newaxis, :]
points2 = points2[:, np.newaxis, :]
points3 = points3[:, np.newaxis, :]
half_lines1 = np.append(points1, points2, axis=1)
half_lines2 = np.append(points1, points3, axis=1)

# ====
# Plot Picture

# ====

fig, ax = plt.subplots(figsize=(5, 5))
# ax.set_xlim(0, 15)
# ax.set_ylim(-3, 15)
# ax.set_aspect("equal")  # to make the arcs look circular

line_collection1 = LineCollection(half_lines1, linewidths=1, color='green')
line_collection2 = LineCollection(half_lines2, linewidths=1, color='green')
ax.add_collection(line_collection1)
ax.add_collection(line_collection2)
ax.plot(x1, y1)
ax.plot(x2, y2)
ax.plot(x3, y3)
ax.set_aspect('equal')

plt.show()

# plt.show()