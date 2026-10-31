from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset("iris")

# print(df.head())
# print(df['species'].value_counts())


X = df.drop("species", axis=1)
y = df['species']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

model = KNeighborsClassifier(n_neighbors=5)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)  # this is to predict accuracy

# print(accuracy)

# another method of predicting accuracy

accuracy = model.score(X_test, y_test)
# print(accuracy) # 100 percent accuracy which means OverFit


model_svm = SVC(gamma='auto')
model_svm.fit(X_train, y_train)
accuracy_svm = model_svm.score(X_test, y_test)
# print(accuracy_svm) # 100

# now we use grid search cv

classifier = GridSearchCV((model_svm), {
    "C": [1, 10, 20, 30],
    'kernel': ['linear', 'rbf']
}, cv=5, return_train_score=False)

classifier.fit(X,y)

# print(classifier.cv_results_)

results = pd.DataFrame(classifier.cv_results_) # this is to understand properly
# print(results)

# now we will take the required data only cause it too much

result = results[['param_C','param_kernel','mean_test_score']]
# print(result) # form this table we can say that C = 1 and kernel = rbf or linear gives the best model
