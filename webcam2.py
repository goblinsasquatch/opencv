import cv2
from cv2 import VideoCapture
import numpy as np
cap = VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    img = cv2.line(frame, (0, height//2,), (width, height//2), (255, 0, 0), 10)
    img = cv2.rectangle(img, (100, 100), (200, 200), (0, 0, 255), 5)
    img = cv2.circle(img, (width//2, height//2), 60, (0, 255, 0), -1)
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(img, 'test text', (100, height-50),
                      font, 2,  (0, 255, 255), 5, cv2.LINE_AA)

    cv2.imshow('frame', img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
