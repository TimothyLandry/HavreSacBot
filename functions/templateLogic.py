import numpy as nm
import cv2

from functions.screenshotLogic import grabRGBImage
from functions.pointLogic import purgeTemplateFindings, findNearestPoint, convertPoint, getMiddlePoint


class TemplateLogic:
    def __init__(self, DEBUG, templatePath, threshold):
        self.templatePath = templatePath
        self.threshold = threshold
        self.DEBUG = DEBUG
        self.loadTemplate()

    def loadTemplate(self):
        self.template = cv2.imread(self.templatePath)
        self.w, self.h = self.template.shape[:-1]

    def lookForTemplate(self, x1, y1, x2, y2):
        self.img_rgb = grabRGBImage(x1, y1, x2, y2)

        # Template matching
        res = cv2.matchTemplate(self.img_rgb, self.template, cv2.TM_CCOEFF_NORMED)
        loc = nm.where(res >= self.threshold)
        points = purgeTemplateFindings(list(zip(*loc[::-1])))
        return points
        
    def getNearestTemplate(self,  x1, y1, x2, y2):
        points = self.lookForTemplate(x1,y1,x2,y2)
        # Finding nearest point compared to the character (approximate)
        x, y = self.img_rgb.shape[:-1]
        middle = (x/2,y/2)
        nearest = findNearestPoint(middle, points)
        if(self.DEBUG):
            cv2.rectangle(self.img_rgb, nearest, (nearest[0] + self.h, nearest[1] + self.w), (255,255,255), 2)

        nearest = getMiddlePoint(nearest, self.w, self.h)
        if(self.DEBUG):
            cv2.rectangle(self.img_rgb, nearest, (nearest[0] , nearest[1]), (255,255,255), 5)

        # Converting point from 400x350 to 1920x1080
        real_point = convertPoint(nearest, (x1, y1, x2, y2))

        # DEBUG - Image output
        if(self.DEBUG):
            cv2.imwrite('DEBUG.png', self.img_rgb)

        return real_point