import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report

df = sns.load_dataset("titanic")
print(df.head())
# print(df.columns)
# print(df.info())
# print(df.describe())

df = df.drop(columns=['deck', 'embark_town',
             'alive', 'class', 'who', 'adult_male'])
# print(df.head())

# we will filled na with mean
df['age'] = df['age'].fillna(df['age'].mean(), inplace=True)

# here we dropped 2 rows which have 2 null values
df.dropna(subset=['embarked'], inplace=True)

# print(df.head())

# print(df.info())

# label encoding

le = LabelEncoder()
df['sex'] = le.fit_transform(df['sex'])
df['embarked'] = le.fit_transform(df['embarked'])

df = df.astype(int)

# print(df.head())

X = df.drop('survived', axis=1)
y = df['survived']

scaler = StandardScaler()

X = scaler.fit_transform(X)
# print(X)


# train test split


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

model = DecisionTreeClassifier()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
# print(y_pred)
# print(y_test)

accuracy = accuracy_score(y_test,y_pred)
# print(accuracy)

matrix = confusion_matrix(y_test,y_pred)
# print(matrix)

report = classification_report(y_test,y_pred)
# print(report)
