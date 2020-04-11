import cv2
import numpy_image as np

# img = cv2.imread("data/lena.jpg", 1)
cap = cv2.VideoCapture(0)
font=cv2.FONT_HERSHEY_SCRIPT_COMPLEX
while (cap.isOpened()):
    ret, frame = cap.read()

    if ret == True:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) #3
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # get prop id

        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        text="width :" + str(cap.get(3)) + "Height :" + str(cap.get(4))
        color=(255,0,0)#BGR
        fontscale=1
        thickness=2
        linetype=cv2.LINE_AA
        frame=cv2.putText(frame,text,(10,50),font,fontscale,color,thickness,linetype)
        cv2.imshow('camera', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()  # important to release reasources
cv2.destroyAllWindows()