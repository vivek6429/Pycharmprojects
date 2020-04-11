import cv2 as cv
img=cv.imread("data/image.jpg")

cv.imshow("image",img)

cv.waitKey(5000)
cv.destroyAllWindows()