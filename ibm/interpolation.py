import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

x = np.linspace(0, 4, 12)
y = np.cos(x ** 2 / 3 + 4)
print(x, y)
plt.plot(x, y, 'o')
plt.show()

f1 = interpolate.interp1d(x, y, kind='linear')
f2 = interpolate.interp1d(x, y, kind='cubic')
xnew = np.linspace(0, 4, 30)
print(x,y)
plt.plot(x, y, 'o', xnew, f1(xnew), '-', xnew, f2(xnew), '--')
plt.legend(['data', 'linear', 'cubic', 'nearest'], loc='best')
plt.show()
