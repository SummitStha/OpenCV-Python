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

	kernel = np.ones((5,5),np.uint8)

	#  Erosion is where we will erode the edges.  If all of the pixels are white, then we get white, otherwise black.
	erosion = cv2.erode(mask, kernel, iterations = 1)
	# In dilation, if the entire area isn't black, then it is converted to white. 
	dilation = cv2.dilate(mask, kernel, iterations = 1)

	# Opening removes false positives i.e. the background noise.
	opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
	# Closing removes false negatives i.e. you have your detected shape, and yet you still have some black pixels within the object then it clears that up.
	closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

	cv2.imshow('frame', frame)
	cv2.imshow('mask', mask)
	cv2.imshow('Erosion',erosion)
	cv2.imshow('Dilation',dilation)
	cv2.imshow('Opening',opening)
	cv2.imshow('Closing',closing)
	
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break

cv2.destroyAllWindows()
cap.release()
