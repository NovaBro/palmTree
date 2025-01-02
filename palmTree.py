import numpy as np




class palmTree():
    def __init__(self):
        self.numFronds = 5
        self.numLeavesPerSpine = 100

        self.palmCenter = 1
        self.leaf_length = 11
        self.resolution = 0.01

        self.leaf_end_x = 10
        self.leafCurve = 4

        self.spines = np.empty([self.numFronds, int((self.leaf_length - self.palmCenter) / self.resolution)])

        self.leaves = np.empty([self.numFronds, 2, self.numLeavesPerSpine])



    def createHead(self):
        for i in self.numFronds():
            x1, y1, half_lines1, half_lines2, points1 = self.createLeaf()
            # self.spines[i] = 

        pass

    def createLeaf(self, ):
        # =====
        # Leaf Spine
        # =====
        x1 = np.arange(self.palmCenter, self.leaf_length, self.resolution)
        y1 = np.log10(x1) * self.leaf_end_x

        # y1 = x1
        # z = 1
        # y1 = 1 / x1
        # z = -1 / (x1) ** 2


        z = 1/(x1 * np.log(10)) * self.leafCurve
        z = -1 * np.reciprocal(z) 
        
        
        def myAngle(degree):
            return (np.pi / 180) * degree

        # =====
        # Leaf Length
        # =====
        # NOTE: we want to create leaves at an angle to the stem.
        # May change this to be at different angles other than 90 degrees
        theta = np.arctan(z)

        intersect = int(3.5 / 3.25)
        numPoints = int(((self.leaf_length - self.palmCenter) / self.resolution) * intersect / (self.leaf_length - self.palmCenter)) + 1

        leafAngle = myAngle(45)

        # ====
        # Half 1
        # ====
        
        # === Shape of lower half : Half 1 ===
        width = np.arange(0, self.leaf_length - self.palmCenter, self.resolution)

        print('numpoints', numPoints)
        
        width[numPoints:] = width[numPoints:] * -0.25 + 3.5
        width[:numPoints] = (width[:numPoints]) * 3

        # === Adjust Leaf Angle Half 1===
        axis1 = np.sin(theta + leafAngle)
        axis2 = np.cos(theta + leafAngle)

        x2 = axis2 * width + x1
        y2 = axis1 * width + y1

        # ====
        # Half 2
        # ====

        # === Shape of higher half : Half 2 ===
        width = np.arange(0, self.leaf_length - self.palmCenter, self.resolution)

        width[numPoints:] = width[numPoints:] * 0.25 - 3.5
        width[:numPoints] = (width[:numPoints]) * -3

        # === Adjust Leaf Angle Half 2===
        axis1 = np.sin(theta - leafAngle)
        axis2 = np.cos(theta - leafAngle)

        x3 = axis2 * width + x1
        y3 = axis1 * width + y1


        # ====
        # Create Leaves
        # ====
        
        current_numLeavesPerSpine = (self.leaf_length - self.palmCenter)/self.resolution
        everyOther = int(current_numLeavesPerSpine/self.numLeavesPerSpine)

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

        spine_lines = makePointPairs(x1, y1, other=everyOther)
        points2 = makePointPairs(x2, y2, other=everyOther)
        points3 = makePointPairs(x3, y3, other=everyOther)

        spine_lines = spine_lines[:, np.newaxis, :]
        points2 = points2[:, np.newaxis, :]
        points3 = points3[:, np.newaxis, :]
        half_lines1 = np.append(spine_lines, points2, axis=1)
        half_lines2 = np.append(spine_lines, points3, axis=1)
        
        spine_lines = np.append(spine_lines[:-1], spine_lines[1:], axis=1)

        return x1, y1, half_lines1, half_lines2, spine_lines



