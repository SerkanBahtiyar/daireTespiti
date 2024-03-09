#daire tespiti

import cv2  as cv
import numpy as np

src = cv.imread("b.png")
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
gray = cv.GaussianBlur(gray, (9, 9), 2, 2)

circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, dp=1, minDist=10, param1=100, param2=50,
                          minRadius=20, maxRadius=100)

if circles is not None:
    circles = np.uint16(np.around(circles))
    for c in circles[0, :]:
        cx, cy, r = c
        cv.circle(src, (cx, cy), 2, (0, 255, 0), 2, 8, 0)
        cv.circle(src, (cx, cy), r, (0, 0, 255), 2, 8, 0)

cv.imshow("cikis", src)
cv.waitKey(0)