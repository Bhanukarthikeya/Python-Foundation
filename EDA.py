# import pandas as pd
# import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt

# tips = sns.load_dataset("tips")

# print(tips.head())

# # Number of rows and columns
# print(tips.shape)

# # Column names
# print(tips.columns)

# # Data types and non-null counts
# tips.info()

# # Statistical summary of numerical columns
# print(tips.describe())

# # Summary of all columns, including categorical ones
# print(tips.describe(include="all"))

# # shape: dataset size.
# # columns: available features.
# # info(): data types and missing-value clues.
# # describe(): mean, standard deviation, quartiles, and other summaries.

# # Missing values in each column
# print(tips.isnull().sum())

# # Total missing values
# print(tips.isnull().sum().sum())

# # Number of duplicate rows
# print(tips.duplicated().sum())

# print("Numerical columns:")
# print(tips.select_dtypes(include="number").columns)

# print("Categorical columns:")
# print(tips.select_dtypes(include=["object", "category"]).columns)

# till now what we studied we will do an example

import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = sns.load_dataset("titanic")
# print(df.head())

# print(df.shape) 891 rows and 15 columns

# print(df.columns)

# print(df.info())

# print(df.describe())

# print(df.describe(include='all'))

# print(df['age'].mean())

# print(df.isnull().sum())

# print(df.isnull().sum().sum())

# print(df.duplicated().sum())

# print(df.isna().sum())

# print(df.select_dtypes(include="number").columns)

# print(df.groupby("sex")["survived"].mean())
# print(df.groupby("pclass")["survived"].mean())
# print(df.groupby("survived")["age"].mean())
# print(df.groupby("embarked")["survived"].mean())

# print("Survival rate by sibsp:")
# print(df.groupby("sibsp")["survived"].mean().round(3))

# print("\nSurvival rate by parch:")
# print(df.groupby("parch")["survived"].mean().round(3))

# print(df["survived"].value_counts())
# print(df["survived"].value_counts(normalize=True).round(3))

# value_counts() gives the number of passengers in each class.
# normalize=True gives the proportions instead.


# print(df["sex"].value_counts())
# print(df["age"].describe())
# print(df["survived"].value_counts())

# now we are going to do plot visualization

import matplotlib.pyplot as plt
import seaborn as sns

# sns.countplot(data=df, x="survived")
# plt.title("Passenger Survival Counts")
# plt.xlabel("Survived (0 = No, 1 = Yes)")
# plt.ylabel("Number of Passengers")
# plt.show()

# print(df['survived'].value_counts())

# sns.histplot(data=df, x="age", bins=30, kde=True)
# plt.title("Distribution of Passenger Ages")
# plt.xlabel("Age")
# plt.ylabel("Frequency")
# plt.show()

# sns.boxplot(data=df, x="survived", y="age")
# plt.title("Age vs Survival")
# plt.xlabel("Survived (0 = No, 1 = Yes)")
# plt.ylabel("Age")
# plt.show()

# sns.countplot(data=df, x="sex", hue="survived")
# plt.title("Survival by Sex")
# plt.show()

# print(df["survived"].unique())