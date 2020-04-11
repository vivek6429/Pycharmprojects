import cv2

# video capture class
cap = cv2.VideoCapture(0)  # try -1 or 0 for primary

# video writer class
# coded check fourcc.org on google
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# or ('X','V','I','D')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))
# filename,codec,fps,tuplesize # width height
print((cap.get(3),"   ",cap.get(4)))
# use cap.set() use this to to change parameters
# but resolution goes to be same value
# can use predefined hardware value

# if false use cap.open to open any other file
# cap returnes  False if wrong video or device
while (cap.isOpened()):
    ret, frame = cap.read()

    if ret == True:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) #3
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # get prop id
        out.write(frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('camera', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()  # important to release reasources
out.release()
cv2.destroyAllWindows()
