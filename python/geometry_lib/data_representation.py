
class Point:
    #todo implement
    pass

#enum Side
class Side:
    LEFT=-1
    RIGHT=1
    NONE=0

class Color:
    #todo implement
    pass

class Segment:
    pass
class Direct_Segment:
    #todo implement
    def __init__(self, p1, p2):
        pass

    def get_side(self, point) -> int:
        return Side.LEFT

    def intersects(self, other: Segment):
        return True

class Intersection_Point:
    def __init__(self, seg1:Segment, seg2:Segment):
        self.segment1 = seg1 
        self.segment2 = seg2
        self.intersection_point = Intersection(seg1, seg2) #function from elementary_functions.py
    def get_inter_point(self):
        return self.intersection_point

class Seg_Point_Side:
    def __init__(self, segment:Segment, point:Point):
        self.segment = segment
        self.point = point
        self.side = WhichSide(segment, point) #function from elementary_functions.py
    def get_side(self):
        return self.side

class Polygon:
    def __init__(self, vertices):
        self.vertices = PolygonVertexList(vertices)
    def get_vertices(self):
        return self.vertices


class List:
    def __init__(self):
        pass
    def Add(self, element):
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


class PointList(List):
    def __init__(self, points):
        assert all(isinstance(x, Point) for x in points)
        point_list = [x for x in points]
        self.data=point_list
    
class SegmentList(List):
    def __init__(self, segments):
        assert all(isinstance(x, Segment) for x in segments)
        seg_list = [x for x in segments]
        self.data=seg_list

class PolygonVertexList(List):
    def __init__(self, points):
        assert all(isinstance(x, Point) for x in points)
        point_list = [x for x in points]
        self.data=point_list

class PolygonList(List):
    def __init__(self, polygons):
        assert all(isinstance(x, Polygon) for x in polygons)
        pol_list = [x for x in polygons]
        self.data=pol_list

class IntersectionPointList(List):
    def __init__(self, elements):
        assert all(isinstance(x, Intersection_Point) for x in elements)
        elem_list = [x for x in elements]
        self.data=elem_list

class SegPointSideList(List):
    def __init__(self, elements):
        assert all(isinstance(x, Seg_Point_Side) for x in elements)
        elem_list = [x for x in elements]
        self.data=elem_list