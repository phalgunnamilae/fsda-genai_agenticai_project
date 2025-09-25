import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data_set = pd.read_csv(r"C:\Users\Kumar\FS AIML\20th - mlr\20th - mlr\MLR\Investment.csv")

X = data_set.iloc[:,:-1]
y = data_set.iloc[:,4]

X = pd.get_dummies(X,dtype=int) 

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, test_size=0.2)

from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)

m = regressor.coef_
print(m)

c = regressor.intercept_
print(c)

#X = np.append(arr = np.ones((50,1)).astype(int),values=X, axis=1)

X = np.append(arr = np.full((50,1), 50914).astype(int), values=X, axis=1)

import statsmodels.api as sm

X_opt = X[:,[0,1,2,3,4,5]]

regressor_OLS = sm.OLS(endog=y, exog =X_opt).fit()
regressor_OLS.summary()

# Here the x5 has the highest p value, which is >0.05, hence remove it and rerun

X_opt = X[:,[0,1,2,3,4]]

regressor_OLS = sm.OLS(endog=y, exog =X_opt).fit()
regressor_OLS.summary()


X_opt = X[:,[0,1,2,3]]

regressor_OLS = sm.OLS(endog=y, exog =X_opt).fit()
regressor_OLS.summary()


X_opt = X[:,[0,1,3]]

regressor_OLS = sm.OLS(endog=y, exog =X_opt).fit()
regressor_OLS.summary()


X_opt = X[:,[0,1]]

regressor_OLS = sm.OLS(endog=y, exog =X_opt).fit()
regressor_OLS.summary()

# Now the p value is 0, hence x1 is the value which is the best fit.

data_set.columns

# here the x1 is 'Digital Marketing', so the conclusion is when the amount invested in Digital Marketing the profits are more 

# Create front end for this 