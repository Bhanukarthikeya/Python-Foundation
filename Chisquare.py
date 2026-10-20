import numpy as np
import seaborn as sns
from scipy.stats import chi2_contingency
import pandas as pd

df = sns.load_dataset("titanic")
# first we need to see in this data which are categorical
# lets see is there any relation in gender and survived

contingency_table = pd.crosstab(df['sex'],df['survived'])
print(contingency_table)
chi2,p_values, dof, expected = chi2_contingency(contingency_table)
print(p_values)
print(expected)
print(chi2)

alpha = 0.05
if p_values < alpha:
    print("we reject the null hypothesis and there is a significant relationship btw gender and survior")
else:
    print("there is no significant difference")

