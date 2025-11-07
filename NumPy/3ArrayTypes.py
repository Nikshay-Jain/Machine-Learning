import numpy as np

a=np.array([[0,1,2,3,4,5,6,7],[0,8,9,10,11,12,13,14]])

print(np.zeros((2,3)))
print(np.ones((4,2,2),dtype='int32'))
print()

print(np.full((2,2),108))
print(np.full_like(a,4))
#same as print(np.full(a.shape,4))
print()

print(np.random.rand(4,2))
print(np.random.random_sample(a.shape))
print(np.random.randint(-4,7,size=(3,3)))
#inside () is random value betn start=-4 and end=7 with a size =(3,3)
print()

#Identity
print(np.identity(5,dtype='int32'))
print()

#Repeat array
arr=np.array([1,2,3])
r1=np.repeat(arr,3,axis=0)
print(r1,'\n')

arr=np.array([[1,2,3]])
r1=np.repeat(arr,3,axis=0)
r2=np.repeat(arr,3,axis=1)
print(r1)
print(r2)
print()

#Create special array
n=np.ones((5,5),dtype='int32')
m=np.zeros((3,3))
m[1,1]=9
n[1:4,1:4]=m
print(n)
print()

#Empty array - just allocates memory
e=np.empty((4,6))
print(e)
print()

#Simple array operation - each element is operated with itself
print(r1)
print(r1*r1)
print(r1+r1)
print(r1/r1)
print(r1**r1)
print(1/r1)