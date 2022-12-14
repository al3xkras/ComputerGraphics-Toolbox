from parser import *
from data_representation import *

def intersect_check(data_file):
    dict = parse_file(data_file)
    intersections = dict['intersections']
    info =[]
    for i in range(len(intersections)):
        inter_point = Intersection(intersections[i].segment1, intersections[i].segment2)
        if inter_point != intersections[i].intersection_point:
            info.append("Point " +  str(i) + " incorrectly calculated!")
    
        