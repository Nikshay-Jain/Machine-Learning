import numpy as np

a=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
#Indices (x,y) compared to Cartesian Coordinates are (-y,x) directions to be traversed in matrix

print(a[1,5])
print(a[0,:])
print(a[:,2])
print(a[0,1:6:2])    #Stepvalue
a[1,5]=20
a[:,2]=[1,2]
print(a,'\n')

#3D array
b=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b)
print(b[:,1,:])

#Slicing works by pointers in C lang so editing in new variable will edit previous one only.