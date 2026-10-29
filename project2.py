from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
df = pd.read_csv("heart.csv")

# EDA

# print(df.head().to_string())

# print(df.shape)

# print(df.info())

# print(df.describe())

# print(df.columns)

# print(df.isnull().sum())

# print(df['Sex'].value_counts()) # 2types M,F
# print(df['ChestPainType'].value_counts()) # 4types
# print(df['FastingBS'].value_counts() # 2types 0,1
# print(df['RestingECG'].value_counts()) # 3types
# print(df['ExerciseAngina'].value_counts()) # 2types N,Y
# print(df['Oldpeak'].value_counts()) #alot
# print(df['ST_Slope'].value_counts()) # 3types

# print(df['HeartDisease'].value_counts())

# def plotting(var,num):
#     plt.subplot(2,2,num)
#     sns.histplot(df[var],kde = True)

# plotting("Age",1)
# plotting("RestingBP",2)
# plotting("Cholesterol",3)
# plotting("MaxHR",4)
# plt.tight_layout()
# plt.show()

# by looking at plots we got to know that one person have a restingBP of 0 it is not possible

# df['cholesterol'].value_counts() # here also 0 There which is not possible

# so we will clean the data

ch_mean = df.loc[df['Cholesterol'] != 0, 'Cholesterol'].mean()
df['Cholesterol'] = df['Cholesterol'].replace(0, ch_mean)
df['Cholesterol'] = df['Cholesterol'].round(2)

resting_bp_mean = df.loc[df['RestingBP'] != 0, 'RestingBP'].mean()
df['RestingBP'] = df['RestingBP'].replace(0, ch_mean)
df['RestingBP'] = df['RestingBP'].round(2)

# plotting("Age",1)
# plotting("RestingBP",2)
# plotting("Cholesterol",3)
# plotting("MaxHR",4)
# plt.tight_layout()
# plt.show()

# sns.countplot(x = df['Sex'],hue = df['HeartDisease'])
# sns.countplot(x = df['ChestPainTypes'],hue = df['ChestPainTypes'])
# sns.countplot(x = df['FastingBS'],hue = df['ChestPainTypes'])

# plt.show()

# sns.boxplot(x = 'HeartDisease',y = 'Cholesterol',data= df)
# sns.violinplot(x = 'HeartDisease',y = 'Age',data= df)
# sns.heatmap(df.corr(numeric_only=True),annot = True)
# plt.show()

# data preprocessing and cleaning

df_encode = pd.get_dummies(df, drop_first=True)
df_encode = df_encode.astype(int)

# scaling

numerical_cols = ['Age', 'RestingBP', 'Cholesterol', 'MaxHR', 'Oldpeak']
scaler = StandardScaler()
df_encode[numerical_cols] = scaler.fit_transform(df_encode[numerical_cols])
# print(df_encode.head())


X = df_encode.drop("HeartDisease",axis = 1)
y = df_encode['HeartDisease']

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

models = {
    "logistic regression": LogisticRegression(),
    "KNN": KNeighborsClassifier(),
    "SVM": SVC(),
    "naive bayes": GaussianNB(),
    "decision tree": DecisionTreeClassifier()
}

result = []

for name,model in models.items():
    model.fit(X_train,y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test,y_pred)
    result.append({
        "model": name,
        "accuracy": round(accuracy,4)
    })

for i in result:
    print(i)