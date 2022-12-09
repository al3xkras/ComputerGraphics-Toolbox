"""@package docstring
Documentation for this module.

More details.
"""
from data_representation import Segment
from data_representation import Point,Side

"""Documentation for this function.

More details.
"""
def VectorProduct(A:Point, B:Point, C:Point, D:Point):
	return (B.x - A.x)(D.y - C.y) - (D.x - C.x)(B.y - A.y)

def IsIntersection(seg1:Segment, seg2:Segment):
	if ((seg1.A == seg1.B) and (seg2.A == seg2.B)):
		if seg1.A == seg2.A:
			return True
		else:
			return False
	elif seg1.A == seg1.B:
		if IfPointIsOnSegment(seg2.A, seg2.B, seg1.A):
			return True
		else:
			return False
	elif seg2.A == seg2.B:
		if IfPointIsOnSegment(seg1.A, seg1.B, seg2.A):
			return True
		else:
			return False
	else:
		vecprod1 = VectorProduct(seg1.A, seg1.B, seg2.A, seg2.B)
		vecprod2 = VectorProduct(seg1.A, seg2.A, seg2.A, seg2.B)
		if vecprod1 == 0 and vecprod2 == 0:
			return True
		elif vecprod1 == 0:
			return False
		else:
			t = vecprod2/vecprod1
			vecprod3 = VectorProduct(seg1.A, seg2.A, seg1.A, seg1.B)
			u = vecprod3/vecprod1
			if t >= 0 and t <= 1 and u <= 1 and u >= 0:
				return True
			else:
				return False


"""Documentation for this function.

More details.
"""

def Orientation(A:Point, B:Point, P:Point):
	return (B.x-A.x)*(P.y-A.y)-(P.x-A.x)*(B.y-A.y)

def BoundingBox(A:Point, B:Point, P:Point):
    if (P.x >= A.x and P.x <= B.x) and (P.y >= A.y and P.y <= B.y):
        return True
    else:
        return False

def IfPointIsOnSegment(A:Point, B:Point, P:Point):
    if BoundingBox(A, B, P) == False:
        return False
    elif Orientation(A, B, P) == 0:
        return True
    else:
        return False


def Intersection(seg1:Segment, seg2:Segment):
    if ((seg1.A == seg1.B) and (seg2.A == seg2.B)):
		if seg1.A == seg2.A:
			return seg1.A
		else:
			return None
	elif seg1.A == seg1.B:
		if IfPointIsOnSegment(seg2.A, seg2.B, seg1.A):
			return seg1.A
		else:
			return None
	elif seg2.A == seg2.B:
		if IfPointIsOnSegment(seg1.A, seg1.B, seg2.A):
			return seg2.A
		else:
			return None
	else:
		vecprod1 = VectorProduct(seg1.A, seg1.B, seg2.A, seg2.B)
		vecprod2 = VectorProduct(seg1.A, seg2.A, seg2.A, seg2.B)
		if vecprod1 == 0 and vecprod2 == 0:
			return infinity
		elif vecprod1 == 0:
			return None
		else:
			t = vecprod2/vecprod1
			vecprod3 = VectorProduct(seg1.A, seg2.A, seg1.A, seg1.B)
			u = vecprod3/vecprod1
			if t >= 0 and t <= 1 and u <= 1 and u >= 0:
				return seg1.A + t*(seg1.B - seg1.A)
			else:
				return None
	

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


