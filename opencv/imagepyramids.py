# TO deal with different resolutions
#
# Pyramid or pyramid representation is a type of multi-scale signal representation
# in which a signal or an image is subjected to REPEATED SMOOTHING  and SUBSAMPLING
#
# 2 TYPES IN OPEN CV
# GAUSSIAN & LAPLACEIAN
#
#  GAUSSIAN  --> REPEATED FILTERING AND SUB-SAMPLING  ---> 2 functions pirdown pir up
#
#  LAPLACEIAN --> formed  from GAUSSIAN , no exclusive function
#                 a level in laplaceian is formed by the differnce between that level in gaussian and
#                 its extended version in UPPER level(the second loop)
#

import cv2
import numpy as np
img = cv2.imread("data/lena.jpg")
layer=img.copy() # adding original image to list
gp=[layer] # gaussian pyramid list
'''  instead of this
# lr1 = cv2.pyrDown(img) # lower resolution
# lr2 = cv2.pyrDown(lr1)
# hr2 = cv2.pyrUp(lr2)  # higher resolution
# 
# cv2.imshow("original image",img)
# cv2.imshow("Pyramid down1 gaussian",lr1)
# cv2.imshow("Pyramid down2 gaussian",lr2)
# cv2.imshow("Pyramid up1 gaussian",hr2)
'''
select = 0 # 1- gaussian 0 - laplaceian
if select == 1: # gaussian

    for i in range(5):
        layer = cv2.pyrDown(layer)
        gp.append(layer)
        cv2.imshow(str(i), layer)
    cv2.imshow("original image", img)

else : # LAPLACEIAN
    # 1st FIND GAUSSIAN  2nd EXPANDED 3rd DIFFERENCE

    for i in range(5):
        layer = cv2.pyrDown(layer)
        gp.append(layer)
        # cv2.imshow(str(i), layer)
    layer = gp[5]   # getting the last image
    cv2.imshow("UPPER LEVEL GAUSSIAN PYRAMID",layer) # show the top upper level ;)

    for i in range(5,0,-1):
        gausian_expaned=cv2.pyrUp(gp[i])
        laplacian=cv2.subtract(gp[i-1],gausian_expaned) # that level and its extended in UPPER LEVEL
        cv2.imshow(str(i),laplacian)



cv2.waitKey(0)
cv2.destroyAllWindows()

# conclusion
# once pyrdown is used info is lost , it can not be retrived using pyr up
# LAPLACEIAN AND GAUSSIAN pyramids helps to blend images and reconstruction of images