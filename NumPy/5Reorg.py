import numpy as np

a=np.array([[1,2,3,4],[5,6,7,8]])
print(a)
b=a.reshape((8,1))      #any order (p,q) st p*q = no of elements
print(b)
print()

#Stack
v1=np.array([1,2,3,4])
v2=np.array([5,6,7,8])
print(np.vstack([v1,v2,v2]))
print()

h1=np.array([[1,2],[3,4]])
h2=np.array([[5,6],[7,8]])
print(np.hstack([h1,h2]))

#Sort
e=np.array([[103,25,36],[81,53,52]])
print(np.sort(e))            #Sort row wise
print(np.sort(e , axis=0))   #Sorts rows too by 1st element of each
print(np.sort(e , axis=1))   #Sorts rows too by 1st element of each
print(np.sort(e , axis=0 , kind='mergesort'))   #Sorts by mergesort algo only
print()

#Arg
print(np.argsort(e))    #prints seq of indices off elements to be positioned in order to get sorted array
print(np.argmin(e))     #prints position val of minimum element
print(np.argmax(e))     #prints position of max val elements
print()