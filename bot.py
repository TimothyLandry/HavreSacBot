import numpy as nm
import cv2

from functions.recoltLogic import RecoltLogic
from functions.templateLogic import TemplateLogic
from functions.capchaLogic import checkForFight

DEBUG = False
RECOLT_TYPE = "SEED" # "RESOURCE" "SEED"
KEYBIND = "3"
SHIFT = True
CTRL = False

p = ["croton","./patterns/herboriste/croton.png", 0.96, (255,255,255)]

# Init Logics
recoltLogic = RecoltLogic(DEBUG, RECOLT_TYPE, KEYBIND, SHIFT, CTRL, p[1], p[2])
templateLogic = TemplateLogic(DEBUG, "./patterns/herboriste/croton.png", 0.96)

# Coordinates for 400 x 350 around character
x1=750
y1=350
x2=1150
y2=700

#######################
# Loop
#######################
#while True:
if(checkForFight()):
    print("\nCAPCHAT FOUND\n")
    exit
    #break

# Template Logic
resource = templateLogic.getNearestTemplate(x1,y1,x2,y2)

# Recolt logic
recoltLogic.recolt(resource)
