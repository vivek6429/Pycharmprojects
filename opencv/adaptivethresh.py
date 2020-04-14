
import cv2
import numpy as np


def nothing(x):
    pass


img = cv2.imread("data/sudoku.png",0)

# cv2.namedWindow("controls")
cv2.createTrackbar("val", "image", 0, 255, nothing)
while True:
    # img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    th2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
    th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    # max value non zero val applied when condition is satisfied
    # adoptive methord 2 tpes
    # ADAPTIVE_THRESH_MEAN_C ----- gives mean in neighbhourhood
    # ADAPTIVE_THRESH_GAUSSIAN_C --- weighted sum of neighbhor hood, weight is gaussian window
    # Threshhold type
    # Blocksize defines size of neighbhour hood area
    # just a constant c subtracted from mean
    # adaptive thresholding based on regions

    cv2.imshow("image", img)

    cv2.imshow("th2", th2)
    cv2.imshow("th3", th3)

    k = cv2.waitKey(1)
    if k == 27:
        break
cv2.destroyAllWindows()