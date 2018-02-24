import cv2
import numpy as np 
import matplotlib.pyplot as plt

img = cv2.imread('img/new.jpg', cv2.IMREAD_GRAYSCALE)   #grayscale is much more good for image analysis
#IMREAD_COLOR = 1
#IMREAD_UNCHANGED = -1
#IMREAD_GRAYSCALE = 0

cv2.imshow('new_image', img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
#cv2.destroyWindow(windowname)

# plt.imshow(img, cmap='gray', interpolation='bicubic')
# plt.plot([50,100], [80,100], 'c', linewidth=5)
# plt.show()

cv2.imwrite('output/grayone.jpg', img)


# k = cv2.waitKey(0)	# for 32-bit machines
k = cv2.waitKey(0) & 0xFF	# for 64-bit machines
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('output/newgray.png',img)
    cv2.destroyAllWindows()