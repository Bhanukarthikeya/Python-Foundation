import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("insurance.csv")

# # print(df.head())
# # print(df.info())
# # print(df.describe())
# # print(df.columns)
# # print(df.isnull().sum().sum())

# EDA

sns.histplot(df['charges'],bins = 50,kde = True)
plt.show()

heat = df.corr(numeric_only=True)
sns.heatmap(heat,annot=True)
plt.show()

print(df.info())

sns.boxplot(x = 'sex',y = 'charges',data = df)
plt.show()

sns.boxplot(x = 'smoker',y = 'charges',data = df)
plt.show()

sns.boxplot(x = 'region',y = 'charges',data = df)
plt.show()

X = df.drop(columns=['charges','sex'])
y = df['charges']

# lets encode X now using one hot encoding

X_encode = pd.get_dummies(X,columns=['smoker','region'],drop_first=True)

X_encode = X_encode.astype(int)
print(X_encode)

# standard scaling

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
numeric_cols = ['age','children','bmi']
X_encode[numeric_cols] = scaler.fit_transform(X_encode[numeric_cols])

print(X_encode)

from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

X_train,X_test,y_train,y_test = train_test_split(X_encode,y,test_size=0.2,random_state=42)
model = LinearRegression()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)

r2 = r2_score(y_test,y_pred)
print(r2)

n = X_test.shape[0]
p = X_test.shape[1]
adj_r2 = 1 - ((1-r2) * (n-1) / (n-p-1))
print(adj_r2)

print(X_encode)


