import numpy as np

list = [1, 2, 3, 4]
arr = np.array(list)
print(arr)

print(np.zeros((2, 3))) # 2 row 3 col
print(np.ones((2, 3)))
print(np.arange(7)) # similar to range , for np array range internal
print("Array Data Type:",arr.dtype)

arr =np.arange(2,10,dtype = np.float)
print(arr)
print("Array Data Type:",arr.dtype)
print(np.linspace(1.,4.,6)) # leniar spacing with 6 elements

print(np.ndarray(1 2 3 4))
mat=np.matrix('1 2;3 4')
print(mat.T)