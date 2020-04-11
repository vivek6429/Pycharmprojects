import cv2
import datetime

# img = cv2.imread("data/lena.jpg", 1)
# print(dt)
cap = cv2.VideoCapture(0)
while (cap.isOpened()):
    ret, frame = cap.read()


    if ret == True:
        # print(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) #3
        # print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # get prop id
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        dt=str(datetime.datetime.now())
        text="width :" + str(cap.get(3)) + "Height :" + str(cap.get(4))
        location=(10,50)
        color=(255,0,0)#BGR
        font=cv2.FONT_HERSHEY_SCRIPT_COMPLEX
        fontscale=1
        thickness=2
        linetype=cv2.LINE_AA
        frame=cv2.putText(frame,dt,location,font,fontscale,color,thickness,linetype)
        cv2.imshow('camera', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()  # important to release reasources
cv2.destroyAllWindows()