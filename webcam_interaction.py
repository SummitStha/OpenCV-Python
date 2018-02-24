#Interacting with an webcam or video feed with opencv

import cv2

cap = cv2.VideoCapture(0)  # to use the 1st webcam in the system

# Define the codec and create VideoWriter object
fourcc = cv2.cv.CV_FOURCC(*'XVID')   # codec of the video we want (i.e. XVID for this one)
out = cv2.VideoWriter('output/output.avi', fourcc, 20.0, (640,480))  # output will be the (filename, codec, number of frames per second (fps), frame size)

print cap.isOpened() # checks whether cap has initialized the capture
#cap.open()	# if cap is not open then use this method to open the cap
# print cap.read()

while cap.isOpened():
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # converting color of frame to gray
	out.write(frame)
	cv2.imshow('frame', frame)
	cv2.imshow('gray', gray)  # showing the gray frame

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

	if ret==True:
		flipped = cv2.flip(frame,0)
		# write the flipped frame
		out.write(flipped)

		cv2.imshow('flipped',flipped)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	else:
		break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()


# Dependencies
# change cv2.cv.CV_FOURCC(*'XVID') to cv2.VideoWriter_fourcc(*'XVID') in line 8 if using opencv3