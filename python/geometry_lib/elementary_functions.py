"""@package docstring
Documentation for this module.

More details.
"""
from data_representation import Segment
from data_representation import Point,Side

"""Documentation for this function.

More details.
"""
def IsIntersection(seg1:Segment, seg2:Segment):
    pass

"""Documentation for this function.

More details.
"""

def Orientation(A:Point, B:Point, P:Point):
	return (B.x-A.x)*(P.y-A.y)-(P.x-A.x)*(B.y-A.y)

def Intersection(seg1:Segment, seg2:Segment):
    pass

"""Documentation for this function.

More details.
"""
def WhichSide(seg:Segment, point:Point):
    aX = seg.A.x
    aY = seg.A.y
    bX = seg.B.x
    bY = seg.B.y
    cX = point.x
    cY = point.y
    value=(bX - aX)*(cY - aY) - (bY - aY)*(cX - aX)
    thresh = 1e-9
    if value >= thresh:
        return Side.LEFT
    elif value <= -thresh:
        return Side.RIGHT
    else:
        return Side.NONE

def CCW(p1:Point, p2:Point, p3:Point):
    value = (p2.y - p1.y) * (p3.x - p2.x) - (p2.x - p1.x) * (p3.y - p2.y)
    thresh = 1e-9
    return value <= -thresh

if __name__ == '__main__':
    pass


