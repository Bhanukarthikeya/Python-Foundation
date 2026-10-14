# class = car blueprint
# object = actual car
# properties(colour,brand,speed)
# behaviors(start,stop,accelerate)

# class car:
#     pass         # creates blueprint  called car
# car_1 = car()
# print(car1)     #car 1 is an object

# variables inside class
# class car:
#     def __init__(self,brand,colour):
#         self.brand = brand
#         self.colour = colour

# car1 = car("BMW" , "Black")

# print(car1.colour,car1.brand, end = " ")


# Functions inside classes

# class student:
#     def __init__(self,name):
#         self.name = name
#     def introduce(self):
#         print(f"my name is {self.name}")

# s1 = student("karthik")
# s2 = student("bhanu")


# s1.introduce()
# print(s2.name)


# Encapsulation - bundling data and methods together

# class bankaccount:
#     def __init__(self,balance):
#         self.balance = balance

#     def deposit(self, deposit_amount):
#         self.balance += deposit_amount

#     def withdraw(self, withdraw_amount):
#         if withdraw_amount > self.balance:
#             print('insufficient balance')
#             pass
#         else:
#             self.balance -= withdraw_amount

# acc1 = bankaccount(10000)
# acc1.deposit(5000)
# acc1.withdraw(14999)
# print(acc1.balance)


# Inheritance - one class can reuse another class

# class animal:
#     def speak(self):
#         print('animal speaks')

# class dog(animal):
#     pass

# dog = dog()
# dog.speak()


# class animal:
#     def eat(self):
#         print('eating')

# class dog(animal):
#     def bark(self):
#         print('barking')

# d = dog()
# d.eat()
# d.bark()


# Polymorphism - same method name, different behavior

# class dog:
#     def sound(self):
#         print('bark')

# class cat:
#     def sound(self):
#         print('meow')

# animals = [dog(),cat()]

# for animal in animals:
#     animal.sound()

# Abstraction - hide unnecessary details


# practice

# class laptop:
#     def __init__(self,brand,ram):
#         self.brand = brand
#         self.ram = ram

#     def show_info(self):
#         print(f'Brand = {self.brand},ram = {self.ram}')

# s1 = laptop("HP","16 GB")
# s1.show_info()


# class animal:
#     def speak(self):
#         print('animal is speaking')

# class dog(animal):
#     def bark(self):
#         print('dog is barking')

# d = dog()

# d.speak()
# d.bark()

# super().__init__()

# class Person:
#     def __init__(self,name):
#         self.name = name

# class Student(Person):
#     def __init__(self,name,roll_no):
#         super().__init__(name)
#         self.roll_no = roll_no

# s = Student('karthik',101)

# print(s.name,s.roll_no)


# class animal:
#     def __init__(self,name):
#         self.name = name

# class dog(animal):
#     def __init__(self,name,breed):
#         super().__init__(name)
#         self.breed = breed

# d = dog('rocky','golden retriver')

# print(d.name)
# print(d.breed)

# practice

# class vehicle:
#     def __init__(self,brand):
#         self.brand = brand

# class car(vehicle):
#     def __init__(self,brand,model):
#         super().__init__(brand)
#         self.model = model

# c1 = car("BMW","M5")
# print(f'brand = {c1.brand}')
# print(f'model = {c1.model}')


# method overriding

# class animal:
#     def speak(self):
#         print('animal sound')

# class dog(animal):
#     def speak(self):
#         print('bark')

# d = dog()
# d.speak()


# class variable


# class student:
#     class_year =  2026       #class variable
#     num_students = 0

#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         student.num_students += 1

# stu1 = student("bhanu",50)
# stu2 = student("karthikeya",45)

# print(student.num_students)

# multiple inheritance
# class animal:

#     def __init__(self,name):
#         self.name = name

#     def eat(self):
#         print(f'{self.name} eating')

#     def sleep(self):
#         print(f'{self.name} sleeping')

# class prey(animal):
#     def flee(self):
#         print(f'{self.name} is fleeing')


# class predator(animal):

#     def hunt(self):
#         print(f'{self.name} is hunting')


# class rabbit(prey):
#     pass


# class hawk(predator):
#     pass


# class fish(predator,prey):
#     pass

# rabbit = rabbit("eheh")
# hawk = hawk('hehe')
# fish = fish('wowow')

# hawk.hunt()
# rabbit.flee()
# fish.flee()
# fish.hunt()
# fish.eat()

# polymorphism
# from abc import ABC, abstractmethod

# class shape:

#     @abstractmethod
#     def area(self):
#         pass

# class circle(shape):
#     def __init__(self,radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius ** 2


# class square(shape):
#     def __init__(self,side):
#         self.side = side

#     def area(self):
#         return self.side ** 2

# class triangle(shape):
#     def __init__(self,base,height):
#         self.base = base
#         self.height = height

#     def area(self):
#         return self.base *self.height * 0.5

# class pizza(circle):
#     def __init__(self,topping,radius):
#         super().__init__(radius)
#         self.topping = topping


# shapes = [circle(4),square(5),triangle(6,7),pizza("pepperoni",5)]


# for shape in shapes:
#     print(shape.area())


# Duck typing - another way to achieve polymorphism besides inheritance

# class animal:
#     alive = True

# class dog(animal):
#     def speak(self):
#         print('woof')

# class cat(animal):
#     def speak(self):
#         print('meow')

# class car:

#     alive = False

#     def speak(self):
#         print('honk')


# animals = [dog(), cat(),car()]

# for animal in animals:
#     animal.speak()
#     print(animal.alive)


# static methods - a method that belong to a class rather than any object from the class(instance usually used for general utility functions)

# class employee:

#     def __init__(self,name,position):
#         self.name = name
#         self.position = position

#     def get_info(self):
#         return f'{self.name} = {self.position}'

#     @staticmethod
#     def is_valid_position(position):   # no need of object in class
#         valid_positions = ['manager','cashier','janitor','cook']
#         return position in valid_positions


# employee1 = employee('bhanu' , 'manager')
# employee2 = employee('karthik' , 'cook')

# # print(employee.is_valid_position('cook'))
# print(employee1.get_info())
# print(employee2.get_info())

