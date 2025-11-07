from sklearn import datasets , linear_model
from sklearn.metrics import mean_squared_error
import numpy as np
import matplotlib.pyplot as plt

#Load dataset
dia = datasets.load_diabetes()

#Columns
#['data', 'target', 'frame', 'DESCR', 'feature_names', 'data_filename', 'target_filename', 'data_module']
#print(dia.DESCR)

#Produce array of arrays having one element each by np.newaxis and slicing the data set for data and target only
dia_x=dia.data[: , np.newaxis , 2]
print("No of data vals:",len(dia_x))

#Filter training (first 30) and testing (last rest) x and y vals
dia_x_train = dia_x[:-30]
dia_x_test = dia_x[-30:]
dia_y_train = dia.target[:-30]
dia_y_test = dia.target[-30:]

#Form a Lin reg model
model = linear_model.LinearRegression()

#best fitting line
model.fit(dia_x_train , dia_y_train)

#Predictions of rest vals
dia_y_predict = model.predict(dia_x_test)

print("Mean sq error:", mean_squared_error(dia_y_test, dia_y_predict))

print("Weights:" , model.coef_)     #y=w0 + w1*x --> w1 is wt and  w0 is intercept
print("Intercepts" , model.intercept_)

plt.scatter(dia_x_test,dia_y_test)
plt.plot(dia_x_test,dia_y_predict)
plt.show()