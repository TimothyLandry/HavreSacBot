import pyautogui
import random

def randomClick(x1,y1,x2,y2):
    pyautogui.click(random.randint(x1,x2), random.randint(y1,y2))

def rightClick(p):
    pyautogui.rightClick(p[0],p[1])

def leftClick(p):
    pyautogui.leftClick(p[0],p[1])
