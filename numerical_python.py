import numpy as np

# print(np.__version__)

# arrays

# array = np.array([1,2,3,4])
# array = array * 2
# print(array)
# print(type(array))

# --multidimensional arrays-------------------------------------------

# array = np.array('A')
# print(array.ndim)     #0 dimensional array

# array = np.array(['A','B','C'])
# print(array.ndim)          #1 dimensional array

# array = np.array([['A','B','C'],[1,2,3],[4,5,6]])
# print(array.ndim)           #2 dimensional array or matrix

# array = np.array([[['A','B','C'],[1,2,3],[4,5,6]], 
#                 [['d','e','f'],[11,22,33],[44,55,66]], 
#                 [['v','a','h'],[111,222,333],[444,555,666]]])   #everything should have 3 elements not possible 2

# print(array.ndim)         #3 dimensional array
# print(array.shape)        #(3,3,3)   3 layers,3 rows,3 coloums


# print(array[0][0][0])   chain indexing normal python
# print(array[0,0,0])   multidimensional indexing  faster

# word = array[0,0,0] + array[2,0,0]

# print(word)     Av  

# numpy slicing--------------------------------------------

# array = np.array([[1,2,3,4],
#                  [5,6,7,8], 
#                  [9,10,11,12], 
#                  [13,14,15,16]])

# array[start:end:step]

# print(array[0])   # 1,2,3,4
# print(array[-1])   #13,14,15,16
# print(array[0:3]) 
# print(array[0:4:2])                   ROWS
# print(array[::-1])

# column---------

# print(array[:,0])        #1,5,9,13
# print(array[:,0:4])
# print(array[0:2,2:4])

# scalar arithmetic in numpy--------------------------------------------------

# array = np.array([1,2,3])

# print(array + 1)
# print(array  - 2)
# print(array * 3)
# print(array / 4)
# print(array ** 5)

# vectorized math functions-------------------------------------------------------

# radii = np.array([1,2,3])
# array = np.array([1,2,3])

# print(np.sqrt(array))
# print(np.round(array))   # floor and ceiling
# print(np.floor(array))   # floor and ceiling
# print(np.ceil(array))   # floor and ceiling
# print(np.pi)

# print(radii ** 2 * np.pi)

# element-wise arithmetic----------------------------------------------------

# array1 = np.array([1,2,3])
# array2 = np.array([4,5,6])

# print(array1 + array2)
# print(array1 - array2)
# print(array1 * array2)
# print(array1 / array2) 
# print(array1 ** array2)

# comparison operators----------------------------------------------------------

# scores = np.array([91,55,100,73,82,64])

# print(scores == 100) # boolean
# print(scores >= 60)  # boolean

# scores[scores < 60] = 0
# print(scores)


# broadcasting------------------------------------------------------------------------

# broadcasting allows numpy to perform operations on arrays
# with different shapers by virtually expanding dimentions
# so they match the larger arrays shape

# the dimensions have the same size
# or 
# one of thr dimensions has a size of 1

# array1 =np.array([[1,2,3,4]])
# array2 = np.array([[1],[2],[3],[4]])
# print(array1.shape)
# print(array2.shape)

# print(array1 * array2)   #case 2              

# array1 =np.array([[1,2,3,4],
#                 [5,6,7,8],
#                 [9,10,11,12],
#                 [13,14,15,16]])
# array2 = np.array([[1],[2],[3],[4]])
# print(array1.shape)
# print(array2.shape)     

# print(array1 * array2)       #case 1

# array1 = np.array([[1,2,3,4,5,6,7,8,9,10]])
# array2 = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])

# print(array1.shape)
# print(array2.shape)
# print(array1 * array2)


# aggregate functions--------------------------------------------------------------

# aggregate functions =  summarize data and typically return a single value

# array = np.array([[1,2,3,4,5],
#                   [6,7,8,9,10]])

# # print(np.sum(array))
# # print(np.mean(array))
# # print(np.std(array))   # standard deviation
# # print(np.var(array))   # variance 
# # print(np.min(array))
# # print(np.max(array))
# # print(np.(array))
# # print(np.argmin(array))   0 = index
# # print(np.argmax(array))   9 = index
# print(np.sum(array,axis = 0))       #summing all the coloums
# print(np.sum(array,axis = 1))       # summing all the rows



# filtering in numpy------------------------------------------------

# filtering refers to the process of selecting elements from an array that match the given condition

# ages = np.array([[21,17,19,20,16,30,18,65],
#                  [39,22,15,99,18,19,20,21]])

# teenagers = ages[ages < 18]
# adults = ages[(ages >= 18) & (ages < 65)]
# seniors = ages[ages >= 65]                           # these all will give a one dimentional array
# evens = ages[ages % 2 == 0]
# odds = ages[ages %2 != 0]

# adults = np.where(ages >= 18, ages, 0)           # the where function preserves the original shape of the arrays

# print(teenagers)
# print(adults)
# print(seniors)
# print(evens)

# random numbers----------------------------------------------

# rng = np.random.default_rng()

# print(rng.integers(low = 1,high = 101,size = (3,2)))

# print(np.random.uniform(-1,1,(3,2)))

# rng = np.random.default_rng()
# array = np.array([1,2,3,4,5])
# rng.shuffle(array)
# num = rng.choice(array)
# nums = rng.choice(array,size = 3)
# print(array)
# print(num)
# print(nums)

import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6]])

print(a.shape)  # (2, 3)
print(a.ndim)   # 2
print(a.size)   # 6


a = np.array([[1, 2, 3],
              [4, 5, 6]])

print(np.sum(a, axis=0))  # [5, 7, 9]
print(np.sum(a, axis=1))  # [6, 15]

a = np.array([10, 20, 30])
print(a - 10)  # [ 0 10 20]


a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

print(a * b)  # [10, 40, 90, 160]


A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print(A @ B)
# [[19 22]
#  [43 50]]



import numpy as np

a = np.array([1, 2, 3, 4, 5, 6])

# Convert 1D array into 2D array
print(a.reshape(2, 3))

# Flatten a multidimensional array
b = np.array([[1, 2], [3, 4]])
print(b.flatten())

# ravel() also flattens an array
print(b.ravel())

# Transpose rows and columns
print(b.T)

# Add a new dimension
print(a[:, np.newaxis].shape)  # (6, 1)

# Expand dimensions
print(np.expand_dims(a, axis=0).shape)  # (1, 6)


a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Join arrays
print(np.concatenate((a, b)))

# Stack vertically
print(np.vstack((a, b)))

# Stack horizontally
print(np.hstack((a, b)))

# Stack arrays along a new axis
print(np.stack((a, b), axis=0))

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Matrix multiplication
print(A @ B)

# Dot product
print(np.dot(A, B))

# Transpose
print(A.T)

# Identity matrix
print(np.eye(2))

# Inverse of a matrix
print(np.linalg.inv(A))

# Solve Ax = b
b = np.array([5, 11])
print(np.linalg.solve(A, b))

# Norm (magnitude)
print(np.linalg.norm([3, 4]))



a = np.array([1, 4, 9, 16])

print(np.sqrt(a))       # Square root
print(np.square(a))     # Squares
print(np.exp(a))        # Exponential
print(np.log(a))        # Natural logarithm
print(np.abs([-2, 3]))  # Absolute values
print(np.round([1.23, 4.56], 1))


a = np.array([10, 20, 30, 40, 50])

print(np.sum(a))                 # Sum
print(np.mean(a))                # Mean
print(np.median(a))              # Median
print(np.std(a))                 # Standard deviation
print(np.var(a))                 # Variance
print(np.min(a))                 # Minimum
print(np.max(a))                 # Maximum
print(np.argmin(a))              # Index of minimum
print(np.argmax(a))              # Index of maximum
print(np.percentile(a, 75))      # 75th percentile
print(np.clip(a, 15, 45))        # Limit values to a range
print(np.diff(a))                # Differences between neighbors
print(np.cumsum(a))              # Cumulative sum














