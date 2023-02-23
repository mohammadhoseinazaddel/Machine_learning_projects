#pylint:disable=no-member

import cv2 as cv
import numpy as np

park = cv.imread('Resources/Photos/park.jpg', 0)
cv.imshow('park', park)



_, mask = cv.threshold(park,150,255,cv.THRESH_BINARY)
cv.imshow('mask', mask)

#erosing حذف نویز
kernel = np.ones((3,3),np.int8)
enrodd_img = cv.erode(mask, kernel, iterations=1)
cv.imshow("enrodd_img",enrodd_img)

# delition باد میکنه
kernel = np.ones((3,3),np.int8)
delition = cv.dilate(mask, kernel, iterations=1)
cv.imshow("deli_img",delition)

# closing 
kernel = np.ones((3,3),np.int8)
closimg = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel)
cv.imshow("clos_img",closimg)

# opening 
kernel = np.ones((3,3),np.int8)
openimg = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)
cv.imshow("openimg",openimg)
 
# gradient =  orginal - delited
kernel = np.ones((3,3),np.int8)
gradient = cv.morphologyEx(mask, cv.MORPH_GRADIENT, kernel)
cv.imshow("gradient",gradient)

cv.waitKey(0)