import cv2
import numpy as np

img=np.zeros([512,512,3],np.uint8)
# img = cv2.imread("data/lena.jpg", 1)
img = cv2.line(img, (0, 0), (255, 255), (255, 0, 0), 5)  # img pt1 pt2 colorbgr thickness1-
img = cv2.arrowedLine(img, (0, 0), (255, 0), (255, 0, 0), 5)
img = cv2.rectangle(img, (0, 0), (255, 255), (255, 0, 0), -1)  # -1 THICKNES for filling
img = cv2.circle(img, (500, 500), 25, (0, 255, 255), -1)
font = cv2.FONT_HERSHEY_COMPLEX

img = cv2.putText(img, "Hello_world", (10, 500), font, 2, (255, 255, 0), 5, cv2.LINE_AA)
# img,text,locat,font,fontsize,color,thicknes,line
cv2.imshow("image", img)

k = cv2.waitKey(0) & 0xFF  # use the mask in 64 bit machine if error

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('copy.png', img)
