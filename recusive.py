# def fact(n):
#     if n ==1:
#         return 1
#     return n*fact(n-1)
# print(fact(5))

# print("hello")
# def sum(number):
#     if number < 10:
#         return number
#     add = 0
#     while number>0:
#         add += number % 10
#         number //=10
#     return sum(add)
# print(sum(2888))

def fact(n):
    if n ==1 or n == 0:
        return 1
    return n * fact(n-1)
print(fact(5))