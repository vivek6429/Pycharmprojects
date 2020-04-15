# technique used for seperation of objects from background
# comparing each pixel with a threshold values
import cv2
import matplotlib.pyplot as plt
import numpy as np


def nothing(x):
    pass


img = cv2.imread("data/gradient.png")
titles = ["original image", "BINARY", "BIN_INV", "TRUNC", "TOZERO", "TO_ZERO_INV"]
cv2.namedWindow("controls")
cv2.createTrackbar("val", "controls", 0, 255, nothing)



while True:

    val = cv2.getTrackbarPos("val", "image")
    ret, thold = cv2.threshold(img, val, 255, cv2.THRESH_BINARY)
    ret2, thold2 = cv2.threshold(img, val, 255, cv2.THRESH_BINARY_INV)
    ret3, thold3 = cv2.threshold(img, val, 255, cv2.THRESH_TRUNC)
    ret4, thold4 = cv2.threshold(img, val, 255, cv2.THRESH_TOZERO)
    ret5, thold5 = cv2.threshold(img, val, 255, cv2.THRESH_TOZERO_INV)
    images = [img, thold, thold2, thold3, thold4, thold5]

    for i in range(6):
        plt.subplot(2, 3, i + 1)
        plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])

    plt.show()
    cv2.imshow("controls",img)

    # 2 row 3 col  index of image
cv2.destroyAllWindows()
