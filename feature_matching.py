import cv2
import numpy as np 
import matplotlib.pyplot as plt

img1 = cv2.imread('img/part-image.jpg', 0)
img2 = cv2.imread('img/main-image.jpg', 0)

# ORB detector to use for the features detection.
orb = cv2.ORB_create()

# Find the key points and their descriptors with the orb detector.
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

# BFMatcher object for matching the features.
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# Create matches of the descriptors, then sort them based on their distances.
matches = bf.match(des1, des2)
matches = sorted(matches, key=lambda x:x.distance)

# Draw the first 10 matches.
img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:10], None, flags=2)
plt.imshow(img3)
plt.show()

