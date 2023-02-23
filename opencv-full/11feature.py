import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


image1 = cv.imread('Resources/Photos/cats.jpg')
image2 = cv.imread('Resources/Photos/cat.jpg')
#sift
feat_sift = cv.SIFT(image1)
sift_keypoints1, descriptors1 = feat_sift.detectAndCompute(image1, None)

image_matches = cv.drawMatches(image1, sift_keypoints1)
cv.imshow("siftfeatures",image_matches)
#ORB
# feat_orb = cv.ORB_create(nfeatures=1000)


# orb_keypoints1, descriptors1 = feat_orb.detectAndCompute(image1, None)
# orb_keypoints2, descriptors2 = feat_orb.detectAndCompute(image2, None)

# bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck= True)

# matches = bf.match(descriptors1, descriptors2)

# matches = sorted(matches, key= lambda x:x.distance)

# image_matches = cv.drawMatches(image1, orb_keypoints1, image2, orb_keypoints2, matches[:100], None, flags=2)

# cv.imshow("feature",image_matches)

cv.waitKey(0)