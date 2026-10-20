import numpy as np
from scipy import stats
sample1 = [85,88,90,92,87,85,89,91,86,88]
sample2 = [82,84,80,83,81,79,78,85,84,83]
# T-test p-values

t_stats,p_value = stats.ttest_ind(sample1,sample2,equal_var=False)

print(t_stats)
print(p_value)

alpha = 0.05
if p_value < alpha:
    print("i will reject the hypothesis")
else:
    print("i accept the hypothesis")

