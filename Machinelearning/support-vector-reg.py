import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data_set = pd.read_csv(r"C:\Users\Kumar\FS AIML\emp_sal.csv")

X = data_set.iloc[:,1:2].values
y = data_set.iloc[:,-1].values

#svm model

from sklearn.svm import SVR

#svr_regressor = SVR() # default kernael is "rbf" and degree=3
#svr_regressor.fit(X,y)

#svr_regressor = SVR(kernel="sigmoid", degree=4, gamma="auto") # default kernael is "rbf" and degree=3
#svr_regressor.fit(X,y)

svr_regressor = SVR(kernel="poly", degree=5, gamma="scale") # default kernael is "rbf" and degree=3
svr_regressor.fit(X,y)


svr_model_pred = svr_regressor.predict([[6.5]])
print(svr_model_pred)


# Knn algorithm.

from sklearn.neighbors import KNeighborsRegressor

#knn_regressor = KNeighborsRegressor()

knn_regressor = KNeighborsRegressor(n_neighbors=6, weights='distance') # Hyper parameter tuning

knn_regressor.fit(X,y)

knn_pred = knn_regressor.predict([[6.5]])
print(knn_pred)
