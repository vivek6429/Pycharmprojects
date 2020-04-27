# hough transform is a technique to detect shape
# if the shape can be expressed mathematically
# it can detect the shape even if it is broken or distorted
#
# for pixels in lines
# y= mx+c
# r=xcos{theta}+ysin{theta} // y=(r-xcos{theta})/sin{theta}
#
#  in hough
#  it is m,c
#  it is r,{theta}
#
#
#
# reverse also possible
# points to lines y becomes intercept mc becomes slope=-x
#
# 4 points in straight line can be represented as 4 lines intercecting at the
# points expressing mc  of line
#
# refer the png files
#
####
# open cv implements two type of hough transform
# standard transform and probablistic hough line
# HoughLines and HoughLinesP

import cv2
import numpy as np

img = cv2.imread("data/sudoku.png")
img_grey = cv2.imread("data/sudoku.png", 0)
edges = cv2.Canny(img_grey, 50, 150, apertureSize=3)  #
cv2.imshow("canny",edges)

#
lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)  #
# image,
# resolutions , threshold

for line in lines:
    rho, theta = line[0]  # rho is distance from coordinate 0,0 (top left corner)
    # theta is angle in rads
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho  # gives origin of image
    y0 = b * rho  # 0 ,0 location top left
    print("xo  :", x0, " yo  :", y0)
    # we need lines
    # X=Rcos{theta}-1000Sin{theta}
    # Y=RSIN{theta}+1000COS{theta}
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    # X=Rcos{theta}+1000Sin{theta}
    # Y=RSIN{theta}-1000COS{theta}
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))
    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

cv2.imshow("image",img)
k=cv2.waitKey(0)
cv2.destroyAllWindows()
