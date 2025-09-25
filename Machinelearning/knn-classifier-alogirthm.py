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

from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier()
classifier.fit(X_train,y_train)

y_pred = classifier.predict(X_test)


from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred)
print(cm)

from sklearn.metrics import accuracy_score

acc_score = accuracy_score(y_test, y_pred)
print(acc_score)

bias = classifier.score(X_train, y_train)
print(bias)

variance = classifier.score(X_test, y_test)
print(variance)
