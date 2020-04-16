# canny edge detector uses multi-stage algorithms to detect wide range of edges in images
# can be broken down to following steps
# 1 NOISE REDUCTION
# 2 GRADIENT CALCULATION -- find intensity gradient
# 3 NON-MAXIMUM SUPPRESSION -- get rid of spurious response to edge detection
# 4 DOUBLE THRESHOLD        -- to determine potential edges
# 5 EDGE TRACKING BY HYSTERESIS -- track edges by hysteresis
#    i.e finalize detection of edges by suppressing edges that are weak or not connected to strong edges
import cv2
import numpy as np
import matplotlib.pyplot as plt

# img = cv2.imread("data/messi5.jpg", 0)
img = cv2.imread("data/lena.jpg", 0)

# thresholds th1 and th2 for hysterisis
canny = cv2.Canny(img,100,200)
titles = ["original image","CANNY"]
images = [img,canny]

for i in range(len(titles)):
    plt.subplot(1, 2, i + 1), plt.title(titles[i]), plt.imshow(images[i], 'gray')
    plt.xticks([]), plt.yticks([])
plt.show()
# conclusion
# proper and precise edges without noise
# check imagegradient.py for comparison
