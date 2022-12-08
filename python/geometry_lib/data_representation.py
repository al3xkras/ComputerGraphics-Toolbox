"""@package docstring
Documentation for this module.

More details.
"""

"""Documentation for this class.

More details.
"""
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getPoint(self):
        return self.x, self.y

    def setPoint_x(self, new_value):
        self.x = new_value

    def setPoint_y(self, new_value):
        self.y = new_value

    def __str__(self) -> str:
        return "Point["+str(self.x)+" "+str(self.y)+"]"


#enum Side
class Side:
    LEFT = -1
    RIGHT = 1
    NONE = 0

class Color:
    NONE = 0
    BLUE = 1
    RED = 2
    GREEN = 3
    pass


"""Documentation for this class.

More details.
"""
class Segment:
    def __init__(self, A:Point, B:Point):
        self.A = A
        self.B = B

    def get_side(self, Point) -> int:
        return self.A
        #todo refactor the code
        return self.B

    def __str__(self) -> str:
        return "Segment["+str(self.A)+" "+str(self.B)+"]"

# important! elementary_functions module imports should be called after
# the declaration of Segment and Point classes, to avoid circular module dependencies
from elementary_functions import WhichSide,Intersection

"""Documentation for this class.

More details.
"""
class Direct_Segment:
    #Notice: 'beginning' stands for starting point and 'end' stands for ending one. The segment is directed from 'beginning' to 'end'
    def __init__(self, beginning, end):
        self.beginning = beginning
        self.end = end

    def get_side(self, Point) -> int:
        return self.beginning
        #todo refactor the code
        return self.end
    def intersects(self, other: Segment):
        return True


"""Documentation for this class.

More details.
"""
class Intersection_Point:
    def __init__(self, seg1:Segment, seg2:Segment):
        self.segment1 = seg1 
        self.segment2 = seg2
        self.intersection_point = Intersection(seg1, seg2) #function from elementary_functions.py
    def get_inter_point(self):
        return self.intersection_point


"""Documentation for this class.

More details.
"""
class Seg_Point_Side:
    def __init__(self, segment:Segment, point:Point):
        self.segment = segment
        self.point = point
        self.side = WhichSide(segment, point) #function from elementary_functions.py
    def get_side(self):
        return self.side


"""Documentation for this class.

More details.
"""
class Polygon:
    def __init__(self, vertices):
        self.vertices = PolygonVertexList(vertices)
    def get_vertices(self):
        return self.vertices


"""Documentation for this class.

More details.
"""
class List:
    def __init__(self):
        #todo add 'data' attribute to self
        pass
    def Add(self, element):
        #todo add 'data' attribute to self
        if not(element in self.data):
            self.data.append(element)
    def Del(self, element):
        try:
            self.data.remove(element)
        except:
            print(f"{element} is not in list")
    def Find(self, element):
        if element in self.data:
            return self.data.index(element)
        else:
            return None
    def IsEmpty(self):
        if len(self.data) == 0:
            return True
        else:
            return False
    def Size(self):
        return len(self.data)


"""Documentation for this class.

More details.
"""
class PointList(List):
    def __init__(self, points):
        #todo call __init__ of the superclass (List)
        assert all(isinstance(x, Point) for x in points)
        point_list = [x for x in points]
        self.data=point_list

"""Documentation for this class.

More details.
"""
class SegmentList(List):
    def __init__(self, segments):
        #todo call __init__ of the superclass (List)
        assert all(isinstance(x, Segment) for x in segments)
        seg_list = [x for x in segments]
        self.data=seg_list

"""Documentation for this class.

More details.
"""
class PolygonVertexList(List):
    def __init__(self, points):
        #todo call __init__ of the superclass (List)
        assert all(isinstance(x, Point) for x in points)
        point_list = [x for x in points]
        self.data=point_list

"""Documentation for this class.

More details.
"""
class PolygonList(List):
    def __init__(self, polygons):
        #todo call __init__ of the superclass (List)
        assert all(isinstance(x, Polygon) for x in polygons)
        pol_list = [x for x in polygons]
        self.data=pol_list

"""Documentation for this class.

More details.
"""
class IntersectionPointList(List):
    def __init__(self, elements):
        #todo call __init__ of the superclass (List)
        assert all(isinstance(x, Intersection_Point) for x in elements)
        elem_list = [x for x in elements]
        self.data=elem_list

"""Documentation for this class.

More details.
"""
class SegPointSideList(List):
    def __init__(self, elements):
        #todo call __init__ of the superclass (List)
        assert all(isinstance(x, Seg_Point_Side) for x in elements)
        elem_list = [x for x in elements]
        self.data=elem_list

