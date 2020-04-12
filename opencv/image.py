import cv2 as cv

img = cv.imread("data/image.jpg", 0)
cv.imshow("image", img)
k = cv.waitKey(0) & 0xFF  # use the mask in 64 bit machine if error
print(img.shape)  # returs tupple shape
print(img.dtype)
print(img.size)

b, g, r = cv.split(img)
img = cv.merge((b, g, r))

if k == 27:
    cv.destroyAllWindows()
elif k == ord('s'):
    cv.imwrite('copy.png', img)

# ROI - Region of interest