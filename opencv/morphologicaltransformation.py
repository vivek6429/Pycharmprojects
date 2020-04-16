# erosion dilation opening and closing
# some simple operation based on image shape
# performed on binary image
# originalimage decidingimagekernal which decides nature of the transformation

import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("data/smarties.png", 0)  # cv2.IMREAD_GRAYSCALE
# img = cv2.imread("data/j5v72y.jpg", 0)
ret, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

# a kernel some shape like square , iterations no of time to do
# bigger the rectangle better result but shapes get joint
kernal = np.ones((5, 5), np.uint8)  # kernal slides through all pixels
######################################
#
# pixel element is 1 if atleast 1 pixel under kernal is 1 in
dilation = cv2.dilate(mask, kernal, iterations=2)

# sides have erroded for shape like soilerosion
# a pixel is considered 1 only when all pixels under it are 1
erosion = cv2.erode(mask, kernal, iterations=2)

# Opening is erosion followed by dilation
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)

# closing is dilation followed by erosion
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)

# morphological gradient is difernce between dilation and erosion
mg = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernal)

# difference between image and opening of an image
tophat = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernal)
#
titles = ['image', "mask", "dilation", "erosion", "open", "close", "morph grad", "tophat"]
images = [img, mask, dilation, erosion, opening, closing, mg, tophat]
for i in range(8):
    plt.subplot(2, 4, i + 1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
