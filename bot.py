from logic.harvestLogic import HarvestLogic
from logic.templateLogic import TemplateLogic
from logic.captchaLogic import CaptchaLogic

DEBUG = True
HARVEST_TYPE = "SEED" # "RESOURCE" "SEED"
JOB = "forestier"
RESOURCE_NAME = "sureau"
KEYBIND = "3"
SHIFT = True
CTRL = False



p = ["croton","./patterns/herboriste/croton.png", 0.96, (255,255,255)]
# pazinclou

# Init Logics
harvestLogic = HarvestLogic(DEBUG, JOB, HARVEST_TYPE, KEYBIND, SHIFT, CTRL)
templateLogic = TemplateLogic(DEBUG, f"./patterns/{JOB}/{RESOURCE_NAME}.png", 0.95)
captchaLogic = CaptchaLogic(DEBUG)

# Coordinates for 400 x 350 around character
x1=600 #750
y1=150 #350
x2=1300 #1150
y2=800 #700

#######################
# Loop
#######################
while True:
    if(captchaLogic.checkForFight()):
        print("\nCAPCHAT FOUND\n")
        break
        #captchaLogic.solve()
        

    # Template Logic
    resource = templateLogic.getNearestTemplate(x1,y1,x2,y2)
    if(resource):
        # Harvest logic
        harvestLogic.harvest(resource)
