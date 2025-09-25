import numpy as np

import matplotlib.pyplot as plt

import pandas as pd 

dataset = pd.read_csv(r"C:\Users\Kumar\FS AIML\13th- ML\13th- ML\5. Data preprocessing\Data.csv")

X = dataset.iloc[:,:-1].values  # independent variable

Y = dataset.iloc[:,3].values  # dependent variable

from sklearn.impute import SimpleImputer 

imputer = SimpleImputer(strategy='median')

imputer = imputer.fit(X[:,1:3])

X[:,1:3] = imputer.transform(X[:,1:3])
 

# transforming categorical data

from sklearn.preprocessing import LabelEncoder

labelEncoder_X = LabelEncoder()

X[:,0] = labelEncoder_X.fit_transform(X[:,0])

labelEncoder_Y = LabelEncoder()

Y = labelEncoder_Y.fit_transform(Y)

# model selection and split the X and Y for training the model

from sklearn.model_selection import train_test_split

# training the model with 80-20 model

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,train_size=0.8, test_size= 0.2)
