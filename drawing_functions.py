import numpy as np
import cv2

# Create a black image
# img = np.zeros((512,512,3), np.uint8)

img = cv2.imread('new.jpg', cv2.IMREAD_COLOR)

# for line
cv2.line(img, (0,0), (150,150), (255,255,255), 15)	# (filename, startpoint, endpoint, color, thickness)

# for rectangle
cv2.rectangle(img, (15,25), (200,150), (0,255,0), 5)	# (filename, top-left coordinate, bottom-right coordinate, color, thickness)

# for circle
cv2.circle(img, (100,63), 55, (0,0,255), -1)	# (filename, center, radius, color, fill-in)

# for ellipse
cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)	# (filename, center, axes lengths, angle, startAngle, endAngle, color, fill-in)

# for polygone
pts = np.array([[10,5], [20,30], [70,20], [50,10]], np.int32)	# (vertices coordinates, int32 datatype)
# pts = pts.reshape((-1,1,2))	# for reshaping the array to ROWSx1x2 
cv2.polylines(img, [pts], True, (0,255,255), 3)		# (filename, points, closed, color, thickness)

font = cv2.FONT_HERSHEY_SIMPLEX	
cv2.putText(img, 'HELLO OPEN CV!!', (0,130), font, 1, (200,255,255), 2, cv2.CV_AA)	# (filename, text, startpoint, font, fontsize, color, thickness, linetype)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Dependencies
# change cv2.CV_AA to cv2.LINE_AA in line 17 if using opencv3