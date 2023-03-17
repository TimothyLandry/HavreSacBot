from functions.screenshotLogic import grabBlackImage
import cv2
import numpy as nm

def checkForFight():
    img = grabBlackImage(25, 25, 50 , 50)
    img = nm.array(img)
    for i in img:
        for x in i:
            if(x != 15):
                return False
    return True