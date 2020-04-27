# template matching is a methord of searching and finding a template image
# inside a larger image
#

import cv2


def nothing(x):
    pass


img = cv2.imread("data/messi5.jpg")
cv2.namedWindow("Trackbasrs")
cv2.createTrackbar("pt1x", "Trackbasrs", 0, 548, nothing)
cv2.createTrackbar("pt1y", "Trackbasrs", 0, 342, nothing)
cv2.createTrackbar("pt2x", "Trackbasrs", 0, 548, nothing)
cv2.createTrackbar("pt2y", "Trackbasrs", 0, 342, nothing)

while True:
    img = cv2.imread("data/messi5.jpg")

    pt1 = (cv2.getTrackbarPos("pt1x", "Trackbasrs"), cv2.getTrackbarPos("pt1y", "Trackbasrs"))
    pt2 = (cv2.getTrackbarPos("pt2x", "Trackbasrs"), cv2.getTrackbarPos("pt2y", "Trackbasrs"))

    img=cv2.rectangle(img, pt1, pt2, (255, 255, 255), 1)
    # img = cv2.circle(img, (pt1[0],pt1[1]),3 ,(0, 0, 255))
    cv2.imshow("Trackbasrs", img)


    k = cv2.waitKey(1)
    if k == 27:
        break
    elif k== ord('s'):
        # img2=img[0:167,0:259]
        # need small to big
        # img2=[y1:y2,x1:x2]
        img = cv2.imread("data/messi5.jpg")
        img2=img[(pt1[1] if pt1[1] < pt2[1] else pt2[1] ) : (pt1[1] if pt1[1] > pt2[1] else pt2[1]),
             (pt1[0] if pt1[0] < pt2[0] else pt2[0]) : (pt1[0] if pt1[0] > pt2[0] else pt2[0]) ]

        cv2.imwrite("head2.jpg",img2)

        print((pt1[1] if pt1[1] < pt2[1] else pt2[1] ),":" , (pt1[1] if pt1[1] > pt2[1] else pt2[1]),"x--&--y", \
              (pt1[0] if pt1[0] < pt2[0] else pt2[0]), ":",(pt1[0] if pt1[0] > pt2[0] else pt2[0]))

cv2.imshow("written",cv2.imread("head2.jpg"))
cv2.waitKey(0)
cv2.destroyAllWindows()


