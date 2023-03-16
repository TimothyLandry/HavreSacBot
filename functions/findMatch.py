import cv2
import numpy as nm

def checkIfUpper(pos):
    y = 1080 - (pos[0]   * 0.5625)
    if(pos[1] < y):
        return True
    else:
        return False


def checkIfUnder(pos):
    y = 1080 - (pos[0] * 0.5625)
    if(pos[1] > y):
        return True
    else:
        return False
    
def getMiddle(pos, template):
    w, h = template.shape[:-1]
    return (int(pos[0]+h/2),int(pos[1]+w/2))

def findMatch(img_rgb, patterns):
    threshold = 0.7
    while threshold > 0.6:
        index = 0
        for p in patterns:
            template = cv2.imread(p[1])
            res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
            loc = nm.where(res >= threshold)

            first = (0,0)
            current = (0,0)
            for pt in zip(*loc[::-1]):
                if(first == (0,0)):
                    first = pt
                current = pt
            if(checkIfUpper(first) and checkIfUnder(current)):
                print(first)
                print(current)
                return (index,getMiddle(first,template),getMiddle(current,template))      
               
        index+=1
        threshold-=0.05
    raise Exception("nomatch")