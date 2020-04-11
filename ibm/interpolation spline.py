import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline

x = np.linspace(-3, 3, 50)
y = np.exp(-x ** 2) + 0.1 * np.random.randn(50)
plt.plot(x, y, 'ro', ms=5)
plt.show()


spl = UnivariateSpline(x, y)
xs = np.linspace(-3, 3, 1000)
plt.plot(xs, spl(xs), 'g', lw=3)
plt.show()

# smoothing improves accuracy
spl.set_smoothing_factor(0.5)
# system knows spl is a variable it passes xs as parameter
# statement where line 11 is reffered
# absolute dynamic binding
plt.plot(xs, spl(xs), 'b', lw=3)
plt.show()
