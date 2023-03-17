
import numpy as nm
import cv2
from time import sleep

from logic.templateLogic import TemplateLogic
from logic.keyLogic import keyPress
from logic.clickLogic import leftClick
from logic.screenshotLogic import grabBlackImage, grabRGBImage
from logic.pointLogic import getMiddlePoint, purgeTemplateFindings, findNearestPoint, convertPoint

class CaptchaLogic:
    def __init__(self, DEBUG):
        self.threshold = 0.9
        self.DEBUG = DEBUG
        self.hpTemplate = TemplateLogic(True, "./patterns/captcha/healthbar.png", self.threshold)
        self.resetTemplates()
    
    def resetTemplates(self):
        self.templates = [
            (TemplateLogic(True, "./patterns/captcha/one.png", self.threshold), False),
            (TemplateLogic(True, "./patterns/captcha/two.png", self.threshold), False),
            (TemplateLogic(True, "./patterns/captcha/three.png", self.threshold), False),
            (TemplateLogic(True, "./patterns/captcha/four.png", self.threshold), False),
            (TemplateLogic(True, "./patterns/captcha/five.png", self.threshold), False),
            (TemplateLogic(True, "./patterns/captcha/six.png", self.threshold), False),
            (TemplateLogic(True, "./patterns/captcha/seven.png", self.threshold), False),
            (TemplateLogic(True, "./patterns/captcha/eight.png", self.threshold), False)
        ]

    def checkForFight(self):
        img = grabBlackImage(25, 25, 50 , 50)
        img = nm.array(img)
        for i in img:
            for x in i:
                if(x != 15):
                    return False
        return True

    def flagTemplate(self, index):
        self.templates[index] = (self.templates[index][0], True)
    
    def findTemplates(self, img):
        self.resetTemplates()
        threshold = self.threshold
        decay = 0.05

        points = []
        findings = 0
        while threshold > 0.6:
            for i,t in enumerate(self.templates):
                if(t[1] == False): # If not already found
                    p = t[0].lookForTemplateInImg(img)
                    p = purgeTemplateFindings(p, 200)
                    if(len(p)==2):
                        findings +=1
                        self.flagTemplate(i)
                        p1 = getMiddlePoint(p[0],t[0].h, t[0].w)
                        p2 = getMiddlePoint(p[1],t[0].h, t[0].w)
                        points = points + [p1,p2]
                    t[0].decreaseThreshold(decay)
                pass
            if(findings<3):
                threshold -= decay
            else:
                if(self.DEBUG):
                    for p in points:
                        cv2.rectangle(img, p, (p[0], p[1]), (255,255,255), 15)
                    cv2.imwrite('DEBUG.png', img)
                return points
            
    def findHealthBar(self, img):
        b = self.hpTemplate.lookForTemplateInImg(img)[0]
        if(self.DEBUG):
            cv2.rectangle(img, b, (b[0], b[1]), (255,255,255), 15)
            cv2.imwrite('DEBUG.png', img)
        return b

    def getThreeNearest(self,img, points):
        b = self.findHealthBar(img)
        final = []
        findings = 0
        while(findings < 3):
            print(points, b)
            n = findNearestPoint(b, points)
            points.remove(n)
            final.append(n)
            if(self.DEBUG):
                cv2.rectangle(img, n, (n[0], n[1]), (0,0,0), 10)
            findings +=1

        if(self.DEBUG):
            cv2.imwrite('DEBUG.png', img)

        return final
        
    def solve(self):
        points = None
        while(points == None or len(points) <6):
            keyPress('f1')
            sleep(3)
            keyPress('f1')
            sleep(0.3)
            img = grabRGBImage(350, 200, 1700, 900)
            if(self.DEBUG):
                cv2.imwrite('DEBUG.png', img)
            points = self.findTemplates(img)
            print(points)

        near = self.getThreeNearest(img,points)

        for n in near:
            n = convertPoint(n, (350, 200, 1700, 900))
            keyPress('1')
            sleep(0.5)
            leftClick(n)
            sleep(0.5)
        
        keyPress('esc')
        sleep(3)
