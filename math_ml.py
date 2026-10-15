# outliers code

import numpy as np
arr = np.array([2, 3, 4, 6, 7, 8, 9, 12, 13, 16, 17, 23, 27, 34, 37, 201])
Q1 = np.percentile(arr, 25)
Q3 = np.percentile(arr, 75)
IQR = Q3 - Q1
upper_fence = Q3 + 1.5 * IQR
lower_fence = Q1 - 1.5 * IQR
new_arr = arr[(arr >= lower_fence) & (arr < upper_fence)]
print(new_arr)
