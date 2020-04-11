import scipy.ndimage as nd
import numpy as np
import  matplotlib.pyplot as plt
im = np.zeros((256,256))
im[64:-64,64:-64]=1
im[90:-90,90:-90]=2
plt.imshow(im)
plt.show()
im=nd.gaussian_filter(im,8)
# gausian filter applies gaussien numbers over pixels

plt.imshow(im)
plt.show()

# conclusion
''' shows overlapping
gusian values shows a disection
'''