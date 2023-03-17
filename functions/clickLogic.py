import pyautogui
import random

def randomClick(x1,y1,x2,y2):
    pyautogui.click(random.randint(x1,x2), random.randint(y1,y2))

def rightClick(p):
    pyautogui.moveTo(p[0],p[1], random.uniform(0.1,0.4))
    pyautogui.rightClick(p[0],p[1])

def leftClick(p):
    pyautogui.moveTo(p[0],p[1], random.uniform(0.1,0.4))
    pyautogui.leftClick(p[0],p[1])
