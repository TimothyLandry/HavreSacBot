from time import sleep
from functions.clickLogic import rightClick, leftClick
from functions.keyLogic import keyDown, keyUp, keyPress
from functions.templateLogic import TemplateLogic

class HarvestLogic:
    def __init__(self, DEBUG, HARVEST_TYPE, KEYBIND, SHIFT, CTRL):
        self.KEYBIND = KEYBIND
        self.SHIFT = SHIFT
        self.CTRL = CTRL
        self.HARVEST_TYPE = HARVEST_TYPE

        self.cutTemplateLogic = TemplateLogic(DEBUG, "./patterns/harvest/resource1.png", 0.9)
        self.seedTemplateLogic = TemplateLogic(DEBUG, "./patterns/harvest/seed.png", 0.9)

    def interact(self, point):
        rightClick(point)
        sleep(0.5)

    def cut(self, point):
        p = self.cutTemplateLogic.getNearestTemplate(point[0]-100, point[1]-150, point[0]+100, point[1]+50)
        if(p):
            leftClick(p)
            sleep(3)

    def seed(self, point):
        p = self.seedTemplateLogic.getNearestTemplate(point[0]-100, point[1]-150, point[0]+100, point[1]+50)
        if(p == None):
            self.cut(point)
        else:
            leftClick(p)
            sleep(3)
        return

    def replant(self, point):
        if(self.SHIFT):
            keyDown('shift')
        if(self.CTRL):
            keyDown('ctrl')

        sleep(0.5)
        keyPress(self.KEYBIND)
        sleep(0.5)

        if(self.SHIFT):
            keyUp('shift')
        if(self.CTRL):
            keyUp('ctrl')

        sleep(0.5)
        plantpoint = (
            point[0],
            point[1]+30
        )
        leftClick(plantpoint)
        sleep(3)
        # Unselect item
        rightClick(plantpoint)


    def harvest(self, point):
        self.interact(point)
        
        if(self.HARVEST_TYPE == "SEED"):
            self.seed(point)
        if(self.HARVEST_TYPE == "RESOURCE"):
            self.cut(point)
            #self.replant(point)