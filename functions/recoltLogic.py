from time import sleep
from functions.clickLogic import rightClick, leftClick
from functions.keyLogic import keyDown, keyUp, keyPress

def interact(point):
    rightClick(point)

def cut(point):
    leftClick((
        point[0],
        point[1]-100
    ))
    sleep(3)

def seed(point):
    leftClick((
        point[0]-95,
        point[1]-75
    ))
    sleep(3)
    return

def replant(point, KEYBIND, SHIFT, CTRL):
    if(SHIFT):
        keyDown('shift')
    if(CTRL):
        keyDown('ctrl')

    sleep(0.5)
    keyPress(KEYBIND)
    sleep(0.5)

    if(SHIFT):
        keyUp('shift')
    if(CTRL):
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




def recolt(point, RECOLT_TYPE, KEYBIND, SHIFT, CTRL):
    interact(point)
    sleep(1)
    if(RECOLT_TYPE == "SEED"):
        seed(point)
    if(RECOLT_TYPE == "RESOURCE"):
        cut(point)
        replant(point, KEYBIND, SHIFT, CTRL)