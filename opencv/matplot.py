from matplotlib import pyplot as plt
import cv2

img = cv2.imread("data/lena.jpg",-1 )
# cv2.imshow('image',img)
cv2.imshow("Image",img)
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.xticks([]),plt.yticks([])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
# conclusion matplot RGB
# cv2 BGR