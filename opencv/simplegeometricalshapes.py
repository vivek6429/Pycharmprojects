import numpy as np
import cv2

img = cv2.imread('data/shapes.png')
imggrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(imggrey, 240, 255, cv2.THRESH_BINARY)
_, contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
for contour in contours:
    approx = cv2.approxPolyDP(contour, .01 * cv2.arcLength(contour, closed=True), closed=True)  #
    # conntour ,approximates polygonal( curves) with a specifi precision epsilon specifys parameter accuracy , closed ?
    cv2.drawContours(img, [approx], 0, (0, 0, 0), 5)
    # [approx] notation which also specify no of contour therefore index always 0
    # find x and y to print shpe in charachter
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 10
    if len(approx) == 3:
        cv2.putText(img, "Triangle", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 4:
        x1, y1, w, h = cv2.boundingRect(approx)
        aspectRatio = float(w / h)
        print(aspectRatio)
        if 1.05 >= aspectRatio >= 0.95:  # not an ideal noise , give a room for error dammit
            cv2.putText(img, "square", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
        else:
            cv2.putText(img, "rectangle", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 5:
        cv2.putText(img, "pentagon", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 10:
        cv2.putText(img, "star", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
    else:
        cv2.putText(img, "circle", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))

cv2.imshow("Shapes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
