import numpy as np

#If you do arr2=arr1 and manipulate arr2, its refected in arr1 unless arr2=arr1.copy()
#Operations like arr1 + 2 or - * / ** means altering all elements of arr1
arr=np.array([[1,2,3],[4,5,6]])
print(np.sin(arr),'\n')
print(np.tan(arr),'\n')

#Linear Algebra
a=np.ones((3,2))
b=np.full((2,3),2)
print(np.matmul(b,a))
print()

c=np.identity(5)
print(np.linalg.det(c))
print()

print(np.min(arr))    #np.min(arr,axis=1) shows [1,4]
print(np.max(arr))    #np.max(arr,axis=0) shows [4,5,6]
print(np.sum(arr))    #np.sum(arr,axis=0) gives [5,7,9]

#Vector pdt
c=np.array([1,2])
d=np.array([[3],[4]])
#d=d.transpose()
print(np.dot(c,d))
print(np.cross(c,d.transpose()))