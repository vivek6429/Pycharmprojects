# technique used for seperation of objects from background
# comparing each pixel with a threshold values
import cv2
import numpy as np


def nothing(x):
    pass


img = cv2.imread("data/gradient.png")
cv2.imshow("image", img)
# cv2.namedWindow("controls")
cv2.createTrackbar("val", "image", 0, 255, nothing)
while True:
    img = cv2.imread("data/gradient.png")
    val = cv2.getTrackbarPos("val", "image")
    print(val)
    ret, thold = cv2.threshold(img, val, 255, cv2.THRESH_BINARY)
    ret2, thold2 = cv2.threshold(img, val, 255, cv2.THRESH_BINARY_INV)
    ret3, thold3 = cv2.threshold(img, val, 255, cv2.THRESH_TRUNC) # after the val pixels remains constant
    ret4, thold4 = cv2.threshold(img, val, 255, cv2.THRESH_TOZERO) # when pxl val < thresh hold it is assigned to zero
    ret5, thold5 = cv2.threshold(img, val, 255, cv2.THRESH_TOZERO_INV)
    # src,threshhold,maxval,type,cv2.type
    # adaptive thresholding based on regions

    
    cv2.imshow("th1 ", thold)
    cv2.imshow("th2_inv", thold2)
    cv2.imshow("th3", thold3)
    cv2.imshow("th4", thold4)
    cv2.imshow("th5", thold5)
    k = cv2.waitKey(1)
    if k == 27:
        break
cv2.destroyAllWindows()