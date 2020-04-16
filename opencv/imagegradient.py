# image gradient is directional change in intensity or color of image
# 3 types

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("data/messi5.jpg", 0)
# img = cv2.imread("data/sudoku.png", 0)
#
# Laplacian gradient
#
# NOTE: FLOAT DATA TYPE , kernel size
lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)  # float data type because of  -ve gradient slope math
lap = np.uint8(np.absolute(lap))

# sobelx   dx--> order of derivative x dy--> order of derivative y , kernal size
#                               BASICLLY THE DIRECTION
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0)  # vertical
sobelx = np.uint8(np.absolute(sobelx))
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)  # Horizontal
sobelY = np.uint8(np.absolute(sobelY))


# combine sobelx and sobel y
sobelcombined = cv2.bitwise_or(sobelY,sobelx)

# comparing with kenny -in another file detailed
canny = cv2.Canny(img,100,200)

titles = ['image', "laplacian", "SOBEL-X", "SOBEL-Y","sobelcombined","canny"]
images = [img, lap, sobelx, sobelY,sobelcombined,canny]
for i in range(len(titles)):
    plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

# import  cannyedgedetector