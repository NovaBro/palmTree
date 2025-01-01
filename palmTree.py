import numpy as np




class palmTree():
    def __init__(self):
        self.numFronds = 5

        self.palmCenter = 1
        self.leaf_length = 11
        self.resolution = 0.01

        self.leafCurve = 10

        pass

    def createHead():
        
        pass

    def createLeaf(self, ):
        # =====
        # Leaf Spine
        # =====

        x1 = np.arange(self.palmCenter, self.leaf_length, self.resolution)
        y1 = np.log10(x1) * self.leafCurve

        y1 = x1
        z = 1

        # z = 1/(x1 * np.log(10)) * leafCurve
        z = -1 * np.reciprocal(z)

        # =====
        # Leaf Length
        # =====
        # NOTE: we want to create leaves at an angle to the stem.
        # May change this to be at different angles other than 90 degrees
        theta = np.arctan(z)
        axis1 = np.sin(theta)
        axis2 = np.cos(theta)

        # === Shape of lower half ===
        width = np.arange(-(self.leaf_length - 1)/2, (self.leaf_length - 1)/2, self.resolution)
        width = width * width * -0.125 + 4
        x2 = axis2 * width + x1
        y2 = axis1 * width + y1

        # === Shape of higher half ===
        width = np.arange(-(self.leaf_length - 1)/2, (self.leaf_length - 1)/2, self.resolution)
        width = width * width * 0.125 - 4
        x3 = axis2 * width + x1
        y3 = axis1 * width + y1


        # ====
        # Create Leaves
        # ====
        numLeavesPerSpine = 30
        current_numLeavesPerSpine = (self.leaf_length - self.palmCenter)/self.resolution
        everyOther = int(current_numLeavesPerSpine/numLeavesPerSpine)

        def makePointPairs(x, y, other):
            """
            This is meant to be for converting [x1, x2, x3, ...] and [y1, y2, y3, ...] to [[x1, y1], [x2, y2], [x3, y3], ...]
            """
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
        
        return x1, y1, half_lines1, half_lines2



