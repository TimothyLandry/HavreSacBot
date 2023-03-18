import numpy as np
import cv2 as cv
from time import sleep

img = cv.imread('test.png')
assert img is not None, "file could not be read, check with os.path.exists()"

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(gray, 127,255,cv.THRESH_BINARY)



kernel = np.ones((3, 3), np.uint8)
img_erosion = cv.erode(thresh, kernel, iterations=2)
cv.imwrite('DEBUG.png', img_erosion)
# img_dilation = cv.dilate(img_erosion, kernel, iterations=1)
# cv.imwrite('DEBUG.png', img_dilation)

# contours, hierarchy = cv.findContours(img_dilation, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

# for c in contours:
#     img_dilation = cv.drawContours(img, [c], 0, (0,255,0), 3)

# cv.imwrite('DEBUG.png', img)