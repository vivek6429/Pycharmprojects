import cv2
import numpy as np


def fun(x):
    print("x ===" + str(x))
    pass




cv2.namedWindow("window")
cv2.createTrackbar("Bar", "window", 0, 255, fun)
switch = "0 bgr \n 1 greyscale"
cv2.createTrackbar(switch, "window", 0, 1, fun)
location = (50, 200)
font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
fontscale = 1
color = (255, 255, 255)
thickness = 1
linetype = cv2.LINE_AA
while True:
    img = cv2.imread("data/lena.jpg")
    s = cv2.getTrackbarPos(switch, "window")
    pos = cv2.getTrackbarPos("Bar", "window")
    frame = cv2.putText(img, str(pos), location, font, fontscale, color, thickness, linetype)
    if s == 1:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("window",img)
    k=cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
