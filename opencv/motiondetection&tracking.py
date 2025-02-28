#
#
import cv2
import numpy as np

# cap = cv2.VideoCapture("data/vtest.avi")
cap = cv2.VideoCapture(0)
ret, frame1 = cap.read()
ret, frame2 = cap.read()
# diff = cv2.absdiff(frame1,frame2)
# cv2.imshow("aaa",frame1)
# cv2.imshow("55",frame2)
# cv2.imshow("diff",diff)
# cv2.waitKey(0)
while cap.isOpened():
    diff = cv2.absdiff(frame1, frame2)
    # cv2.imshow("diff",diff)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)  # to find contours in later stage
    # cv2.imshow("diffgray", gray)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    # cv2.imshow("diffgrayblur", blur)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    # cv2.imshow("thresh", thresh)
    # dilate the threshholded image to fill the holes  helps IN FINDING BETTER CONTOURS
    dilated = cv2.dilate(thresh, None, iterations=3)
    # cv2.imshow("dilated", dilated)
    img, contours, heirar = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)  ## need only contours
    # cv2.drawContours(frame1,contours,-1,(0,255,0),2) no need of contours need to draw rectangle
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)  # x,y x+w,y+h gives 2 points to draw rectangle
        ##### check AREA FOR FILTER
        if cv2.contourArea(contour) < 900:
            continue
        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame1, "Status:{}".format('Movement'), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 3)

    # cv2.drawContours(frame1,contours,-1,(0,255,0),2) no need of contours need to draw rectangle

    cv2.imshow("feed", frame1)
    frame1 = frame2
    ret, frame2 = cap.read()

    if cv2.waitKey(40) == 27:
        break
cap.release()
cv2.destroyAllWindows()
