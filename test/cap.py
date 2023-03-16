import numpy as nm
import cv2
from PIL import ImageGrab

x1=408
y1=202
x2=1647
y2=862
cap = ImageGrab.grab(bbox =(x1, y1, x2, y2))
cap.save('captures/cap.jpg')