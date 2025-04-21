import cv2 # pip install opencv-python

test_img = cv2.imread('obama.jpg')

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
faces_rects = face_cascade.detectMultiScale(test_img, scaleFactor = 1.2, minNeighbors = 2)


for (x,y,w,h) in faces_rects:
     cv2.rectangle(test_img, (x, y), (x+w, y+h), (190, 105, 220), 5)

cv2.imshow('my image', test_img)
cv2.waitKey(0)
cv2.destroyAllWindows()