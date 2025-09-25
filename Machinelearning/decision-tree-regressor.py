import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data_set = pd.read_csv(r"C:\Users\Kumar\FS AIML\emp_sal.csv")

X = data_set.iloc[:,1:2].values
y = data_set.iloc[:,-1].values

# Decision Tree

from sklearn.tree import DecisionTreeRegressor

dtr_regressor = DecisionTreeRegressor()
dtr_regressor.fit(X,y)

dtr_regressor_pred = dtr_regressor.predict([[6.5]])
print(dtr_regressor_pred)

# Random Forest

from sklearn.ensemble import RandomForestRegressor

rf_reg_model = RandomForestRegressor(random_state=0)
rf_reg_model.fit(X,y)

rf_reg_red = rf_reg_model.predict([[6.5]])
print(rf_reg_red)