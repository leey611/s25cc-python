# reference: https://levelup.gitconnected.com/face-detection-with-python-using-opencv-5c27e521c19a
import cv2 # pip install opencv-python

test_img = cv2.imread('obama.jpg')

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
faces_rects = face_cascade.detectMultiScale(test_img, scaleFactor = 1.2, minNeighbors = 2)

img_copy = test_img.copy()

for (x, y, w, h) in faces_rects:
    cv2.rectangle(img_copy, (x, y), (x+w, y+h), 2)
    # select the areas where the face was found
    rect_color = img_copy[y:y+h, x:x+w]
    # blur the colored image
    blur = cv2.GaussianBlur(rect_color, (101,101), 0)        
    img_copy[y:y+h, x:x+w] = blur   

# cv2.imwrite('new_img.jpg', img_copy) # save image

cv2.imshow('my image', img_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()