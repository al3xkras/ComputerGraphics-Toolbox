class Point:
    #todo implement
    pass

class Color:
    #todo implement
    pass

class Segment:
    pass
class Vector:
    #todo implement
    def __init__(self, p1, p2):
        pass

    def get_side(self, point) -> VectorSide:
        return VectorSide.LEFT

    def intersects(self, other: Segment):
        return True
class PointList:
    #todo implement
    pass
class SegmentList:
    #todo implement
    pass
class Polygon:
    #todo implement
    def get_vertices(self):
        #todo return a PolygonVertexList
        pass

class PolygonVertexList:
    def __init__(self, vertices):
        if vertices is None:
            vertices=tuple()
        vert_list = [x for x in vertices]
        assert all(isinstance(x, Point) for x in vert_list)
        self._vertices=vert_list
        self._segments = [Vector(vertices[i],vertices[(i+1)%len(vertices)]) for i in range(vertices)]

    def add_vertex(self, vertex:Point):
        #todo check for self-intersections
        assert vertex is not None
        self._vertices.append(vertex)
    def remove_vertex(self):
        self._vertices.remove(len(self._vertices)-1)
    def remove_vertex(self,index):
        self._vertices.remove(index)
    def __index__(self, index):
        return self._vertices[index]
    def __hash__(self):
        return self._vertices.__hash__()
    def __len__(self):
        return len(self._vertices)
    def __add__(self, other):
        if isinstance(other,PolygonVertexList):
            self._vertices+=other._vertices
        elif isinstance(other,Polygon):
            self._vertices.append(other)


class PolygonList:
    def __init__(self, polygons):
        """
        :param polygons: any Iterable containing objects of type Polygon
        """
        if polygons is None:
            polygons=tuple()
        poly_list = [x for x in polygons]
        assert all(isinstance(x,Polygon) for x in poly_list)
        self._polygons=poly_list

    def add_polygon(self, polygon:Polygon):
        assert polygon is not None
        self._polygons.append(polygon)

    def remove_polygon(self):
        self._polygons.remove(len(self._polygons)-1)
    def remove_polygon(self,index):
        self._polygons.remove(index)
    def __index__(self, index):
        return self._polygons[index]
    def __hash__(self):
        return self._polygons.__hash__()
    def __len__(self):
        return len(self._polygons)
    def __add__(self, other):
        if isinstance(other,PolygonList):
            self._polygons+=other._polygons
        elif isinstance(other,Polygon):
            self._polygons.append(other)

#enum VectorSide
class VectorSide:
    LEFT=-1
    RIGHT=1
    NONE=0

