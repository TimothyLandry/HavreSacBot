import numpy as nm
import cv2
from PIL import ImageGrab

x1=408
y1=202
x2=1647
y2=862
#cap = ImageGrab.grab(bbox =(x1, y1, x2, y2))
#cap.save('debug.jpg')

def checkForPair(loc):
    for pt in zip(*loc[::-1]):  # Switch columns and rows
        print (pt)
        cv2.rectangle(img_rgb, pt, (pt[0] + h, pt[1] + w), p[3], 2)
    return


patterns = [
    # [name, path, threshold, color]
    ["one","./patterns/one.png", 0.80, (0,0,0)],
    ["two","./patterns/two.png", 0.8, (255,0,0)],
    ["three","./patterns/three.png", 0.75, (255,255,0)],
    ["four","./patterns/four.png", 0.75, (255,255,255)],
    ["five","./patterns/five.png", 0.65, (0,255,255)],
    ["six","./patterns/six.png", 0.8, (0,0,255)],
    ["seven","./patterns/seven.png", 0.65, (127,127,127)],
    ["eight","./patterns/eight.png", 0.55, (45,100,45)],
]

img_rgb = cv2.imread('./captures/cap7.jpg')

found = 0
threshold = 0.9
while found < 3:
    print("start")
    for p in patterns:
        template = cv2.imread(p[1])
        w, h = template.shape[:-1]

        res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
        
        loc = nm.where(res >= threshold)

        print(p[0])
        print(loc)
        print(len(loc))

        last_x =0
        last_y =0
        for pt in zip(*loc[::-1]):  # Switch columns and rows
            if(not(last_x == 0 and last_y ==0)):
                if((pt[0]-last_x) > 10 or (pt[1]-last_y)>10):
                    cv2.rectangle(img_rgb, (last_x,last_y), (last_x + h, last_y + w), p[3], 2)
                    cv2.rectangle(img_rgb, pt, (pt[0] + h, pt[1] + w), p[3], 2)
                    found+=1
                    patterns.remove(p)

                    
                    
            last_x = pt[0]
            last_y = pt[1]
        threshold-=0.01
        print("end")



cv2.imwrite('result.png', img_rgb)