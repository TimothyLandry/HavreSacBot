import numpy as nm
import cv2

from functions.pointLogic import purgeTemplateFindings, findNearestPoint, convertPoint, getMiddlePoint
from functions.screenshotLogic import grabRGBImage
from functions.recoltLogic import recolt
from functions.capchaLogic import checkForFight

DEBUG = False
RECOLT_TYPE = "SEED" # "RESOURCE" "SEED"
KEYBIND = "3"
SHIFT = True
CTRL = False

p = ["croton","./patterns/herboriste/croton.png", 0.96, (255,255,255)]

# Load template
template = cv2.imread(p[1])
w, h = template.shape[:-1]

# Coordinates for 400 x 350 around character
x1=750
y1=350
x2=1150
y2=700

#######################
# Loop
#######################
while True:
    if(checkForFight()):
        print("\nCAPCHAT FOUND\n")
        break

    img_rgb = grabRGBImage(x1, y1, x2, y2)

    # Template matching
    res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
    loc = nm.where(res >= p[2])

    # Purging duplicate findings
    points = purgeTemplateFindings(list(zip(*loc[::-1])))

    # Finding nearest point compared to the character (approximate)
    x, y = img_rgb.shape[:-1]
    middle = (x/2,y/2)
    nearest = findNearestPoint(middle, points)

    # DEBUG - Template rectangle
    if(DEBUG):
        cv2.rectangle(img_rgb, nearest, (nearest[0] + h, nearest[1] + w), p[3], 2)

    nearest = getMiddlePoint(nearest, w, h)

    # DEBUG - Click rectangle
    if(DEBUG):
        cv2.rectangle(img_rgb, nearest, (nearest[0] , nearest[1]), p[3], 5)

    # Converting point from 400x350 to 1920x1080
    real_point = convertPoint(nearest, (x1, y1, x2, y2))

    # Recolt logic
    recolt(real_point, RECOLT_TYPE, KEYBIND, SHIFT, CTRL)

    # DEBUG - Image output
    if(DEBUG):
        cv2.imwrite('DEBUG.png', img_rgb)