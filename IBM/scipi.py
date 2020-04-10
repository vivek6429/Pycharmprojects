# from scipy.constants import pi as s
# from math import pi as m
# from scipy.constants import  pi as s
from math import pi as mpi

from scipy import linalg
import numpy as np

A = np.array([[1, 2, 13], [4, 4, 4], [7, 8, 99]])
eig_val, eig_vect = linalg.eig(A)
print(eig_val)
print(eig_vect)

v = np.array([[2], [3], [5]])
s = linalg.solve(A, v)
print(s)
print("A   ", A)
print(linalg.inv(A))
