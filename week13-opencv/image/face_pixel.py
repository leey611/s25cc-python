# create a venv
import cv2 # pip install opencv-python
import numpy as np

test_img = cv2.imread('obama.jpg')

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
faces_rects = face_cascade.detectMultiScale(test_img, scaleFactor = 1.2, minNeighbors = 2)

img_copy = test_img.copy()
 
for (x, y, w, h) in faces_rects:
    cv2.rectangle(img_copy, (x, y), (x+w, y+h), 2)

    # select the face region
    rect_color = img_copy[y:y+h, x:x+w]

    # reshape to 2D array of pixels
    shuffled = rect_color.reshape(-1, 3) # 3->rgb channel
    np.random.shuffle(shuffled)

    # reshape back to original shape
    shuffled = shuffled.reshape(rect_color.shape)

    # insert back into image
    img_copy[y:y+h, x:x+w] = shuffled

# cv2.imshow('my image', test_img)
cv2.imshow('my image', img_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()