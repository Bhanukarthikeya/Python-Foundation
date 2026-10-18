# using p values for z test
import numpy as np
import scipy.stats as norm

# by mistake we have taken sample size less than 30 but its just for example
sample = [172, 174, 168, 169, 171, 173, 175, 170, 169, 172]
population_mean = 170
population_std = 3
sample_mean = np.mean(sample)
n = len(sample)
z_score = (sample_mean - population_mean)/(population_std / np.sqrt(n))
alpha = 0.05
# we will get one p value this will come p_value = 0.1705
p_value = 2 * (1 - norm.cdf(abs(z_score)))

if p_value < alpha:
    print("i will reject the null hypothesis")
else:
    print("i will accept the null hypothesis")

# output for this code is i will accept the null hypothesis

# now lets see for critical values


# by mistake we have taken sample size less than 30 but its just for example
sample = [172, 174, 168, 169, 171, 173, 175, 170, 169, 172]
population_mean = 170
population_std = 3
sample_mean = np.mean(sample)
n = len(sample)
z_score = (sample_mean - population_mean)/(population_std / np.sqrt(n))
alpha = 0.05
# if alpha is 0.05 and it is two tailed then the critical value is 1.96 according to z table
# so here we will compare z_score with the the critical value
