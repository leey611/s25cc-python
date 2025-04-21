import numpy as np
import cv2

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        face_roi = frame[y:y+h, x:x+w]

        # shuffle pixels in the face region
        shuffled = face_roi.reshape(-1, 3)
        np.random.shuffle(shuffled)
        shuffled = shuffled.reshape(face_roi.shape)

        # replace the face with the shuffled version
        frame[y:y+h, x:x+w] = shuffled

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
