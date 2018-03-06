import numpy as np
import cv2

cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture('video/people-walking.mp4')

fgmogbg = cv2.BackgroundSubtractorMOG()	# Creates a background object.
fgmog2bg = cv2.BackgroundSubtractorMOG2()	# It detects and marks shadows as well.

while True:
    ret, frame = cap.read()

    # To get the foreground mask.
    fgmogmask = fgmogbg.apply(frame)
    fgmog2mask = fgmog2bg.apply(frame)

    cv2.imshow('original',frame)
    cv2.imshow('fgmogmask',fgmogmask)
    cv2.imshow('fgmog2mask',fgmog2mask)

    
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    

cap.release()
cv2.destroyAllWindows()


# Note: For OpenCV version-3:
#	use cv2.createBackgroundSubtractorMOG() in line 5 and cv2.createBackgroundSubtractorMOG2() in line 6.