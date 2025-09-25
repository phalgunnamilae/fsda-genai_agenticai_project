import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data_set = pd.read_csv(r"C:\Users\Kumar\FSDS-AIML\fsds_genai_agenticai\Machinelearning\regressors_practice\logit classification.csv")

X = data_set.iloc[: , 2:4]
y = data_set.iloc[:,-1]

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size= 0.80, test_size= 0.20, random_state=0)

#Scaling

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


# from sklearn.preprocessing import Normalizer

# nrm = Normalizer()
# X_train = nrm.fit_transform(X_train)
# X_test = nrm.transform(X_test)


# Fit the model

from sklearn.linear_model import LogisticRegression

classifier = LogisticRegression()
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)
# Model Accuracy

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred)
print(cm)


from sklearn.metrics import accuracy_score

acc_score = accuracy_score(y_test, y_pred)
print(acc_score)

from sklearn.metrics import classification_report

classify_report = classification_report(y_test, y_pred)
print(classify_report)


# Bias and Variance

# Bias -- Is training score , Varaince is Testing score

bias = classifier.score(X_train, y_train)
print(bias)

variance = classifier.score(X_test, y_test)
print(variance)


# ------ Future Prediction ------------

data_set1 = pd.read_csv(r"C:\Users\Kumar\FS AIML\2.LOGISTIC REGRESSION CODE\final1.csv")

d2 = data_set1.copy()

data_set1 = data_set1.iloc[:, [3,4]].values

from sklearn.preprocessing import StandardScaler

sc1 = StandardScaler()
M = sc1.fit_transform(data_set1)

y_pred1 = pd.DataFrame()
d2['y_pred1'] = classifier.predict(M)

d2.to_csv("predicted_final.csv")

# import os

# os.getcwd()












