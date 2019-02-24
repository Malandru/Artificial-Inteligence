import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while cv2.waitKey(1) != 27:
    ret, frame = cap.read()
    print frame.dtype
    cv2.imshow('Camera', frame)

cap.release()
cv2.destroyAllWindows()
