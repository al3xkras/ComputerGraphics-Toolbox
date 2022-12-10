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
def orientation(ax,ay,bx,by,cx,cy):
    # todo test
    return (bx-ax)*(cy-ay)-(cx-ax)*(by-ay)

def Orientation(A:Point, B:Point, P:Point):
    return orientation(A.x,A.y,B.x,B.y,P.x,P.y)

def BoundingBox(A:Point, B:Point, P:Point):
    # todo test
    return (P.x >= A.x and P.x <= B.x) and (P.y >= A.y and P.y <= B.y)

def IfPointIsOnSegment(A:Point, B:Point, P:Point):
    # todo test
    if not BoundingBox(A, B, P):
        return False
    elif Orientation(A, B, P) == 0:
        return True
    return False


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
    value=orientation(aX,aY,bX,bY,cX,cY)
    thresh = 1e-9
    if value >= thresh:
        return Side.LEFT
    elif value <= -thresh:
        return Side.RIGHT
    return Side.NONE

def CCW(p1:Point, p2:Point, p3:Point):
    value = Orientation(p1,p2,p3)
    thresh = 1e-9
    return value <= -thresh

if __name__ == '__main__':
    pass


