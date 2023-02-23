# import cv2 as cv
# import numpy as np
# from matplotlib import pyplot as plt

# image = cv.imread('Resources/Photos/cats.jpg', 0)
# img_hist= cv.calcHist([image], [0],None,[256], [0,256])
# equalized_histogram = cv.equalizeHist(image)
# img_equal_hist= cv.calcHist([equalized_histogram], [0],None,[256], [0,256])

# clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
# cl1 = clahe.apply(image)
# cl_equal_hist= cv.calcHist([cl1], [0],None,[256], [0,256])


# plt.subplot(231), plt.imshow(image, 'gray')
# plt.subplot(234), plt.plot(img_hist)
# plt.subplot(232), plt.imshow(equalized_histogram, 'gray')
# plt.subplot(235), plt.plot(img_equal_hist)
# plt.subplot(233), plt.imshow(cl1, 'gray')
# plt.subplot(236), plt.plot(cl_equal_hist)
# plt.show()

#pylint:disable=no-member

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

mask = cv.circle(blank, (img.shape[1]//2,img.shape[0]//2), 100, 255, -1)

masked = cv.bitwise_and(img,img,mask=mask)
cv.imshow('Mask', masked)

# GRayscale histogram
# gray_hist = cv.calcHist([gray], [0], mask, [256], [0,256] )

# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

# Colour Histogram

plt.figure()
plt.title('Colour Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors = ('b', 'g', 'r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i], mask, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])

plt.show()

cv.waitKey(0)