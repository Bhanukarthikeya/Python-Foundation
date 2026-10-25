from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("ford.csv")

print(df.shape)

print(df.head())

print(df.info())

print(df.describe())

print(df.isnull().sum())

# EDA

sns.histplot(df['price'],bins = 50,kde=True)
plt.show()

heat = df.corr(numeric_only=True)
sns.heatmap(heat,annot = True)
plt.show()

sns.boxplot(data=df,x = "year",y = 'price')
plt.show()

sns.scatterplot(x = 'mileage',y = 'price',data = df)
plt.show()

sns.boxplot(x = 'engineSize', y = 'price',data = df)
plt.show()

sns.boxplot(data= df, x = 'transmission', y = 'price')
plt.show()

sns.boxplot(data= df, x = 'fuelType', y = 'price')
plt.show()

sns.boxplot(data= df, x = 'model', y = 'price')
plt.show()

X = df.drop(columns=['price'])
y = df['price']

# now lets encode X

X_one_encode = pd.get_dummies(
    X, columns=['model', 'transmission', 'fuelType'], drop_first=True)

X_one_encode = X_one_encode.astype(int)
print(X_one_encode)

# importing sklearn label encoder

encode = LabelEncoder()

cols = ['model', 'transmission', 'fuelType']
Xlable = X.copy()
label_encoders = {}

for col in cols:
    le = LabelEncoder()
    Xlable[col] = le.fit_transform(Xlable[col].astype(str))
    label_encoders[col] = le

print(Xlable)

# standard scaler


numerical_cols = ['year', 'mileage', 'tax', 'mpg', 'engineSize']
scaler = StandardScaler()
X_one_encode[numerical_cols] = scaler.fit_transform(
    X_one_encode[numerical_cols])

Xlable[['model', 'year', 'transmission', 'mileage', 'fuelType', 'tax', 'mpg', 'engineSize']] = scaler.fit_transform(
    Xlable[['model', 'year', 'transmission', 'mileage', 'fuelType', 'tax', 'mpg', 'engineSize']])

print(Xlable)


# importing train test split
# importing linerregression
# importing r2_score

# model with one hot encoding

X_train,X_test,y_train,y_test = train_test_split(X_one_encode,y,test_size = 0.2,random_state=42)

model = LinearRegression()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
print(y_pred) #predicted
print(y_test) #actual

r2 = r2_score(y_test,y_pred)
print(r2)

# adjusted r2
n = X_test.shape[0]
p = X_test.shape[1]
adj_r2 = 1 - ((1-r2) * (n-1) / (n-p-1))
print(adj_r2)

# lable encoding model

X_train2,X_test2,y_train2,y_test2 = train_test_split(Xlable,y,test_size = 0.2,random_state=42)
model = LinearRegression()
model.fit(X_train2,y_train2)
y_pred2 = model.predict(X_test2)
r22 = r2_score(y_test2,y_pred2)
print(r22)

n2 = X_test2.shape[0]
p2 = X_test2.shape[1]
adj_r22 = 1 - ((1-r22) * (n2-1) / (n2-p2-1))
print(adj_r22)