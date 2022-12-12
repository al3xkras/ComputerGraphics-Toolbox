"""@package docstring
Documentation for this module.

More details.
"""
from elementary_functions import Intersection
from data_representation import *

class Info:
    def __init__(self, caption, comment):
        self.caption = caption
        self.comment = comment

def pointFromLine(line, color:Color):
    list = line.split(chr(9))
    return Point(float(list[0]), float(list[1]), color)

def segmentFromLine(line, color:Color):
    list = line.split(chr(9))
    return Segment(Point(float(list[0]), float(list[1]), color), Point(float(list[2]), float(list[3]), color),color)

def intersecPointFromLine(line):
    list = line.split(chr(9))
    seg1 = Segment(Point(float(list[0]), float(list[1]), int(list[4])), Point(float(list[2]), float(list[3]), int(list[4])),int(list[4]))
    seg2 = Segment(Point(float(list[5]), float(list[6]), int(list[9])), Point(float(list[7]), float(list[8]), int(list[9])),int(list[9]))
    point = Point(float(list[10]), float(list[11]), Color.NONE)
    return Intersection_Point(seg1, seg2, point)

def segPointSideFromLine(line):
    list = line.split(chr(9))
    seg = Segment(Point(float(list[0]), float(list[1]), Color.NONE), Point(float(list[2]), float(list[3]), Color.NONE),Color.NONE)
    point = Point(float(list[4]), float(list[5]), Color.NONE)
    if int(list[6]) == -1:
        side = Side.LEFT
    elif int(list[6]) == 1:
        side = Side.RIGHT
    else:
        side = Side.NONE
    return Seg_Point_Side(seg, point, side)

def DataInfo(filepath):
    file = open(filepath, "r")
    lines = file.readlines()
    file.close()
    infoList = []
    i = 0
    while i < len(lines):
        if lines[i][0] == '[':
            caption = lines[i][1:].split(']')[0]
            i+=1
            comment = ''
            if caption == 'info':
                while lines[i] != '':
                    comment += lines[i]
                    i += 1
            else:
                while lines[i][0] == '#':
                    comment += lines[i]
            info = Info(caption, comment)
            infoList.append(info)
    return infoList


    




