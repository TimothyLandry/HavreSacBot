import itertools
import math

def findNearestPoint(middle,points):
    dist = 10000
    smallest = (0,0)
    for p in points:
        d = abs(math.dist(middle, p))
        if(d < dist):
            dist = d
            smallest = p
    return smallest

def purgeTemplateFindings(input_list, threshold=10):
    combos = itertools.combinations(input_list, 2)
    points_to_remove = [point2 for point1, point2 in combos if math.dist(point1, point2)<=threshold]
    points_to_keep = [point for point in input_list if point not in points_to_remove]
    return points_to_keep

def convertPoint(point, sub):
    return (sub[0]+point[0], sub[1]+point[1])

def getMiddlePoint(point, w, h):
    return (int(point[0]+w/2), int(point[1]+h/2))