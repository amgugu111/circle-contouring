import numpy as np
import cv2

device =cv2.VideoCapture(0)
while True:
    _, frame = device.read()
    blurred_frame = cv2.GaussianBlur(frame, (5, 5), 0)
    gray = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2GRAY)
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 100)
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:
            cv2.circle(blurred_frame, (x, y), r, (0, 255, 0), 4)
            cv2.rectangle(blurred_frame, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
        cv2.imshow('frame', blurred_frame)
        k=cv2.waitKey(1) & 0xFF
        if k==27:
            break

device.release()
cv2.destroyAllWindows()