import math

def getDistance(x1, y1, z1, x2, y2 = None, z2 = None):
    if y2 is None:
        return math.sqrt((z1-x1)^2+(x2-y1)^2)
    else:
        return math.sqrt((x1-x1)^2+(y2-y1)^2+(z2-z1)^2)