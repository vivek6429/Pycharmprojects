import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
# from sklearn import datasets, linear_model, metrics
# from sklearn.model_selection import train_test_split


def generate_dataset(n):
    x, y = [], []
    for i in range(n + 1):
        x1 = i
        x2 = i / 2 + np.random.rand() * n
        x.append([1, x1, x2])
        y.append(x1 * x1 + x2 * x2 + 1)
    print('Generated x values  ', np.array(x))
    print('Generated y values  ', np.array(y))
    return np.array(x), np.array(y)


def mse(coef, x, y):
    return np.mean((np.dot(x, coef) - y) ** 2) / 2


def gradients(coef, x, y):
    return np.mean(x.transpose() * (np.dot(x, coef) - y), axis=1)


def multilinear_regression(coef, x, y, lr, b1=0.9, b2=0.999, epsilon=1e-8):

    prev_error = 0
    m_coef = np.zeros(coef.shape)
    v_coef = np.zeros(coef.shape)
    t = 0
    while True:
        error = mse(coef, x, y)
        if abs(error - prev_error) <= epsilon:
            break
        prev_error = error
        grad = gradients(coef, x, y)
        t += 1
        m_coef = b1 * m_coef + (1 - b1) * grad
        v_coef = b1 * v_coef + (1 - b2) * grad ** 2
        moment_m_coef = m_coef / (1 - b1 ** t)
        moment_v_coef = m_coef / (1 - b2 ** t)
        delta = ((lr / moment_v_coef**0.5 + 1e-8) * (b1*moment_m_coef+(1-b1)*grad/(1-b1**t)))
        coef = np.subtract(coef,delta)
    return coef







# driver

x, y = generate_dataset(50)

mpl.rcParams['legend.fontsize'] = 12
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.scatter(x[:, 1], x[:, 2], y, label='y values', s=5)
ax.legend(loc='best')
ax.view_init(45, 0)
plt.show()

coef = np.array([0, 0, 0])
c=multilinear_regression(coef, x, y, 1e-1)
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.scatter(x[:, 1], x[:, 2], y, label='y values', s=5, color="dodgerblue")
ax.scatter(x[:, 1], x[:, 2], c[0] + c[1] * x[:, 1] + c[2] * x[:, 2], label='Regression values', s=5, color="orange")
ax.legend(loc='best')
ax.view_init(45, 0)
plt.show()


# Pillow	7.1.1	7.1.1
# cycler	0.10.0	0.10.0
# imageio	2.8.0	2.8.0
# joblib	0.14.1	0.14.1
# kiwisolver	1.2.0	1.2.0
# matplotlib	3.2.1	3.2.1
# numpy	1.18.2	1.18.3
# opencv-contrib-python	4.2.0.34	4.2.0.34
# pip	20.0.2	20.0.2
# pyparsing	2.4.7	2.4.7
# pyserial	3.4	3.4
# python-dateutil	2.8.1	2.8.1
# scikit-learn	0.22.2.post1	0.22.2.post1
# scipy	1.4.1	1.4.1
# setuptools	46.1.3	46.1.3
# six	1.14.0	1.14.0
# sklearn	0.0	0.0