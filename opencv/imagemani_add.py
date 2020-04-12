import cv2 as cv

img = cv.imread("data/messi5.jpg", 1 )
img2 = cv.imread("data/opencv-logo.png")

print(img.shape)  # returs tupple shape
print(img.dtype)
print(img.size)

ball=img[280:340,330:390]
img[273:333,100:160]=ball

# cv.imshow("image", img)
# to add two images size should be same
img=cv.resize(img,(512,512))
img2=cv.resize(img2,(512,512))
# dst=cv.add(img,img2) # input array1, array2, outputarray dist, inputarray mask=noArray(), int  dtype=-1

# can also add weighted img weight. img2 weight2 scalar output  dtype
# uses an eqn dst = saturate (src1 x alpha + src2 x beta + gamma(the scalar) )
# weight sum =1
dst=cv.addWeighted(img,.90,img2,.10,0)


cv.imshow("image", dst)
k = cv.waitKey(0) & 0xFF  # use the mask in 64 bit machine if error
if k == 27:
    cv.destroyAllWindows()
elif k == ord('s'):
    cv.imwrite('copy.png', img)

# ROI - Region of interest