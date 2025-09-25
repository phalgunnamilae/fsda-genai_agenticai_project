import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import (
    LinearRegression, Ridge, Lasso, ElasticNet, SGDRegressor, HuberRegressor
)
from sklearn.svm import SVR
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline #data leakages 
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.neural_network import MLPRegressor
import xgboost as xgb
import lightgbm as lgb
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import pickle

#Title

st.title("Welcome to Regressor Analyser")

#Load data set
data_set = pd.read_csv(r"C:\Users\Kumar\FSDS-AIML\fsds_genai_agenticai\USA_Housing.csv")


# Pre Processing
X = data_set.drop(['Price','Address'], axis=1)
y = data_set['Price']

# Split data

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.2, train_size=0.8, random_state=0)

# Define models

models = {
    "LinearRegression": LinearRegression(),
    'RobustRegression': HuberRegressor(),
    'RidgeRegression': Ridge(),
    'LassoRegression': Lasso(),
    'ElasticNet': ElasticNet(),
    'PolynomialRegression': Pipeline([
        ('poly', PolynomialFeatures(degree=4)),
        ('linear', LinearRegression())
    ]),
    'DecisitionTree': DecisionTreeRegressor(),
    'RandomForest': RandomForestRegressor(),
    'SVR': SVR(),
    'KNN': KNeighborsRegressor(),
    'LGBM': lgb.LGBMRegressor(),
    }

model_name = st.sidebar.selectbox("Select Regressor", list(models.keys()))

# Train and Evaluate models

results = []

# models[model_name].fit(X_train, y_train)
# y_pred = models[model_name].predict(X_test)

# mae = mean_absolute_error(y_test, y_pred)
# mse = mean_squared_error(y_test, y_pred)
# r2 = r2_score(y_test, y_pred)

# st.write(f"Mean absolute error for {model_name} is {mae}")
# st.write(f"Mean squared error for {model_name} is {mse}")
# st.write(f"R2 for {model_name} is {r2}")



for name, model in models.items():
   model.fit(X_train, y_train)
   y_pred = model.predict(X_test)
    
   mae = mean_absolute_error(y_test, y_pred)
   mse = mean_squared_error(y_test, y_pred)
   r2 = r2_score(y_test, y_pred)
    
   results.append({
       'Model': name,
       'MAE': mae,
       'MSE': mse,
       'R2': r2
  })
    
   with open(f"{name}.pkl",'wb') as f:
       pickle.dump(model, f)
        
#convert the results to csv file

results_df = pd.DataFrame(results)
results_df.to_csv('model_evaluation_results.csv', index=False)

print("Models have been trained and saved as pickle files. Evaluation results have been saved to model_evaluation_results.csv.")

    
    
    
    