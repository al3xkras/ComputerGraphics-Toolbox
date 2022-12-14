"""@package docstring
Documentation for this module.

More details.
"""
from parser import *

class FilePrintStream:
    line_end='\n'
    def __init__(self,filename):
        self.fname=filename
        self._file=None

    def open(self):
        if not self._file:
            self._file=open(self.fname,'w+')

    def write_line(self,line):
        if self._file:
            self._file.write(line+self.line_end)

    def close(self):
        if self._file:
            self._file.close()

class TestOutputWriter:
    values='values'
    intersections='intersections'
    title='title'
    info='info'
    section_end= ''
    info_expr='[info]\n#%s'
    title_expr='[%s]'
    point_expr="%.3f %.3f %s" #x y color
    segment_expr="%.3f %.3f %.3f %.3f %s" #x1 y1 x2 y2 color
    intersection_point_expr="%.3f %.3f %.3f %.3f %s %.3f %.3f %.3f %.3f %s %.3f %.3f"
    seg_point_side_expr="%.3f %.3f %.3f %.3f %.3f %.3f %d" #x1 y1 x2 y2 x3 y3
    val_type_formats={
        Point:point_expr,
        Segment:segment_expr,
        Intersection_Point:intersection_point_expr,
        Seg_Point_Side:seg_point_side_expr,
        str:title_expr
    }
    val_to_params={
        Point: lambda p:(p.x,p.y,p.color),
        Segment: lambda s:(s.A.x,s.A.y,s.B.x,s.B.y,s.color),
        Intersection_Point: lambda ip: (ip.segment1.A.x,ip.segment1.A.y,ip.segment1.B.x,ip.segment1.B.y,ip.segment1.color,
                                        ip.segment1.A.x,ip.segment1.A.y,ip.segment1.B.x,ip.segment1.B.y,ip.segment1.color,
                                        ip.intersection_point.x,ip.intersection_point.y),
        Seg_Point_Side: lambda sps: (sps.segment.A.x,sps.segment.A.y,sps.segment.B.x,sps.segment.B.y,
                                     sps.point.x,sps.point.y,
                                     sps.side),
        str: lambda s: TestOutputWriter.title_expr%s
    }

    def __init__(self):
        self.sections=dict()
        self.header=None

    """
    def run_intersection_test(self):
        _type=self.intersections
        _tests=self.sections[_type]
        test_results=[]
        for i in range(0,len(_tests)):
            _t=_tests[i]
            p=_t.intersection_point
            _t=_t.segment1,_t.segment2
            if len(_t)<2: break
            test_results.append([_t[0],_t[1],p,Intersection(*_t)])
        #todo complete implementation
        for _x in test_results:
            for y in _x:
                print(y)
            print()"""

    def add_section(self,section_name):
        assert not section_name in self.sections
        self.sections[section_name]={
            self.title:section_name,
            self.values:[]
        }

    def set_section_title(self,section,title):
        self.sections[section][self.title]=title

    def add_section_value(self,section,value):
        self.sections[section][self.values].append(value)

    def remove_section_value_by_index(self,section,i):
        del self.sections[section][self.values][i]

    def remove_section_value(self,section,value):
        self.sections[section][self.values].remove(value)

    def set_section_info(self, section, info):
        self.sections[section][self.info]=info


    def set_header(self,header):
        self.header=header

    def print_to_stream(self, print_stream):
        #todo implement
        if self.header:
            print_stream.write_line(self.info_expr%self.header)
            print_stream.write_line(self.section_end)
        for s in self.sections:
            s_val=self.sections[s]
            print_stream.write_line(self.title_expr%s_val[self.title])
            for val in s_val[self.values]:
                vtype=type(val)
                print_stream.write_line(
                    self.val_type_formats[vtype]
                        %(self.val_to_params[vtype](val)))

            if self.info in s_val:
                print_stream.write_line(self.info_expr%s_val[self.info])
            print_stream.write_line(self.section_end)

    def print_to_file(self, filename):
        fs=FilePrintStream(filename)
        fs.open()
        self.print_to_stream(fs)
        fs.close()

    @staticmethod
    def from_dict(sections, header=None):
        w=TestOutputWriter()
        if header:
            w.set_header(header)
        for section_name in sections:
            w.add_section(section_name)
            for val in sections[section_name]:
                w.add_section_value(section_name,val)
        return w


if __name__ == '__main__':
    t=TestOutputWriter.from_dict(test_cases())
    t.set_section_info("points 0","Additional info goes here")
    t.set_header("This is the title")
    t.print_to_file("./test_out.txt")
    #t.run_intersection_test()

