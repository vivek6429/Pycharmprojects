import cv2 as cv

img=cv.imread("data/image.jpg",0)
cv.imshow("image",img)
k=cv.waitKey(0) & 0xFF # use the mask in 64 bit machine if error

if k==27:
    cv.destroyAllWindows()
elif k==ord('s'):
    cv.imwrite('copy.png', img)