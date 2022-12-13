from data_representation import *
import os
import re


# class Info:
#     def __init__(self, comment, content):
#         self.comment = comment
#         self.content = content

def pointFromLine(line, color: Color):
    line_copy = line
    list = line_copy.split(chr(9))
    return Point(float(list[0]), float(list[1]), color)


def segmentFromLine(line, color: Color):
    line_copy = line
    list = line_copy.split(chr(9))
    return Segment(Point(float(list[0]), float(list[1]), color), Point(float(list[2]), float(list[3]), color), color)


def intersecPointFromLine(line):
    line_copy = line
    list = line_copy.split(chr(9))
    seg1 = Segment(Point(float(list[0]), float(list[1]), int(list[4])),
                   Point(float(list[2]), float(list[3]), int(list[4])), int(list[4]))
    seg2 = Segment(Point(float(list[5]), float(list[6]), int(list[9])),
                   Point(float(list[7]), float(list[8]), int(list[9])), int(list[9]))
    point = Point(float(list[10]), float(list[11]), Color.NONE)
    return Intersection_Point(seg1, seg2, point)


def segPointSideFromLine(line):
    line_copy = line
    list = line_copy.split(chr(9))
    seg = Segment(Point(float(list[0]), float(list[1]), Color.NONE), Point(float(list[2]), float(list[3]), Color.NONE),
                  Color.NONE)
    point = Point(float(list[4]), float(list[5]), Color.NONE)
    if int(list[6]) == -1:
        side = Side.LEFT
    elif int(list[6]) == 1:
        side = Side.RIGHT
    else:
        side = Side.NONE
    return Seg_Point_Side(seg, point, side)


RE_SECTION_NAME = re.compile(r"\[(([a-zA-Z]+) ?([\d]*))\]\n")
"""
regex catching new sections and dividing it on 3 parts
f.e. "[points 1]\n" -> group(0) = "[points 1]\n"; group(1) = "points 1"; group(2) = "points"; group(3) = "1"
"""
RE_COMMENT = re.compile(r"\# ?([^\n]*)\n")
"""
regex catching comments and dividing it on 2 parts
f.e. "# Zestaw nr 3\n" -> group(0) = "# Zestaw nr 3\n"; group(1) = "Zestaw nr 3"
"""


def parse_file(dir_path):
    file = open(dir_path, 'r')
    count = 0

    section_name = ""
    sections_dictionary = {}
    start = False
    empty = True
    section_content = []
    flag = 0
    # section_content = PointsSet("","")

    while True:
        count += 1

        # Get next line from file
        line = file.readline()
        # print(line)
        # print(count)
        # Checking if line is a new section or a comment
        match_section_name = RE_SECTION_NAME.match(line)
        match_comment = RE_COMMENT.match(line)

        # if line is empty
        # end of file is reached
        if not line:
            if start:
                sections_dictionary[section_name] = section_content
                section_content = []
            break

        # If line is a new section
        if match_section_name:
            if empty:
                section_name = match_section_name.group(1)
                empty = False

            else:  # if there was no empty line between sections
                sections_dictionary[section_name] = section_content
                section_content = []
                section_name = match_section_name.group(1)
            start = True

            # If the section name is "info" then add nothing, pass
            if section_name == "info":
               # flag = 0
                start = False
                empty = True
            # If the section name contains "point" then set flag on 1 and turn start adding lines to content (lines 106-119)
            elif match_section_name.group(2) == "points":
                # start = True
                flag = 1
            # If the section name contains "segments" then set flag on 2 and turn start adding lines to content (lines 106-119)
            elif match_section_name.group(2) == "segments":
                # start = True
                flag = 2
            # If the section name contains "intersections" then set flag on 3 and turn start adding lines to content (lines 106-119)
            elif match_section_name.group(2) == "intersections":
                # start = True
                flag = 3
            # If the section name contains "polygon" then set flag on 4 and turn start adding lines to content (lines 106-119)
            elif match_section_name.group(2) == "polygon":
                # start = True
                flag = 4
            # If the section name contains "whichside" then set flag on 5 and turn start adding lines to content (lines 106-119)
            elif match_section_name.group(2) == "whichside":
                # start = True
                flag = 5
            # If the section name does not match any criterion given
            else:
                print("*********** ERROR ************\nvalid section name")

        # If comment or new line, then pass
        # elif line == "\n":
        #     start = False
        #     flag = 0
        #     # Adding object to dictionary
        #     sections_dictionary[section_name] = section_content
        #     section_content = []

        # Adding content of section
        elif start:
            if match_comment or line == "\n":
                pass
            else:
                # if flag == 1 or flag == 2:
                color = section_name[-1]
                if color == "0":
                    color = Color.NONE
                elif color == "1":
                    color = Color.BLUE
                elif color == "2":
                    color = Color.RED
                elif color == "3":
                    color = Color.GREEN
                else:  # If color not given or not needed
                    color = Color.NONE
                if flag == 1:
                    section_content.append(pointFromLine(line, color))
                elif flag == 2:
                    section_content.append(segmentFromLine(line, color))
                elif flag == 3:
                    section_content.append(intersecPointFromLine(line))
                elif flag == 4:
                    pass  # to implement
                elif flag == 5:
                    section_content.append(segPointSideFromLine(line))

        # Comment -> pass
        # elif line == "\n":
        #      pass

        # Content of section "info" or empty line or comment -> pass
        else:
            pass

        # print("Line{}: {}".format(count, line.strip()))

    file.close()
    return sections_dictionary


# GIVE THE PATH OF FILE YOU WANT TO USE
dict = parse_file("/dane.txt")
#print(dict)