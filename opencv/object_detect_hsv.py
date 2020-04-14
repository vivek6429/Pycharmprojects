import cv2
import numpy as np


def callback(x):
    pass

cap = cv2.VideoCapture(0)
cv2.namedWindow("Tracking")
cv2.createTrackbar("LH", "Tracking", 0, 255, callback)
cv2.createTrackbar("LS", "Tracking", 0, 255, callback)
cv2.createTrackbar("LV", "Tracking", 0, 255, callback)
cv2.createTrackbar("UH", "Tracking", 255, 255, callback)
cv2.createTrackbar("US", "Tracking", 255, 255, callback)
cv2.createTrackbar("UV", "Tracking", 255, 255, callback)
while True:
    ret , frame =cap.read() # read from camera
    if ret == False:
        print("Camera read error ")  # filsafe
        break
    
    LH = cv2.getTrackbarPos("LH", "Tracking")
    LS = cv2.getTrackbarPos("LS", "Tracking")
    LV = cv2.getTrackbarPos("LV", "Tracking")
    UH = cv2.getTrackbarPos("UH", "Tracking")
    US = cv2.getTrackbarPos("US", "Tracking")
    UV = cv2.getTrackbarPos("UV", "Tracking")

    # frame = cv2.imread("data/smarties.png")
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    l_b = np.array([LH, LS, LV])  # lower blue
    u_b = np.array([UH, US, UV])  # upper limit
    mask = cv2.inRange(hsv, l_b, u_b)
    res = cv2.bitwise_and(frame, frame, mask=mask)  # colored framesource1 , source2,mask

    cv2.imshow("image", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res ", res)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
