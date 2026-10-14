
# n = 153
# result = 0
# num = n
# nod = len(str(n))
# while num > 0:
#     ld = num % 10
#     result += ld ** nod
#     num = num // 10

# print(result == n)
# print("hello")

# n = 10
# num = n
# list = []
# for i in range(1,num +1 ):
#     if num % i == 0:
#         list.append(i)
# print(list)

# from math import *
# result = []
# num = 36
# for i in range(1,int(sqrt(num)) + 1):
#     if num % i == 0:
#         oth = num // i
#         result.append(i)
#         result.append(oth)
# print(result)

# n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
# m = [10, 111, 1, 9, 5, 67, 2]

# freq_map = dict()
# for num in n:
#     freq_map[num] = freq_map.get(num, 0) + 1

# for num in m:
#     if num < 1 or num > 10:
#         print(0)
#     else:
#         print(freq_map.get(num, 0))

# def func(i,n):
#     if i > n:
#         return
#     func(i+ 1,n)
#     print(i)

# func(1,7)


# nums =  [5,9,4,11,6,2,1,3,7]
# n = len(nums)
# for i in range(0,n):
#     max_ind = i
#     for j in range(i+1,n):
#         if nums[j] > nums[max_ind]:
#             max_ind = j
#     nums[max_ind],nums[i] = nums[i],nums[max_ind]

# print(nums)


# def merge_array(left,right):
#     result = []
#     i,j = 0,0
#     n,m = len(left),len(right)
#     while i < n and j < m:
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j+=1
#     if i < n:
#         while i < n:
#             result.append(left[i])
#             i +=1
#     if j <m:
#         while j < m:
#             result.append(right[j])
#             j += 1
#     return result

# def merge_sort(nums):
#     if len(nums)<=1:
#         return nums
#     mid = len(nums)//2
#     left_arr = nums[:mid]
#     right_arr = nums[mid:]
#     left = merge_sort(left_arr)
#     right = merge_sort(right_arr)
#     return merge_array(left,right)

# print(merge_sort([1,1,2,6,7,9,4,4,6,8,4,8,9,9,8,6,4,3,2,5]))


# sorting

# selection sort
# nums = [5,7,8,4,1,6,9,2]
# n = len(nums)
# for i in range(0,n):
#     min_ind = i
#     for j in range(i +1,n):
#         if nums[j] < nums[min_ind]:
#             min_ind = j
#     nums[i] , nums[min_ind] = nums[min_ind], nums[i]
# print(nums)

# bubble sort

# nums = [5,7,8,4,1,6,9,2]

# for i in range(len(nums)-2,-1,-1):
#     for j in range(0,i+1):
#         if nums[j] > nums[j+1]:
#             nums[j],nums[j+1] = nums[j+1],nums[j]
# print(nums)

# insertion sort

# nums = [5,7,8,4,1,6,9,2]
# n = len(nums)
# for i in range(1,n):
#     key = nums[i]
#     j = i-1
#     while j >= 0 and nums[j] > key:
#         nums[j+1] = nums[j]
#         j -=1
#     nums[j+1] = key
# print(nums)

# merge sort

# nums1 = [1, 1, 1, 2, 4, 6, 7]
# nums2 = [1, 2, 3, 6, 7, 8, 9, 10]
# result = []

# for i in range(len(nums1)):
#     for j in range(len(nums2)):
#         if nums1[i] not in result:
#             result.append(nums1[i])
#         if nums2[j] not in result:
#             result.append(nums2[j])

# print(result)

# for i in range(len(nums1)):
#     if nums1[i] not in result:
#         result.append(nums1[i])

# for i in range(len(nums2)):
#     if nums2[i] not in result:
#         result.append(nums2[i])
# print(result)

# nums = [9,6,4,2,3,5,7,0,1]
# # n = len(nums)
# for i in range(0,n+1):
#     if i not in nums:
#         print(i)

# n = sum(nums)
# print(n)

# nums = [1,1,0,0,1,1,1,1]
# maxi = 0
# count = 0
# for i in range(0,len(nums)):
#     if nums[i] == 1:
#         count += 1
#     else:
#         count = 0
#     maxi = max(maxi,count)
# print(maxi)

# nums = [1,99,101,98,2,5,3,99,100]
# greatest = 0

nums = [0,1,3,5,4]
n = len(nums) -1
sum1 = (n) * (n-1) / 2
sum2 = sum(nums)
print(sum2 - sum1)