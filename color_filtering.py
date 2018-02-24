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

	cv2.imshow('frame', frame)
	cv2.imshow('mask', mask)
	cv2.imshow('res', res)
	
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break

cv2.destroyAllWindows()
cap.release()
