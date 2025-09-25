# lasso ridge regularization 

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 
%matplotlib inline

from sklearn import preprocessing
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import r2_score 

data = pd.read_csv(r"C:\Users\Kumar\FS AIML\car-mpg.csv")
data.head()

data = data.drop(['car_name'], axis =1)

data['origin'] = data['origin'].replace({1:'america', 2:'europe', 3:'asia'})

data = pd.get_dummies(data,columns=['origin'],dtype=int)

data = data.replace('?',np.nan)

data = data.apply(pd.to_numeric, errors = 'ignore')

numeric_cols = data.select_dtypes(include = [np.number]).columns

data = data.apply(lambda x : x.fillna(x.median()), axis=0)

X = data.drop(['mpg'], axis=1) # independent variable
y = data[['mpg']] # dependent variable

# Scaling the data

X_s = preprocessing.scale(X)
X_s = pd.DataFrame(X_s, columns =  X.columns)

y_s = preprocessing.scale(y)
y_s = pd.DataFrame(y_s, columns=y.columns)

# train and test data

X_train, X_test, y_train, y_test = train_test_split(X_s, y_s, test_size=0.2, random_state=0)

regression_model = LinearRegression()
regression_model.fit(X_train,y_train)

for idx, col_name in enumerate(X_train.columns):
    print('The coefficient for {} is {}'.format(col_name, regression_model.coef_[0][idx]))
    
intercept = regression_model.intercept_[0]
print('The intercept is {}'.format(intercept))


# Ridge model

ridge_model = Ridge(alpha= 0.3)
ridge_model.fit(X_train, y_train)

print('Ridge model coef: {}'.format(ridge_model.coef_))


#alpha factor here is lambda (penalty term) which helps to reduce the magnitude of coeff

lasso_model = Lasso(alpha = 0.1)
lasso_model.fit(X_train, y_train)

print('Lasso model coef: {}'.format(lasso_model.coef_))