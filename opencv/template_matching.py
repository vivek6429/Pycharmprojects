# template matching is a methord of searching and finding a template image
# inside a larger image
# methord called match template

import cv2
import numpy as np

img = cv2.imread("data/messi5.jpg")
grey_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
template = cv2.imread("head.jpg", 0)
# h, w = template.shape()
w,h = template.shape[::-1]

res = cv2.matchTemplate(grey_image, template, method=cv2.TM_CCOEFF_NORMED)  # several methord , try them out
print(res)
# in matrix shows bright point when matching
#  reflected in matrix as a decimal number
#  GET THE BRIGHTEST POINT : this point matches with templates  `top left` 0,0 point
#  use numpy where
threshold = 0.9  # initialy
loc = np.where(res >= threshold)  # find values which is greter or equal to thresh
# loc = np.where()
print(loc)
for pt in zip(*loc[::-1]): # reversed here to change r,c to x,y coz r-->y c-->x on window
    img = cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (255, 255, 255), 1)

cv2.imshow("messi", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
