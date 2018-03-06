import cv2
import numpy as np

# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades

# Loading in the face and eye cascades.
#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
eye_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')
#https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_smile.xml
smile_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_smile.xml')

cap = cv2.VideoCapture(0)
#img = cv2.imread('img/fg-extraction.jpg')

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # detectMultiScale detects objects of different sizes in the input image. The detected objects are returned as a list of rectangles.
    # Here it is used to detect the faces.
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Find faces, their sizes, draw rectangles, and note the ROI.
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)  # draws rectangle. (image, startpoint, endpoint, color, thickness)
        roi_gray = gray[y:y+h, x:x+w]   # region of image where faces are detected in the grayscale image.
        roi_color = img[y:y+h, x:x+w]   # region of image where faces are detected in the color image.
        
        # Find the eyes in the detected faces region and draw rectangle around it.
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

        # Find the smile in the detected faces region and draw rectangle around it as well.
        smile = smile_cascade.detectMultiScale(roi_gray)
        for (sx, sy, sw, sh) in smile:
            cv2.rectangle(roi_color,(sx,sy),(sx+sw,sy+sh),(0,0,255),2)

    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()