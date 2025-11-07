from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

iris=datasets.load_iris()
#print(iris.DESCR) for description
print("\nFeatures: \n1. sepal length in cm \n2. sepal width in cm \n3. petal length in cm \n4. petal width in cm")
print("\nLabel: \n0.Iris Setosa \n1.Iris Versicolour \n2.Iris Virginica")

features=iris.data
labels=iris.target

#Train the KNN Classifier
clf = KNeighborsClassifier()
clf.fit(features,labels)

#Prediction
preds = clf.predict([[5.1, 3.4, 4.9, 2.3]])
print("\nGiven sample is:",preds)

#Plot data set
plt.scatter(features[:,0],labels, label='Sepal length')
plt.scatter(features[:,1],labels, label='Sepal width')
plt.scatter(features[:,2],labels, label='Petal length')
plt.scatter(features[:,3],labels, label='Petal Width')
plt.legend()
plt.show()