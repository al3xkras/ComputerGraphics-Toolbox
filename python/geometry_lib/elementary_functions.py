"""@package docstring
Documentation for this module.

More details.
"""
from data_representation import Segment
from data_representation import Point

"""Documentation for this function.

More details.
"""
def IsIntersection(seg1:Segment, seg2:Segment):
    pass

"""Documentation for this function.

More details.
"""
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
        return 1
    elif value <= -thresh:
        return -1
    else:
        return 0

def CCW(p1:Point, p2:Point, p3:Point):
    value = (p2.y - p1.y) * (p3.x - p2.x) - (p2.x - p1.x) * (p3.y - p2.y)
    thresh = 1e-9
    return value <= -thresh

if __name__ == '__main__':
    pass