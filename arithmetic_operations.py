import cv2
import numpy as np 

img1 = cv2.imread('img/plot.png')
img2 = cv2.imread('img/main.png')
#img1 and img2 are of the same size
img3 = cv2.imread('img/logo.png')


# Image Addition
# add = img1 + img2
add = cv2.add(img1, img2)	# added all of the pixels values together


# Image Blending
weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)		# (filename1, weight1, filename2, weight2, gamma-value)


# Bitwise Operation
rows, cols, channels = img3.shape
roi = img1[0:rows, 0:cols]	# Put img3 on top-left corner of img1, So created a ROI

img2gray = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)	# Add a threshold. (image, threshold-value, maximum-value, binary-threshold-inverse)
mask_inv = cv2.bitwise_not(mask)	# Invisible part or the black area of the mask
img3_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)	# Black-out the area of logo in ROI
img3_fg = cv2.bitwise_and(img3, img3, mask=mask)	# Take only region of logo from logo image.

# Put img3 logo in ROI and modify the img1
dst = cv2.add(img3_bg, img3_fg)
img1[0:rows, 0:cols] = dst


cv2.imshow('add', add)
cv2.imshow('weighted', weighted)
cv2.imshow('mask', mask)
cv2.imshow('mask_inv', mask_inv)
cv2.imshow('img1_bg', img3_bg)
cv2.imshow('img3_fg', img3_fg)
cv2.imshow('dst', dst)
cv2.imshow('res', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
