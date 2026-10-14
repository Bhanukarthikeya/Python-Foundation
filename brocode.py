# conditional operator - one line short-cut for the if else statement (ternary operator)
# print or assign one of two values based on a condition
#                       X if condition else Y

# num = 5
# print("positive" if num > 0 else "negative")
# print("EVEN" if num%2 == 0 else "ODD")

# string methods

# name = input('enter your full name: ')
# phone_number = input("enter your phone number: ")
# result = len(name)
# print(name.find("a"))
# print(name.rfind("a"))
# print(name.capitalize())
# print(name.upper())
# print(name.lower())
# print(name.isdigit())
# print(name.isalpha())
# print(phone_number.count("-"))
# phone_number.replace("-"," ")
# print(help(str))


# print(result)


# user_name = input("enter a valid username: ")

# if len(user_name) > 12:
#     print("your username is too long")

# elif not user_name.find(" ") == -1:
#     print("your username cant contain spaces")

# elif not user_name.isalpha():
#     print("your username cant contain numbers")

# else:
#     print(f"welcome {user_name}")

# indexing = accessing elements of a sequence using [] [start: end : step]

# credit_number = "1234-5678-9012-3456"

# print(credit_number[0])
# print(credit_number[0:4])
# print(credit_number[5:9])
# print(credit_number[5:])
# print(credit_number[-1])
# print(credit_number[::2])
# print(credit_number[::-1])

# format specifiers

# while loops

# age = int(input("enter age: "))

# while age < 0:
#     print("age cant be negative")
#     age = int(input("enter age: "))

# print(age)

# food = input("enter a food you like(q to quit): ")

# while not food == "q":
#     print(f"you like food {food}")
#     food = input("enter a food you like(q to quit): ")

# num = input("enter a number btw (1 - 10): ")

# while num < 1 or num > 10:
#     print(f"{num} not valid")
#     num = input("enter a number btw (1 - 10): ")

# for loops

# for i in range(1,11):
#     print(i)

# for i in range(21):
#     if i == 15:
#         continue
#     else:
#         print(i)

# collection of data - lists[] - ordered and changeable. duplicates OK
#                      set{} - unordered and immutable, but add/remove - OK, duplicates - NO
#                      tuple() -  ordered and unchangeable. duplicates OK, FASTER

# fruits = ["apple", "banana", "orange", "coconut"]
# for fruit in fruits:
#     print(fruit)

# print(fruits[1])
# print(fruits[::-1])
# print(len(fruits))
# print("apple" in fruits)
# fruits[0] = "pineapple"
# fruits.append("pineapple")
# fruits.remove("apple")
# fruits.insert(0,"pineapple")
# fruits.sort
# fruits.reverse
# fruits.clear
# print(fruits.index("apple"))
# print(fruits.count("banana"))
# fruits.pop()
# print(fruits)

# print(dir(fruits))
# print(help(fruits))

# dictionary - a collection of {key:value} pairs, ordered and changeable, NO duplicates

# capitals = {"USA": "washington D.C",
#             "india": "new delhi"}

# print(dir(capitals))
# print(help(capitals))

# capitals.get("USA")
# capitals.update({"germany": "berlin"}) # adding new data
# capitals.update({"USA": "detroid"})  # update the existing data
# capitals.pop("india")
# capitals.popitem()
# capitals.clear()
# keys = capitals.keys()
# values = capitals.values()
# items = capitals.items()
# for key,value in capitals.items():
#     print(f"{key}: {value}")

# random

# import random
# die = random.randint(1,6)
# print(die)

# number =  random.randint(0,1) # gives a random floating point number from 0-1
# print(number)

# options = ("rock", "paper", "scissors")
# print(random.choice(options))

# cards = ["2","3","4","7","9","8"]
# random.shuffle(cards)
# print(cards)

# functions

# def happy_birthday(name,age):
#     print(f"happy birthday to {name} and you are {age} years old")

# happy_birthday(name="bro",age=20)
# happy_birthday(name="steve",age=30)

# def display_invoice(username,amount,due_date):
#     print(f"hello {username}")
#     print(f"your bill of {amount} is due: {due_date}")


# display_invoice("bhanu" 100000, "01/01")

# return - statement used to end a function and send a result back to thr caller

# def add(x,y):
#     z = x + y
#     return z

# print(add(3,4))


# def create_name(first, last):
#     first = first.capitalize()
#     last = last.capitalize()
#     return first+ " " + last

# full_name =  create_name("bro","code")
# print(full_name)


# default arguments -  a default value for certain parameters
#                      default is used when the argument is omitted
#                      make your function more flexible, reduces # fo arguments
#                      1. position 2. default 3. keyword 4. arbitrary

# default arguments

# def net_price(list_price,discount = 0,tax = 0.05):
#     return list_price* (1+tax)* (1- discount)

# print(net_price(500))
# print(net_price(500,0.1))


# import time
# def count(end,start = 0):
#     for i in range(start,end +1):
#         print(i)
#         time.sleep(1)

# count(0,10)

# keyword arguments -  an argument preceded by a identifier
#                      helps with readability
#                      order of arguments doesnt matter
#                      1. positional 2. default 3. keyword 4.arbitrary

# def hello(greeting,title,first,last):
#     print(f"{greeting} {title} {first} {last}")

# hello(greeting = "hello",title="Mr.", first="spongebob",last= "squarepants")

# for i in range(1,11):
#     print(i,end = " ")

# print("1","2","3","4",sep = "-")

# args - allows you to pass multiple non-key arguments
# kwargs - allows you to pass multiple key-word arguments
#           * unpacking operator

# def add(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     return total

# print(add(1,2,3,4,5))

# def display_name(*args):
#     for arg in args:
#         print(arg, end = " ")

# display_name("palak","kumari")

# iterables =  an object/collection that can return its element one at a time,
#              allowing it to be iterable over in a loop

# numbers = [1,2,3,4,5]

# for num in numbers:
#     print(num)

# for num in reversed(numbers):
#     print(num)

# my_dict = {"A": 1,"B": 2,"C": 3}

# for key,value in my_dict.items():
#     print(f"{key}: {value}")

# membership operators - used to test weather a value or variable is found in a sequence( string,list,tuple,set and dictonary)
#                        1. in      2. not in

# word = "apple"

# letter = input("guess a letter in a secret word: ")
# if letter in word:
#     print(f"there is a {letter}")
# else:
#     print(f"{letter} is not found")

# students = ["spongebob", "patrick" , "sandy"]
# student = input("enter a name of student: ")
# if student in students:
#     print(f"{student} is a student")
# else:
#     print(f"{student} not found")

# list comprehension - a concise way to create lists in python
#                      compact and easier to read than traditional loops
#                      [expression for value in iterable if condition]

# doubles = []
# for i in range(1,11):
#     doubles.append(i*2)

# print(doubles)

# doubles = [i *2 for i in range(1,11)]
# triples = [j *3 for j in range(1,11)]

# fruits = ["apple","orange","banana","coconut"]
# fruits = [fruit.upper() for fruit in fruits]

# numbers = [1,-2,3,-4,5,-6]
# positive = [num for num in numbers if num>=0]
# negative = [num for num in numbers if num<0]
# even = [num for num in numbers if num%2==0]
# odd = [num for num in numbers if num%2 != 0]

# module - a file containing code you want to include in your program
#          use import to include a module (built-in or your own)
#          useful to break up a large program reusable separate files


# join function - join() is a string method used to combine multiple stings into one sting
# "separator".join(iterable)

# words = ["hello", "world"]
# result =  " ".join(words)

# exception handling

# exception = an event that interrupts the flow  of a program (ZeroDivisionError,typeerror, value error)
#             1.try , 2.except , 3.finally

# try:
#     number = int(input("enter a number: "))
#     print(1/number)
# except ZeroDivisionError:
#     print("you cant divide by zero idiot")
# except ValueError:
#     print("enter only numbers please")
# except Exception:
#     print("something went wrong")
# finally:
#     print("Do some cleanup here")

# python file detection

# relative file path

# import os

# file_path = "test.txt" # relative filepath this is which this text will be in vs code
# file_path = "stuff/test.txt" # relative filepath this is which this text will be in vs code

# if os.path.exists(file_path):
#     print(f"the location {file_path} exists")
# else:
#     print("that location doesnt exists")

# absolute file path

# import os


# file_path = "C:/Users/bhanu/OneDrive/Desktop" # relative filepath this is which this text will be in vs code

# if os.path.exists(file_path):
#     print(f"the location {file_path} exists")

#     if os.path.isfile(file_path):
#         print("that is a file")

#     elif os.path.isdir(file_path):
#         print("that is a directory")

# else:
#     print("that location doesnt exists")


# python writing files (.txt, .json, .csv)

# txt_data = "i like pizza"

# file_path = "output.txt"

# with open(file = file_path,mode = 'w') as file:
#     file.write(txt_data)
#     print(f"txt file '{file_path} was created")

# txt_data = "i like pizza"

# file_path = "output.txt"

# with open(file = file_path,mode = 'a') as file:
#     file.write(txt_data)
#     print(f"txt file '{file_path} was created")

# employees = ['bhanu','karthikeya','palak','kumari']

# file_path = "C:/Users/bhanu/OneDrive/Desktop/output.txt"

# try:
#     with open(file_path,"w") as file:
#         for employee in employees:
#             file.write(employee,end = " ")
#         print(f"txt file {file_path} was created")
# except FileExistsError:
#     print("this file already exists")

# import json

# employee = {
#     "name": "spongebob",
#     "age": 30,
#     "job": "cook"
# }

# file_path = "C:/Users/bhanu/OneDrive/Desktop/output.json"

# try:
#     with open(file_path, "w") as file:
#         json.dump(employee, file, indent=4 )
#         print(f"json file {file_path} is created")
# except FileExistsError:
#     print("that file already exists")


# import json
# import csv

# employees = [["name", "age,", "job"],
#              ["bhanu", 30, "Cook"],
#              ["palak", 19, "manager"],
#              ["karthikeya", 35, "sweeper"]]

# file_path = "C:/Users/bhanu/OneDrive/Desktop/output.csv"

# try:
#     with open(file_path, "w", newline="") as file:
#         writer = csv.writer(file)
#         for row in employees:
#             writer.writerow(row)
#         print(f"csv file {file_path} is created")
# except FileExistsError:
#     print("that file already exists")

# file_path = "C:/Users/bhanu/OneDrive/Desktop/bro_code"
# try:
#     with open(file_path, "r") as file:
#         content = file.read()
#         print(content)
# except FileExistsError:
#     print("that file was not found")
# except PermissionError:
#     print("you do not permission to access this file")

# import json

# file_path = "C:\Users\bhanu\OneDrive\Desktop/bro_code.json"

# try:
#     with open(file_path,"r") as file:
#         content = json.load(file)
#         print(content)
# except FileNotFoundError:
#     print("file not found")


# import csv

# file_path = "C:\Users\bhanu\OneDrive\Desktop/bro_code.csv"

# try:
#     with open(file_path,"r") as file:
#         content = csv.reader(file)
#         for line in content:
#             print(line)
#         print(content)
# except FileNotFoundError:
#     print("file not found")


