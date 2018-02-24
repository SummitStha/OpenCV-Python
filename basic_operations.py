import numpy as np 
import cv2

img = cv2.imread('img/new.jpg', cv2.IMREAD_COLOR)

img[70,85] = [0,0,255]
px = img[70,85]
print px

img[100:200, 100:200] = [0,0,255]

face = img[1000:1070, 1000:1200]
img[0:70, 0:200] = face

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
