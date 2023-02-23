import cv2 as cv
import numpy as np


import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Resources/Photos/park.jpg')
# cv.imshow('Park', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

# Sobel 
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)
cv.imshow('Combined Sobel', combined_sobel)

# canny
canny = cv.Canny(gray, 150, 175)
cv.imshow('Canny', canny)




# image = cv.imread('Resources/Photos/Road_in_Norway.jpg', 0)
# image_noise_removed = cv.GaussianBlur(image, (3,3),0)
# cv.imshow("f",image)
# # Laplacian
# laplacian = cv.Laplacian(image_noise_removed, cv.CV_64F)
# cv.imshow("laplacian",laplacian)

# # sobelx
# sobelx= cv.Sobel(image_noise_removed, cv.CV_64F, 1, 0, ksize=5)
# cv.imshow("sobelx",sobelx)

# # sobely
# sobely= cv.Sobel(image_noise_removed, cv.CV_64F, 0, 1, ksize=5)
# cv.imshow("sobely",sobely)


# # Canny Edge Detection
# canny = cv.Canny(image_noise_removed, 100, 200)


# """
# plt.subplot(1,2,1),plt.imshow(image,cmap = 'gray')
# plt.title('Original'), plt.xticks([]), plt.yticks([])
# plt.subplot(1,2,2),plt.imshow(canny,cmap = 'gray')
# plt.title('Canny'), plt.xticks([]), plt.yticks([])
# plt.show()
# """
# plt.subplot(2,2,1),plt.imshow(image,cmap = 'gray')
# plt.title('Original'), plt.xticks([]), plt.yticks([])
# plt.subplot(2,2,2),plt.imshow(canny,cmap = 'gray')
# plt.title('Canny'), plt.xticks([]), plt.yticks([])
# plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
# plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
# plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
# plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

# plt.show()


cv.waitKey(0)