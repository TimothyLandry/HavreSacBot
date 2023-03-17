from PIL import ImageGrab
import cv2
import os

def grabRGBImage(x1,y1,x2,y2):
    cap = ImageGrab.grab(bbox =(x1, y1, x2, y2))
    cap.convert('RGBA').save('cap.png')
    img_rgb = cv2.imread('cap.png')
    os.remove('cap.png')
    return img_rgb

def grabBlackImage(x1,y1,x2,y2):
    cap = ImageGrab.grab(bbox =(x1, y1, x2, y2))
    cap.convert('RGBA').save('cap.png')
    img_black = cv2.imread('cap.png',0)
    os.remove('cap.png')
    return img_black