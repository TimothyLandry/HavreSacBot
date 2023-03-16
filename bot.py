import cv2
from PIL import ImageGrab

from functions.findMatch import findMatch

#cap = ImageGrab.grab(bbox =(x1, y1, x2, y2))
#cap.save('debug.jpg')


patterns = [
    # [name, path, threshold, color]
    ["one","./patterns/one.png"],
    ["two","./patterns/two.png"],
    ["three","./patterns/three.png"],
    ["four","./patterns/four.png"],
    ["five","./patterns/five.png"],
    ["six","./patterns/six.png"],
    ["seven","./patterns/seven.png"],
    ["eight","./patterns/eight.png"],
]

img_rgb = cv2.imread('./captures/full_cap2.png')

matchs = []
while len(matchs)<3:
    if(len(matchs) == 0):
        color = (0,0,0) # noir
    elif(len(matchs)==1):
        color = (0,255,0) # vert
    else:
        color = (255,255,255) # blanc

    m = findMatch(img_rgb, patterns)
    matchs.append(m)
    patterns.pop(m[0])
    cv2.rectangle(img_rgb, (m[1][0],m[1][1]), (m[1][0] + 25, m[1][1] + 25), color, 2)
    cv2.rectangle(img_rgb, (m[2][0],m[2][1]), (m[2][0] + 25, m[2][1] + 25), color, 2)


    
w, h = img_rgb.shape[:-1]
cv2.line(img_rgb,(0,w),(h,0), (255,255,255), 2)





                    
                    



cv2.imwrite('result.png', img_rgb)