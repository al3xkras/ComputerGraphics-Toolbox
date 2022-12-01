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
class PointList:
    #todo implement
    pass
class SegmentList:
    #todo implement
    pass
class Polygon:
    def __init__(self, vertices):
        self.vertices = PolygonVertexList(vertices)
    def get_vertices(self):
        return self.vertices

class PolygonVertexList:
    def __init__(self, vertices):
        if vertices is None:
            vertices=tuple()
        vert_list = [x for x in vertices]
        assert all(isinstance(x, Point) for x in vert_list)
        self.data=vert_list

    def Add(self, vertex:Point):
        #todo check for self-intersections
        assert vertex is not None
        self.data.append(vertex)
    def Remove(self,index=None):
        if index is None:
            index= len(self.data) - 1
        self.data.remove(index)
    def __index__(self, index):
        return self.data[index]
    def __hash__(self):
        return self.data.__hash__()
    def __len__(self):
        return len(self.data)
    def Size(self):
        return len(self)
    def isEmpty(self):
        return len(self)==0
    def Find(self, vertex):
        return vertex in self.data
    def __add__(self, other):
        if isinstance(other,PolygonVertexList):
            self.data+=other.data
        elif isinstance(other,Polygon):
            self.data.append(other)


class PolygonList:
    def __init__(self, polygons):
        """
        :param polygons: any Iterable containing objects of type Polygon
        """
        if polygons is None:
            polygons=tuple()
        poly_list = [x for x in polygons]
        assert all(isinstance(x,Polygon) for x in poly_list)
        self.data=poly_list

    def Add(self, polygon:Polygon):
        assert polygon is not None
        self.data.append(polygon)

    def Remove(self,index=None):
        if index is None:
            index= len(self.data) - 1
        self.data.remove(index)
    def __index__(self, index):
        return self.data[index]
    def __hash__(self):
        return self.data.__hash__()
    def __len__(self):
        return len(self.data)
    def __add__(self, other):
        if isinstance(other,PolygonList):
            self.data+=other.data
        elif isinstance(other,Polygon):
            self.data.append(other)


