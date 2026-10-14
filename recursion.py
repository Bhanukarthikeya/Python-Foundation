# def countdown(n):
#     if n == 0:
#         print("blast off")
#     else:
#         print(n)
#         countdown(n-1)

# countdown(5)

# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fact(n-1)

# print(fact(5))

# def total(nums):
#     if len(nums) == 0:
#         return 0
#     else:
#         return nums[0] + total(nums[1:])

# print(total([3,4,5,6]))

# def nums(n):
#     if n == 0:
#         return
#     nums(n -1)
#     print(n)

# nums(5)

# def nums(n):
#     if n == 0:
#         return
#     print(n)
#     nums(n-1)
# nums(5)

# def sum(n):
#     if n == 0:
#         return 0
#     else:
#         return n + sum(n-1)

# print(sum(7))

# def num(number):
#     if number < 10:
#         return 1
#     return 1 + num(number // 10)

# print(num(1239438949))

# def sum(n):
#     if n < 10:
#         return n
#     else:
#         return n % 10 + sum(n//10)

# print(sum(12345))

def rev(name):
    if len(name) == 1:
        return name
    else:
        return rev(name[1:]) + name[0]
