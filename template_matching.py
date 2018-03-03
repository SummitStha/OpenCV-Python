import cv2
import numpy as np

# Read the image from which template is to be matched and convert to grayscale
img_bgr = cv2.imread('img/cube.jpg')
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

# Read the template to be matched and its width and height is taken
template = cv2.imread('img/cube-template.jpg', 0)
w, h = template.shape[::-1]		# (width, height) of the given template 

# Match the template with matchTemplate() function and find where its result is greater than or equals to given threshold
res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.9
loc = np.where(res >= threshold)

# For every matched template in the given image, draw a rectangle around it
for pt in zip(*loc[::-1]):
	cv2.rectangle(img_bgr, pt, (pt[0]+w, pt[1]+h), (0,255,0), 2)	# (filename, top-left coordinate, bottom-right coordinate, color, thickness)

cv2.imshow('Detected', img_bgr)
cv2.imwrite('output/template-match.jpg', img_bgr)