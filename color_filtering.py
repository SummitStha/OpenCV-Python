import cv2
import numpy as np 

cap = cv2.VideoCapture(0)

# Hue Saturation Value
while True:
	_, frame = cap.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)	#  convert the frames to HSV

	# HSV values for the color
	lower_red = np.array([150,150,10])
	upper_red = np.array([180, 255, 255])

	mask = cv2.inRange(hsv, lower_red, upper_red)	# Create mask, which uses an "inRange" statement, for specific range. 
	res = cv2.bitwise_and(frame, frame, mask=mask)	# Show color where there is the frame AND the mask. 

	# Apply a simple smoothing, where we do a sort of averaging per block of pixels, here a 15 x 15 square
	kernel = np.ones((15,15), np.float32)/225
	smoothed = cv2.filter2D(res, -1, kernel)

	# Gaussian Blur
	blur = cv2.GaussianBlur(res, (15,15), 0)

	# Median Blur
	median = cv2.medianBlur(res, 15)

	# Bilateral Filter
	bilateral = cv2.bilateralFilter(res, 15, 75, 75)

	cv2.imshow('frame', frame)
	cv2.imshow('mask', mask)
	cv2.imshow('res', res)
	cv2.imshow('smoothed', smoothed)
	cv2.imshow('blur', blur)
	cv2.imshow('median', median)
	cv2.imshow('bilateral', bilateral)
	
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break

cv2.destroyAllWindows()
cap.release()
