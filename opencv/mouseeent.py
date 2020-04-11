import numpy as np
import cv2

# events= [ i for i  in dir(cv2) if 'EVENT' in i ]
# print(events)
#
# Need to create a mouse callback
windowname="The black screen" # need same window name to work @ callback and in show
def click_evnt(event,x,y,flags,param): # specific format
    location = (x, y)
    color = (255, 0, 0)  # BGR
    font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
    fontscale = 0.4
    thickness = 1
    linetype = cv2.LINE_AA

    if (event==cv2.EVENT_LBUTTONDOWN):
        print(x,"    ",y)
        text = str(x)+" "+str(y)
        cv2.putText(img, text, location, font, fontscale, color, thickness, linetype)
        cv2.imshow(windowname,img)
    if (event==cv2.EVENT_RBUTTONDOWN):
        blue= img[y,x,0]
        green = img[y, x, 1]
        red  = img[y, x, 2]
        text="Blue :"+str(blue)+"Green :"+str(green)+"Red :"+str(red)
        cv2.putText(img, text, location, font, fontscale, color, thickness, linetype)
        cv2.imshow(windowname, img)




img=cv2.imread("data/image.jpg")
cv2.imshow(windowname,img)
cv2.setMouseCallback(windowname,click_evnt)
cv2.waitKey(0)
cv2.destroyAllWindows()