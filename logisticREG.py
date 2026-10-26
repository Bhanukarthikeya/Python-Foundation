import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

df = sns.load_dataset("titanic")
# print(df.head())
# print(df.columns)
# print(df.info())
# print(df.describe())

df = df.drop(columns= ['deck','embark_town','alive','class','who','adult_male'])
# print(df.head())

df['age'] = df['age'].fillna(df['age'].mean(),inplace=True) # we will filled na with mean

df.dropna(subset=['embarked'],inplace = True) # here we dropped 2 rows which have 2 null values

# print(df.head())

# print(df.info())

# label encoding
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
df['sex'] = le.fit_transform(df['sex'])
df['embarked'] = le.fit_transform(df['embarked'])

df = df.astype(int)

# print(df.head())

X = df.drop('survived',axis= 1)
y = df['survived']

# train test split

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

# logistic reg

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()

model.fit(X_train,y_train)
y_pred = model.predict(X_test)

# print(y_pred)
# print(y_test)

# confusion matrix

from sklearn.metrics import accuracy_score, confusion_matrix,classification_report
accuracy = accuracy_score(y_test,y_pred)
# print(accuracy)

matrix = confusion_matrix(y_test,y_pred)
# print(matrix)

report = classification_report(y_test,y_pred)
# print(report)