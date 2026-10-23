import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings('ignore')
df = pd.read_csv("insurance.csv")
print(df)

# EDA

print(df.shape)

print(df.head()) 
print(df.info())    # gives us the datatype of the column
print(df.describe())  # gives mean,mode,median,std,25,50,75,max,min
print(df.isnull().sum()) # no null values in this insurance data set

numeric_columns = ["age","bmi","children","charges"]
for col in numeric_columns:
    plt.figure(figsize = (6,4))
    sns.histplot(df[col],kde = True,bins = 20)

sns.countplot(x = df["children"])
sns.countplot(x = df["smoker"])
plt.show()

# # input and output comparison(visualization)

for col in numeric_columns:
    plt.figure(figsize=(6,4))
    sns.boxplot(x = df[col])
plt.show()

plt.figure(figsize=(8,6))
sns.heatmap(df.corr(numeric_only=True),annot=True)
plt.show()

# data cleaning and preprocessing

df_cleaned = df.copy()
df_cleaned.drop_duplicates(inplace=True)
df_cleaned.isnull().sum()
df_cleaned.dtypes

df_cleaned["sex"].value_counts()  # this is to check weather the data given is containing only male and females ex it might contain Male so

# now converting objects in numeric terms (encode)
# label encoding for gender and smoker
df_cleaned["sex"] = df_cleaned["sex"].map({"male": 0,
                                           "female": 1}) # updating male and female to 0 and 1

df_cleaned["smoker"] = df_cleaned["smoker"].map({"yes": 1,
                                                 "no": 0})

df_cleaned.rename(columns={"sex": "is_female",
                           "smoker": "is_smoker"},inplace=True)

# one-hot encoding for region

df_cleaned = pd.get_dummies(df_cleaned,columns=["region"],drop_first=True)
df_cleaned = df_cleaned.astype(int)

# Feature Engineering

sns.histplot(df["bmi"])
plt.show()

# bins

df_cleaned["bmi_category"] = pd.cut(
    df_cleaned["bmi"],
    bins = [0,18.5,24.9,29.9,float('inf')],
    labels=['underweight','normal','overweight','obese'])

df_cleaned = pd.get_dummies(df_cleaned,columns=["bmi_category"],drop_first=True)
df_cleaned = df_cleaned.astype(int)
print(df_cleaned.head())

# Feature scaling

df_cleaned.columns  # we need to change scale of bmi,age and children

from sklearn.preprocessing import StandardScaler
col = ['age','bmi','children']
scaler = StandardScaler()

df_cleaned[col] =scaler.fit_transform(df_cleaned[col]) # change of scale is done
print(df_cleaned.head())

# Feature Extraction
# pearson correlation

from scipy.stats import pearsonr

# list of features to check against target
selected_features = ['age','bmi','children','is_female','is_smoker','region_northwest','region_southeast','region_southwest',
                     'bmi_category_normal','bmi_category_overweight','bmi_category_obese']

correlations = {
    feature: pearsonr(df_cleaned[feature],df_cleaned['charges'])[0]
    for feature in selected_features
}

correlation_df = pd.DataFrame(list(correlations.items()),columns = ['Feature','pearson correlation'])
correlation_df.sort_values(by='pearson correlation',ascending= False) 
# print(correlation_df) # result we will come in between -1 to 1 in this data set is_smoker is highest
# now if correlations is above .50 or below -.50 then there must be a positive or negitive correlation (highly correlated must use)
#.2 to .5 also need to be considered 
# .1 to .2 in this case first we need to see and trial and error like that mean suppose if children comes under this .1 to .2 first 
# we need to test the model accuracy using children and nest without children we will compare if with children is more accurate then 
# children must be there (hit and trail) 
# here region_northwest and region_southwest is very very less correlated to target so we can remove it

# next chi square test - for categorical variables

cat_features = ['is_female','is_smoker','region_northwest','region_southwest','region_southeast','bmi_category_normal','bmi_category_overweight','bmi_category_obese']

from scipy.stats import chi2_contingency
import pandas as pd
alpha = 0.05
df['charges_bin'] = pd.qcut(df['charges'],q = 4,labels=False)
chi2_result = {}

for col in cat_features:
    contingency = pd.crosstab(df[col],df['charges'])
    chi2_stat, p_val,_,_ = chi2_contingency(contingency)
    decision = "reject null(keep feature)" if p_val <alpha else "accept null(drop feature)"
    chi2_result[col] = {
        'chi2_statistic': chi2_stat,
        'p_value': p_val,
        'Decision': decision   
    }
chi2_df = pd.DataFrame(chi2_result)
chi2_df = chi2_df.sort_values(by = 'p_value')
print(chi2_df)
# remove the unwanted features here

# DONEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE

