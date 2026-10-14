a = 0
b = 1
for i in range(11):
    c = a+b
    a = b
    b = c
    print(c)