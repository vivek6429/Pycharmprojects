import cv2
import numpy as np
import matplotlib.pyplot as plt

#
# img = cv2.imread("data/opencv-logo.png")
# img = cv2.imread("data/gaussian_blur.jpg")
# img = cv2.imread("data/saltandpepper.jpeg")
img = cv2.imread("data/lena.jpg")

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Homogeneous filter each , kernel has homageneous weight
# k=(1/(Kwidth*Kheight))[width,height]
# each output pixel is mean of kernal neighbours
kernel = np.ones((5, 5), np.float32) / 25
dst = cv2.filter2D(img, -1, kernel)  # src depthof dest
# images can be filtered similar to signals lpf hpf
# lpf removes noise , blurring --> need to convolve over image
# hpf finding edges in images ?
# LPF
blur = cv2.blur(img, (5, 5))
# Gaussian filter --> uses different weight kernel in both x and y direction
# k=1/16  *  [ 1  4   6   4   1    middle has higher weight ,lower to sides
#              4 16   24  16  4
#              6  24  36  24  6     for high frequency noise like gaussian
#              4  16  24  16  4
#              1  4   6    4  1
# second is kernel
# third is  sigma x -->
gblur = cv2.GaussianBlur(img, (5, 5), 0)
#
# Median filter, output pixel is median of neighboring pixels
# great for dealing  " salt and pepper noise"  white distorted like salt and black distorted like pepper
# NOTE: Kernel size must be odd here except 1 ie 3,5,7,9 etc for 1 u get original image
mblur = cv2.medianBlur(img, 5)
#
# all methods not only removed noise but also smoothed the edges
#
# Bilateral filter can be used TO PRESERVE EDGES
#
# image ,diameter of each pixel that is used during pixel ,
# sigma color ie filter sigma in color space , sigma space ie filter sigma in cooordinate space
bilateral= cv2.bilateralFilter(img,9,75,75)
titles = ['image', '2dconv', 'blur', 'gaussian blur', "median blur", "bilateral"]
images = [img, dst, blur, gblur, mblur,bilateral]

for i in range(6):
    plt.subplot(2, 3, i + 1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
