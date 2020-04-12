import numpy as np
import cv2

# events= [ i for i  in dir(cv2) if 'EVENT' in i ]
# print(events)
#
# Need to create a mouse callback
windowname = "The black screen"  # need same window name to work @ callback and in show


def click_evnt(event, x, y, flags, param):  # specific format
    blue = img[y, x, 0]
    green = img[y, x, 1]
    red = img[y, x, 2]
    text = "Blue :" + str(blue) + "Green :" + str(green) + "Red :" + str(red)
    location = (x, y)
    color = (255, 0, 0)  # BGR
    font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
    fontscale = 0.4
    thickness = 1  # -1 to fill
    linetype = cv2.LINE_8

    if (event == cv2.EVENT_LBUTTONDOWN):
        print(x, "    ", y)
        cv2.circle(img, location, 16, color, thickness, linetype)
        points.append(location)
        mycolorimage=np.zeros((512,512,3),np.uint8)
        mycolorimage[:]=[blue,green,red]

        if len(points) >= 2 :
            cv2.line(img,points[-2],points[-1],color,thickness,linetype)
            # points.clear()
    cv2.imshow("color", mycolorimage)
    cv2.imshow(windowname, img)


img = cv2.imread("data/lena.jpg")
cv2.imshow(windowname, img)
points = []
cv2.setMouseCallback(windowname, click_evnt)
cv2.waitKey(0)
cv2.destroyAllWindows()
