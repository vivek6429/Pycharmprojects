import numpy as np
import cv2
def function(x):
    print(x)
    pass
img=np.zeros((300,512,3),np.uint8)
cv2.namedWindow('image') # simply a window with a name
cv2.createTrackbar("B",'image',0,255,function)# trackbarname imagewindowname initialval final callback
cv2.createTrackbar("G",'image',0,255,function)
cv2.createTrackbar("R",'image',0,255,function)
switch =' 0 : OFF\n 1 : ON'
cv2.createTrackbar(switch,'image',0,1,function)
while True:
    cv2.imshow('image',img) # loading the image onto the named window
    k=cv2.waitKey(1) & 0xFF
    if k == 27:# esc
        break
    b = cv2.getTrackbarPos("B", 'image')
    g = cv2.getTrackbarPos("G", 'image')
    r = cv2.getTrackbarPos("R", 'image')
    s = cv2.getTrackbarPos(switch, 'image')
    if s == 0:
        img[:]=0
    else:
        img[:] = [b, g, r]



b=cv2.getTrackbarPos("B",'image')

print(b)
cv2.destroyAllWindows()