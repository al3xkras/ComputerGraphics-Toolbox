from data_representation import *
from io_operations import parse_file
from numpy import nan
from math import isnan

def intersect_check(data_file):
    dict = parse_file(data_file)
    intersections = dict['intersections']
    info =[]
    for i in range(len(intersections)):
        inter_point = Intersection(intersections[i].segment1, intersections[i].segment2)
        if (isnan(inter_point.x) and isnan(intersections[i].intersection_point.x)):
            pass 
        elif inter_point != intersections[i].intersection_point:
            info.append("Point " +  str(i) + " incorrectly calculated! Calculated result: (" + str(inter_point.x) + "," + str(inter_point.y) + ")\n")
    f = open("test_data_set\out.txt", "w")
    for section in dict:
        f.write(section + "\n")
        for el in dict[section]:
            line = str(el.segment1.A.x)+chr(9)+str(el.segment1.A.y)+chr(9)+str(el.segment1.B.x)+chr(9)+str(el.segment1.B.y)+chr(9)+str(el.segment1.color)+chr(9)+str(el.segment2.A.x)+chr(9)+str(el.segment2.A.y)+chr(9)+str(el.segment2.B.x)+chr(9)+str(el.segment2.B.y)+chr(9)+str(el.segment2.color)+chr(9)+str(el.intersection_point.x)+chr(9)+str(el.intersection_point.y)+"\n"
            f.write(line)
    f.write("[info]\n")
    for infoline in info:
        f.write(infoline)
    if len(info) == 0:
        f.write("Everything correct!\n")
    f.close()

intersect_check("test_data_set/test_data_intersections.txt")
    
        