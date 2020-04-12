# masks are binary images which indicates the pixels
# in which an operation is to be performed
import cv2
import numpy as np
img1 = np.zeros((250,500,3),np.uint8)
img1 = cv2.rectangle(img1,(200,0),(300,100),(255,255,255),-1)
img2 = np.zeros((250,500,3),np.uint8)
img2 = cv2.rectangle(img2,(249,0),(499,249),(255,255,255),-1)
# rectangle src edge1 edge2 color
# cv2.imwrite("image_1.png",img2)
bitXor=cv2.bitwise_xor(img2,img1)


cv2.imshow("image1 ",img1)
cv2.imshow("image2 ",img2)
cv2.imshow("bitAnd ",bitXor)
cv2.waitKey(0)
cv2.destroyAllWindows()