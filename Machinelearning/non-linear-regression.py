import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data_set = pd.read_csv(r"C:\Users\Kumar\FS AIML\emp_sal.csv")

X = data_set.iloc[:,1:2].values
y = data_set.iloc[:,-1].values


from sklearn.linear_model import LinearRegression

lin_reg = LinearRegression()
lin_reg.fit(X,y)

#linear regression visualization

plt.scatter(X,y,color='red')
plt.plot(X, lin_reg.predict(X), color='blue')
plt.title('Linear Regression graph')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()

lin_reg_predict = lin_reg.predict([[6.5]])
lin_reg_predict

# polynomial regression

from sklearn.preprocessing import PolynomialFeatures

#poly_reg = PolynomialFeatures()
#X_poly = poly_reg.fit_transform(X)  # Linear model builds 1 degree poly, Polynomial model builds 2 or more degree poly


#poly_reg = PolynomialFeatures(degree=3)
#X_poly = poly_reg.fit_transform(X)  # Linear model builds 1 degree poly, Polynomial model builds 2 or more degree poly

poly_reg = PolynomialFeatures(degree=5)
X_poly = poly_reg.fit_transform(X)  # Linear model builds 1 degree poly, Polynomial model builds 2 or more degree poly


poly_reg.fit(X_poly,y)

lin_reg2 = LinearRegression()
lin_reg2.fit(X_poly,y)

plt.scatter(X, y, color='red')
plt.plot(X, lin_reg2.predict(poly_reg.fit_transform(X)), color='blue')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

poly_model_pred = lin_reg2.predict(poly_reg.fit_transform([[3.5]]))
poly_model_pred
