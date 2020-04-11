import matplotlib.pyplot as plt
import matplotlib.image as img
import random

# im = img.imread('car.png')
# print(im)
x = [1, 2, 3, 4, 5]
y = [5, 10, 15, 20, 25]
lum = im[:, :, 3]
# #a=plt.scatter(x,y)
# plt.plot(x,y)
# plt.title("CAAAAAAAAAAR")
#plt.imshow(lum)
# plt.show()
#
# plt.title("CAAAAAAAAAAR")
# plt.grid('major')
# plt.imshow(lum,cmap='hot')
# plt.colorbar()
# #plt.xticks(np.arange(0,51,)
# plt.show()


fig = plt.figure()

def get_graphs():
    xs=[]
    ys=[]
    for i in range(10):
        xs.append(i)
        ys.append(random.randrange(10))
    print(xs,ys)
    return xs, ys


ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)
x,y=get_graphs()
ax1.plot(x,y)
ax1.tick_params(axis='both',which='both',length = 0) # length of ----- line


x,y=get_graphs()
ax2.plot(x,y,'b')
ax2.axes.get_xaxis().set_visible(False)
ax2.axes.get_yaxis().set_visible(False)

x,y=get_graphs()
ax3.plot(x,y,'g')
ax3.yaxis.set_major_formatter(plt.NullFormatter())
ax3.xaxis.set_major_formatter(plt.NullFormatter())

x,y=get_graphs()
ax4.plot(x,y,'r')
ax4.tick_params(axis='x', rotation = 45)
ax4.tick_params(axis='y', rotation = -45)
plt.show()