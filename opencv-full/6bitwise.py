#pylint:disable=no-member

import cv2 as cv
import numpy as np

lady = cv.imread('Resources/Photos/lady.jpg')
cv.imshow('lady', lady)

group = cv.imread('Resources/Photos/group 2.jpg')
cv.imshow('group', group)

# join = lady + group
# cv.imshow('join', join)

# join = cv.resize(group, [828,640]) + cv.resize(lady, [828,640])
# cv.imshow('join', join)

group_rs = cv.resize(group, [828,640])
lady_rs = cv.resize(lady, [828,640])
# join = cv.add(group_rs,lady_rs)
# cv.imshow('join', join)

# join = cv.addWeighted(group_rs,.8,lady_rs,.4,0)
# cv.imshow('join', join)

group2gray = cv.cvtColor(group_rs, cv.COLOR_BGR2GRAY)

ret, mask = cv.threshold(group2gray,150,255,cv.THRESH_BINARY)
cv.imshow("mask", mask)
mask_inverse = cv.bitwise_not(mask)
cv.imshow("invmask", mask_inverse)

bitwise_and_image = cv.bitwise_and(group,group,mask=mask)
cv.imshow("bitand",bitwise_and_image)

# blank = np.zeros((400,400), dtype='uint8')

# rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
# circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

# cv.imshow('Rectangle', rectangle)
# cv.imshow('Circle', circle)

# # bitwise AND --> intersecting regions
# bitwise_and = cv.bitwise_and(rectangle, circle)
# cv.imshow('Bitwise AND', bitwise_and)

# # bitwise OR --> non-intersecting and intersecting regions
# bitwise_or = cv.bitwise_or(rectangle, circle)
# cv.imshow('Bitwise OR', bitwise_or)

# # bitwise XOR --> non-intersecting regions
# bitwise_xor = cv.bitwise_xor(rectangle, circle)
# cv.imshow('Bitwise XOR', bitwise_xor)

# # bitwise NOT
# bitwise_not = cv.bitwise_not(circle)
# cv.imshow('Circle NOT', bitwise_not)

cv.waitKey(0)