import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset = pd.read_csv(r"C:\Users\Kumar\FS AIML\Salary_Data.csv")

x = dataset.iloc[:,:-1]
y = dataset.iloc[:,-1]

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, train_size= 0.8)

from sklearn.linear_model import LinearRegression

regressor = LinearRegression()

regressor.fit(x_train, y_train)

y_pred = regressor.predict(x_test)

plt.scatter(x_test, y_test, color = 'red')
plt.plot(x_train, regressor.predict(x_train), color='blue')
plt.title("Salary vs Experience (Test set)")
plt.xlabel("Years of exp")
plt.ylabel("Salary")
plt.show()

#slope

m = regressor.coef_

# c value

c = regressor.intercept_

yr_12 = (m*12)+c  # for 12 year exp

yr_20 = (m*20)+c  # for 20 year exp salary 

bias = regressor.score(x_train, y_train)
bias

variance = regressor.score(x_test, y_test)
variance

# stats for simple linear regressor model

dataset.mean()

dataset['Salary'].mean()

dataset.median()

dataset['Salary'].median()

dataset['Salary'].mode()

dataset.var()

dataset['Salary'].var()

# standard deviation

dataset.std()

dataset['Salary'].std()


# coefficient of variance 

from scipy.stats import variation

variation(dataset.values)

variation(dataset['Salary'])


# correlation

dataset.corr()


dataset['Salary'].corr(dataset['YearsExperience'])


#skewness

dataset.skew()

dataset['Salary'].skew()

# standard error

dataset.sem()

dataset['Salary'].sem()


# Z score

import scipy.stats as stats 

dataset.apply(stats.zscore)

stats.zscore(dataset['Salary'])


# SSR - sum of squares regressors 

y
