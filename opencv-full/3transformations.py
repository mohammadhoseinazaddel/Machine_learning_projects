#pylint:disable=no-member

import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('Park', img)

# Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

# translated = translate(img, -100, 100)
# cv.imshow('Translated', translated)

# Rotation
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]
    # print(img.shape)
    # print(height)
    # print(width)

    if rotPoint is None:
        rotPoint = (width//2,height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    print(rotMat)
    dimensions = (width,height)

    return cv.warpAffine(img, rotMat, dimensions)

# rotated = rotate(img, -45)
# cv.imshow('Rotated', rotated)

# rotated_rotated = rotate(img, -90)
# cv.imshow('Rotated Rotated', rotated_rotated)

# Resizing
# INTER_NEAREST – a nearest-neighbor interpolation
# INTER_LINEAR – a bilinear interpolation (used by default)
# INTER_AREA – resampling using pixel area relation. It may be a preferred method for image decimation, as it gives moire’-free results. But when the image is zoomed, it is similar to the INTER_NEAREST method.
# INTER_CUBIC – a bicubic interpolation over 4×4 pixel neighborhood
# INTER_LANCZOS4 – a Lanczos interpolation over 8×8 pixel neighborhood

# # shrinking
# # INTER_AREA
# resized = cv.resize(img, (100,100), interpolation=cv.INTER_AREA)
# cv.imshow('Resized', resized)

# # enlarging
# # INTER_LINEAR
# # INTER_CUBIC
# resized = cv.resize(img, (1000,1000), interpolation=cv.INTER_CUBIC)
# cv.imshow('Resizedint', resized)

# Flipping
flip = cv.flip(img, -1)
# Vertical flipping of the image (flipCode == 0) 
cv.imshow('Flip', flip)

# # Cropping
# cropped = img[200:400, 300:400]
# cv.imshow('Cropped', cropped)


cv.waitKey(0)