#Log Regr classifier for iris virginica or not
from sklearn import datasets
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression

iris = datasets.load_iris()
x = iris['data'][:,3:]
y = (iris['target'] == 2).astype(np.int16)

#Train log regr model
clf = LogisticRegression()
clf.fit(x,y)

#Predicting
print(clf.predict([[2.6]]))

#Plotting
x_new = np.linspace(0,3,1000).reshape(-1,1)     #Give 1000 nos betn 0 and 3. Reshaping in single column
y_prob = clf.predict_proba(x_new)
print(y_prob)
plt.plot(x_new, y_prob[:,1], "g-", label="Virginica")
plt.legend()
plt.show()