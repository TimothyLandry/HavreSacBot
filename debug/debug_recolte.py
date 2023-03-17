import numpy as nm
import cv2

from functions.pointLogic import purgeTemplateFindings, findNearestPoint, convertPoint
from functions.screenshotLogic import grabRGBImage
from functions.clickLogic import rightClick

patterns = [
    ["croton","./patterns/herboriste/croton.png", 0.96, (255,255,255)],
]

#img_rgb = cv2.imread('./cap2.png')
x1=750
y1=350
x2=1150
y2=700

img_rgb = grabRGBImage(x1, y1, x2, y2)

for p in patterns:
    template = cv2.imread(p[1])
    w, h = template.shape[:-1]

    res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
    loc = nm.where(res >= p[2])

    points = purgeTemplateFindings(list(zip(*loc[::-1])))

    x, y = img_rgb.shape[:-1]
    middle = (x/2,y/3)
    nearest = findNearestPoint(middle, points)
    cv2.rectangle(img_rgb, nearest, (nearest[0] + h, nearest[1] + w), p[3], 2)

    real_point = convertPoint(nearest, (x1, y1, x2, y2))
    rightClick(real_point)


cv2.imwrite('result.png', img_rgb)