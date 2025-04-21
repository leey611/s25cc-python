import numpy as np
import cv2

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        # get circle x,y
        center_x = x + w // 2
        center_y = y + h // 2
        radius = max(w, h) // 2
        cv2.circle(frame, (center_x, center_y), radius, (0, 255, 255), 3) 

        # eyes' region of interest 
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            eye_center = (ex + ew // 2, ey + eh // 2)
            eye_radius = max(ew, eh) // 3
            cv2.circle(roi_color, eye_center, eye_radius, (255, 0, 0), 2) 

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
