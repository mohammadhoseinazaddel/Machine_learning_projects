#pylint:disable=no-member

import cv2 as cv
# from mathpo
# img = cv.imread('../Resources/Photos/cats.jpg')
# cv.imshow('Cats', img)

img_gray = cv.imread('Resources/Photos/cats.jpg', cv.IMREAD_GRAYSCALE)
cv.imshow('Catgray', img_gray)

img_color = cv.imread('Resources/Photos/cats.jpg', cv.IMREAD_COLOR)
cv.imshow('Catscolorage', img_color)

img_gray_2 = cv.imread('Resources/Photos/cats.jpg', cv.IMREAD_REDUCED_GRAYSCALE_4)
cv.imshow('Catsgray2', img_gray_2)

print(cv.IMREAD_COLOR) # 1
print(cv.IMREAD_GRAYSCALE) # 0
print(cv.IMREAD_REDUCED_GRAYSCALE_4) # 16 32
print(cv.IMREAD_UNCHANGED) # -1
# cv.waitKey(3000)
cv.waitKey(0)

# RGB(255,255,255)
# BGR
# RGBA BGRA
# Reading Videos

# save image 
img_gray_2 = cv.imwrite('/kkd/catscolor.jpg', img_color) # error nemide

img_gray_2 = cv.imwrite('catscolor.jpg', img_color) # error nemide



# capture = cv.VideoCapture('../Resources/Videos/dog.mp4')

# while True:
#     isTrue, frame = capture.read()
    
#     # if cv.waitKey(20) & 0xFF==ord('d'):
#     # This is the preferred way - if `isTrue` is false (the frame could 
#     # not be read, or we're at the end of the video), we immediately
#     # break from the loop. 
#     if isTrue:    
#         cv.imshow('Video', frame)
#         if cv.waitKey(20) & 0xFF==ord('d'):
#             break            
#     else:
#         break

# capture.release()
cv.destroyAllWindows()
