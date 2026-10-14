tickets = 200
while True:
    n = int(input("number of tickets: "))
    
    
    if tickets - n < 0:
        print("tickets not available")
        continue
    tickets -= n
    print(f"no of tickets left are {tickets}")
    if tickets == 0:
        print("sold out")
        break
