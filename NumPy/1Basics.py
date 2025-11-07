import numpy as np

#2D array
a=np.array([[1,2,3],[4,5,6]])
print(a)
print(a.ndim)               #Dimentions
print(a.shape)              #Order
print('Data Type:',a.dtype)
print(a.size)               #no of elements
print(a.itemsize)           #memory occupied by each element
print(a.nbytes)             #tot memory occupied

#3D array
b=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b)