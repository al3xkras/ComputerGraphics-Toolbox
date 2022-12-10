import os
import re


# class Info:
#     def __init__(self, comment, content):
#         self.comment = comment
#         self.content = content

class PointsSet:
    """
    Class creating object containing name of the points section and its content as a text
    """
    def __init__(self, name, content):
        self.name = name
        self.content = content

class Segments:
    """
    Class creating object containing name of the segments section and its content as a text
    """
    def __init__(self, name, content):
        self.name = name
        self.content = content

class Intersections:
    """
    Class creating object containing name of the intersections section and its content as a text
    """
    def __init__(self, name, content):
        self.name = name
        self.content = content

class Polygon:
    """
    Class creating object containing name of the polygons section and its content as a text
    """
    def __init__(self, name, content):
        self.name = name
        self.content = content

class WhichSide:
    """
    Class creating object containing name of the whichside section and its content as a text
    """
    def __init__(self, name, content):
        self.name = name
        self.content = content

RE_SECTION_NAME = re.compile(r"\[(([a-zA-Z]+) ?[\d]*)\]\n")
"""
regex catching new sections and dividing it on 3 parts
f.e. "[points 1]\n" -> group(0) = "[points 1]\n"; group(1) = "points 1"; group(2) = "points"
"""
RE_COMMENT = re.compile(r"\# ?([^\n]*)\n")
"""
regex catching comments and dividing it on 2 parts
f.e. "# Zestaw nr 3\n" -> group(0) = "# Zestaw nr 3\n"; group(1) = "Zestaw nr 3"
"""

def parse_file(dir_path):
    file = open(dir_path, 'r')
    # count = 0

    section_name = ""
    content = ""
    sections_dictionary = {}
    start = False
    flag = 0
    section_content = PointsSet("","")

    while True:
        # count += 1

        # Get next line from file
        line = file.readline()

        # Checking if line is a new section or a comment
        match_section_name = RE_SECTION_NAME.match(line)
        match_comment = RE_COMMENT.match(line)

        # If line is a new section
        if match_section_name:
            section_name = match_section_name.group(1)
            # If the section name is "info" then add nothing, pass
            if section_name == "info":
                pass
            # If the section name contains "point" then set flag on 1 and turn start adding lines to content (lines 106-119)
            elif match_section_name.group(2) == "points":
                start = True
                flag = 1
            # If the section name contains "segments" then set flag on 2 and turn start adding lines to content (lines 106-119)
            elif match_section_name.group(2) == "segments":
                start = True
                flag = 2
            # If the section name contains "intersections" then set flag on 3 and turn start adding lines to content (lines 106-119)
            elif match_section_name.group(2) == "intersections":
                start = True
                flag = 3
            # If the section name contains "polygon" then set flag on 4 and turn start adding lines to content (lines 106-119)
            elif match_section_name.group(2) == "polygon":
                start = True
                flag = 4
            # If the section name contains "whichside" then set flag on 5 and turn start adding lines to content (lines 106-119)
            elif match_section_name.group(2) == "whichside":
                start = True
                flag = 5
            # If the section name does not match any criterion given
            else: print("*********** ERROR ************\nvalid section name")

        # Adding content of section
        elif start:
            # ";" is set as separator - the end of content in the section
            if ";" in line:
                content += line
                start = False
                # Adding content to object in class selected according to the value of the flag
                if flag == 1: section_content = PointsSet(section_name, content)
                elif flag == 2: section_content = Segments(section_name, content)
                elif flag == 3: section_content = Intersections(section_name, content)
                elif flag == 4: section_content = Polygon(section_name, content)
                elif flag == 5: section_content = WhichSide(section_name, content)
                # Adding object to dictionary
                sections_dictionary[section_name] = section_content
                # Clearing content
                content = ""
            else:
                # If comment then pass, else add to content
                if match_comment: pass
                else: content += line

        # If comment or new line, then pass
        elif match_comment or line == "\n":
            pass

        # Content of section "info", pass
        else: pass


        # if line is empty
        # end of file is reached
        if not line:
            break
        # print("Line{}: {}".format(count, line.strip()))

    file.close()
    return sections_dictionary

# GIVE THE PATH OF FILE YOU WANT TO USE
parse_file(".../test.txt")