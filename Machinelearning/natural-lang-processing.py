import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

#import data set

data_set = pd.read_csv(r"C:\Users\nphal\fsda-genai_agenticai_project\Restaurant_Reviews.tsv", delimiter='\t', quoting=3)


# Data cleaning

import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer


# List of classifiers
classifiers = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "KNN": KNeighborsClassifier(),
    "SVM": SVC(),
    "Decision Tree": DecisionTreeClassifier(),
    "Random Forest": RandomForestClassifier(),
    "Naive Bayes": GaussianNB(),
    "Gradient Boosting": GradientBoostingClassifier(),
    "AdaBoost": AdaBoostClassifier()
}


corpus = []

for i in range(0, 1000):
    review = re.sub('[^a-zA-Z]', ' ', data_set['Review'][i])
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)
    
# Create Bag of model to convert the text to vectors 

# from sklearn.feature_extraction.text import CountVectorizer

# cv = CountVectorizer()
# X = cv.fit_transform(corpus).toarray()
# y = data_set.iloc[:, 1].values


from sklearn.feature_extraction.text import TfidfVectorizer

tfv = TfidfVectorizer()

X = tfv.fit_transform(corpus).toarray()
y = data_set.iloc[:,1].values

# Splitting the data set to train and split

from sklearn.model_selection import train_test_split

X_train,X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train, predict and evaluate
for name, clf in classifiers.items():
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    
    print(f"\n{name}")
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))
    print("bias is {}", clf.score(X_train, y_train))
    print("variance is {}", clf.score(X_test, y_test))

#from sklearn.tree import DecisionTreeClassifier

#dtc = DecisionTreeClassifier()

#dtc.fit(X_train, y_train)

# Predict the result

#y_pred = dtc.predict(X_test)


# Build the Confusion Matrix

#cm = confusion_matrix(y_test, y_pred)

#acc_score = accuracy_score(y_test, y_pred)

#bias = dtc.score(X_train, y_train)
#variance = dtc.score(X_test, y_test)

# bias is 99% and varaince is 67% low, hence this is underfitting model 

# Apply all the classification algorithms and achieve the best fit model 



#===============================================
'''
CASE STUDY --> model is underfitted  & we got less accuracy 

1> Implementation of tfidf vectorization , lets check bias, variance, ac, auc, roc 
2> Impletemation of all classification algorihtm (logistic, knn, randomforest, decission tree, svm, xgboost,lgbm,nb) with bow & tfidf 
4> You can also reduce or increase test sample 
5> xgboost & lgbm as well
6> you can also try the model with stopword 


6> then please add more recores to train the data more records 
7> ac ,bias, varian - need to equal scale ( no overfit & not underfitt)

'''