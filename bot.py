import numpy as nm
import cv2

from functions.harvestLogic import HarvestLogic
from functions.templateLogic import TemplateLogic
from functions.capchaLogic import checkForFight

DEBUG = False
HARVEST_TYPE = "SEED" # "RESOURCE" "SEED"
KEYBIND = "3"
SHIFT = True
CTRL = False

p = ["croton","./patterns/herboriste/croton.png", 0.96, (255,255,255)]
# pazinclou

# Init Logics
harvestLogic = HarvestLogic(DEBUG, HARVEST_TYPE, KEYBIND, SHIFT, CTRL)
templateLogic = TemplateLogic(DEBUG, "./patterns/herboriste/croton.png", 0.9)

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

    # Template Logic
    resource = templateLogic.getNearestTemplate(x1,y1,x2,y2)
    if(resource):
        # Harvest logic
        harvestLogic.harvest(resource)
