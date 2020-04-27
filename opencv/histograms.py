# uses
# Tells ehther image has been properly eposed
# Tells whether lightning where flat or harsh
# to analyze the adjustments required
import numpy as np
import cv2
from matplotlib import pyplot as plt

# img = np.zeros((200,200),np.uint8)
# cv2.rectangle(img,(0,50),(100,100),(127),-1)
img = cv2.imread("data/lena.jpg")
b, g, r = cv2.split(img)

# ravel , max pixel vals,range
# shows pixel values
# gives overall idea about the intensity distributions
# plt.hist(img.ravel(),256,[0,256])
# plt.hist(b.ravel(),256,[0,256])
# plt.hist(g.ravel(),256,[0,256])
# plt.hist(r.ravel(),256,[0,256])
# cv2.imshow("window",img)
# cv2.imshow("windowb",b)
# cv2.imshow("windowg",g)
# cv2.imshow("windowr",r)
# plt.show()


# [image] --- note as square i.e list , [0] for channel
# mask - none for all , size , ranges 0 to 256
# need matplotlib
hist = cv2.calcHist([img], [0], None, histSize=[256], ranges=[0, 256])
plt.plot(hist)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
