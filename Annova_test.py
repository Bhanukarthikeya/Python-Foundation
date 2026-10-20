import seaborn as sns
import pandas as pd
from scipy.stats import f_oneway

df = sns.load_dataset("titanic")
print(df)
df = df[['age','p_class']].dropna()

print(df["pclass"].unique())


class_1 = df[df['pclass'] == 1]['age']
class_2 = df[df['pclass'] == 2]['age']
class_3 = df[df['pclass'] == 3]['age']

f_stats,p_value = f_oneway(class_1,class_2,class_3)
print(f_stats)
print(p_value)

alpha = 0.05
if p_value < alpha:
    print("reject the null hypothesis")
else:
    print("there is no significant difference ")

