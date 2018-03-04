import cv2
import numpy as np

img = cv2.imread('img/corner-detection.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)		# Conversion to float32

corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)		#(image,  max-corners-to-detect, quality, minimum-distance-between-corners)
corners = np.int0(corners)		# Conversion to int0

# Iterate through each corner, making a circle at each point which is a corner.
for corner in corners:
	x, y = corner.ravel()
	cv2.circle(img, (x,y), 3, 255, -1)

cv2.imshow('corners', img)
cv2.imwrite('output/corners.jpg', img)
