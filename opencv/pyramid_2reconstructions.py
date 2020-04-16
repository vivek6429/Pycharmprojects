# STEPS TO BLEND IMAGE
# 1 LOAD TWO IMAGES
# 2 FIND GAUSSIAN PYRAMIDS OF EACH
# 3 FIND LAPLACEIAN
# 4 JOIN LEFT AND RIGHT IN EACH LEVEL OF LAPLACEIAN
# 5 JOIN AND RECONSTRUCT
import cv2
import numpy as np

apple = cv2.imread("data/apple.jpg")
orange = cv2.imread("data/orange.jpg")
print(apple.shape)  # 512 , 512 , 3
print(orange.shape)  # 512 , 512 , 3
apple_orange = np.hstack((apple[:, :256], orange[:, 256:]))

# generate gaussian pyramid for apple and orange
apple_copy = apple.copy()
gp_apple = [apple_copy]
orange_copy = orange.copy()
gp_orange = [orange]
for i in range(6):
    apple_copy = cv2.pyrDown(apple_copy)
    gp_apple.append(apple_copy)
    orange_copy = cv2.pyrDown(orange_copy)
    gp_orange.append(orange_copy)

# generate laplacian
apple_copy = gp_apple[5]  # NOTE 5
lp_apple = [apple_copy]
orange_copy = gp_orange[5]
lp_orange = [orange_copy]
for i in range(5, 0, -1):
    expandedversion = cv2.pyrUp(gp_apple[i])
    laplacian_apple = cv2.subtract(gp_orange[i - 1], expandedversion)
    lp_apple.append(laplacian_apple)
    expandedversion = cv2.pyrUp(gp_orange[i])
    laplacian_orange = cv2.subtract(gp_apple[i - 1], expandedversion)
    lp_orange.append(laplacian_orange)

# Join the half
apple_orange_pyramid = []
n = 0
for apple_lap, orange_lap in zip(lp_apple, lp_orange):
    n += 1
    cols, rows, ch = apple_lap.shape  # to get size of image
    laplacian = np.hstack((apple_lap[:, :int(cols / 2)], orange_lap[:, int(cols / 2):]))
    apple_orange_pyramid.append(laplacian)

# RE CONSTRUCT THE IMAGE
apple_orange_reconstruct = apple_orange_pyramid[0]
for i in range(1,6):
    apple_orange_reconstruct = cv2.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct = cv2.add(apple_orange_pyramid[i], apple_orange_reconstruct)
cv2.imshow("apple", apple)
cv2.imshow("orange", orange)
cv2.imshow("apple_orange", apple_orange)
cv2.imshow("apple_orange_reconstructed", apple_orange_reconstruct)
cv2.waitKey(0)
cv2.destroyAllWindows()
