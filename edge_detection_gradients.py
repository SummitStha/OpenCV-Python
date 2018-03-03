import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:

    # Take each frame
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_red = np.array([30,150,50])
    upper_red = np.array([255,255,180])
    
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask= mask)

    # Laplician is a gradient that goes both ways, i.e. both towards "x" and "y"
    laplacian = cv2.Laplacian(frame, cv2.CV_64F)	# cv2.CV_64F is the data type
    
    # Sobel is used to get directional intensity with gradients.
    sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)	# (frame, data-type, x, y, kernel-size)
    sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)	# (frame, data-type, x, y, kernel-size)

    # Canny Edge detection can be used to convert these gradients to pure edges.
    edges = cv2.Canny(frame,100,200)

    cv2.imshow('original',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('laplacian',laplacian)
    cv2.imshow('sobelx',sobelx)
    cv2.imshow('sobely',sobely)
    cv2.imshow('edges',edges)


    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()