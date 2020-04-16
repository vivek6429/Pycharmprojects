import numpy as np
import cv2

# it is easier to use grayscale for finding contours

img = cv2.imread("data/opencv-logo.png")
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 125, 255, 0)
contours = []
a, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)  # mode , methord
# countour is a python list of all contours in image , each individual contour is numpy array
# cv2.imshow("image",a)
# print(contours)
# cv2.waitKey(0)
# print(hierarchy)
cv2.drawContours(img, contours, -1, (0, 255, 255),3)
# on_original image, contours, index =-1 implys draw allof it or any other (specify)  color,thickness
# NOW ORGINAL IMAGE HAS CONTOUR DRAWN ON IT
print("No of counters :", str(len(contours)))
cv2.imshow("image", img)
cv2.imshow("Image Gray", imgray)
cv2.waitKey(0)
cv2.destroyAllWindows()
