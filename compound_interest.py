principal = 0
rate = 0
time = 0

while principal <= 0:
    principal = float(input("enter principal amount: "))
    if principal <= 0:
        print("principal cannot be equal to zero")


while rate <= 0:
    rate = float(input("enter the interest  rate: "))
    if rate <= 0:
        print("interest rate cannot be equal to zero")

while time <= 0:
    time = int(input("enter time: "))
    if time <= 0:
        print("time cannot be equal to zero")

# print(principal)
# print(rate)
# print(time)

total = principal * pow((1 + rate / 100), time)
print(f"balance after {time} year is {total:.2f}")
