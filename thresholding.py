# Simplification of an image, by making everything as a 0 or 1/white or black.

import cv2
import numpy as np 

img = cv2.imread('img/bookpage.jpg')
ret, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)		# (image, threshold, maximum-value, threshold-type)

# Grayscale the image, and then do a threshold
grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret2, binary = cv2.threshold(grayscale, 12, 255, cv2.THRESH_BINARY)

# Using Gaussian Adaptive and Otsu's Thresholds
gaus = cv2.adaptiveThreshold(grayscale, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)		# (image, maximum-value, adaptive-threshold-type, binary-type, threshold)
ret3, otsu = cv2.threshold(grayscale, 125, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)		# (image, threshold, maximum-value, threshold-type)

cv2.imshow('original', img)
cv2.imshow('threshold', threshold)
cv2.imshow('binary threshold', binary)
cv2.imshow('gaus', gaus)
cv2.imshow('otsu', otsu)
cv2.waitKey(0)
cv2.destroyAllWindows()