# from abc import ABC, abstractmethod
# from car import Car


# class element:
#     id_count = 1

#     def __init__(self, w, h, loc, mat):

#         self.width = w
#         self.height = h
#         self.location = loc
#         self.material = mat
#         self.id = self.gen_id()

#         print(f'creating an element<{self.id}>')

#     def gen_id(self):
#         el_id = element.id_count
#         element.id_count += 1
#         return el_id

#     def print_data(self):
#         print(f'element <{self.id}>')
#         print(f'material: {self.material}')
#         print(f'height: {self.height}')
#         print(f'width: {self.width}')
#         print(f'location: {self.location}')

#     def move(self, x, y):
#         print(f'moving an element <{self.id}> X:{x} , Y:{y}')
#         old_x = self.location[0]
#         old_y = self.location[1]
#         self.location = (old_x + x, old_y + y)


# elem_a = element(10, 20, (0, 0), 'wood')
# elem_b = element(15, 30, (10, 10), 'concrete')

# # print(elem_a.height,elem_b.width)

# # elem_a.height = 30
# # elem_a.width  = 40

# # print(elem_a.height,elem_a.width)

# elem_a.print_data()
# elem_b.print_data()


# inheritance


# class element:

#     def __init__(self):
#         print('element __init__ executed')
#         self.category = self.cat()

#     def cat(self):
#         return self.__class__.__name__

#     def move(self):
#         print(f'moving {self.cat()}')

#     def rotate(self):
#         print(f'rotating {self.cat()}')

#     def scale(self):
#         print(f'scaling {self.cat()}')


# class wall(element):
#     def __init__(self):
#         print('wall __init__ executed')

#     def move(self):
#         print('moving wall based on line')


# class Floor(element):

#     def __init__(self):
#         print('floor __init__ executed')

#     def move(self):
#         print('moving floor based on point')


# wall_a = wall()
# floor_a = Floor()

# wall_a.move()
# floor_a.move()


# car1 = Car("mustang", "2024", "red", True)
# car2 = Car("bmw", "2026", "pink", False)

# print(car1.model)
# print(car2.colour)

# methods


# class Car:
#     def __init__(self, model, year, colour, for_sale):
#         self.model = model
#         self.year = year                   # instance variables

#         self.colour = colour
#         self.for_sale = for_sale

#     def drive(self):
#         print(f"you drive the {self.year} {self.colour} {self.model} ")

#     def stop(self):
#         print(f"you stopped the {self.year} {self.colour} {self.model}")


# car1 = Car("mustang", "2024", "red", True)

# car1.stop()
# car1.drive()


# class variables = shared among all instances of a class


# defined outside the constructor
# allow you to share data among all objects created from that class


# class Student:

#     class_year = 2024     # class variable
#     num_students = 0

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         Student.num_students += 1


# stu1 = Student("bhanu", 30)
# stu2 = Student("karthikeya", 35)

# # here we cant know weather class_year is class variable or instance variable
# print(stu1.class_year)
# # here we can definately say that class_year is class variable
# print(Student.class_year)

# # inheritance - allows a class to inherit attributes and methods from another class
# #               allows with code reusability and extensibility
# #               class child(parent)


# class Animal:
#     def __init__(self, name):
#         self.name = name
#         self.is_alive = True

#     def eat(self):
#         print(f"{self.name} is eating")

#     def sleep(self):
#         print(f"{self.name} is sleeping")


# class Dog(Animal):

#     def speak(self):
#         print("woof")


# class Cat(Animal):

#     def speak(self):
#         print("meow")


# class Mouse(Animal):

#     def speak(self):
#         print("sqeak")


# dog = Dog('scooby')
# cat = Cat("garfeild")
# mouse = Mouse("mickey")

# print(dog.name)
# print(dog.is_alive)
# dog.sleep()
# dog.speak()

# multiple inheritance - inherit from more than one parent class
# C(A, B)
# multilevel inheritance - inherit from a parent while inherits from another parent
# C(B) < - B(A) < - A


# class Animal:

#     def __init__(self, name):
#         self.name = name

#     def eat(self):
#         print(f"{self.name} is eating")

#     def sleep(self):
#         print(f"{self.name} is sleeping")


# class Pray(Animal):

#     def flee(self):
#         print(f"{self.name} is fleeing")


# class Predator(Animal):

#     def hunt(self):
#         print(f"{self.name} is hunting")


# class Rabbit(Pray):
#     pass


# class Hawk(Predator):
#     pass


# class Fish(Pray, Predator):

#     pass


# class Lion(Predator):
#     pass


# rabbit = Rabbit("bugs")
# hawk = Hawk("tony")
# fish = Fish("nemo")
# lion = Lion("hehe")

# rabbit.flee()
# rabbit.hunt()   # wrong
# hawk.hunt()
# fish.hunt()
# fish.flee()
# lion.hunt()
# rabbit.sleep()
# fish.eat()

# abstract class - a class that cannot be instantiated on its own
# meant to be subclassed
# they can contain abstract methods, which are declared but have no implementation
# abstract class benefits:
#     1. prevents instantiation of the class itself
#     2. requires children to use inherited abstract methods


# class Vehicle(ABC):

#     @abstractmethod
#     def go(self):
#         pass

#     @abstractmethod
#     def stop(self):
#         pass

# # vehicle = Vehicle()  # error will occur


# class Car(Vehicle):

#     def go(self):
#         print("you drive the car")

#     def stop(self):
#         print("you stop the car")


# class Motorcycle(Vehicle):

#     def go(self):
#         print("you ride the motorcycle")

#     def stop(self):
#         print("you stop the motorcycle")


# motorcycle = Motorcycle()
# motorcycle.go()
# motorcycle.stop()
# car = Car()          # this abstract method class if we forget any method in a class which is inherited it gives type error
# # here in car or motorcycle if we miss any or both of go and stop methods it gives a error
# car.go()
# car.stop()

# super() - function used in a child class to call methods from a parent class (super class)
# allows you to extend the functionality of the inherited methods


# class Shape:
#     def __init__(self, color, filled):
#         self.color = color
#         self.filled = filled


# class Circle(Shape):
#     def __init__(self, color, filled, radius):
#         super().__init__(color, filled)
#         self.radius = radius


# class Square(Shape):
#     def __init__(self, color, filled, side):
#         super().__init__(color, filled)
#         self.side = side


# class Triangle(Shape):
#     def __init__(self, color, filled, width, height):
#         super().__init__(color, filled)
#         self.width = width
#         self.height = height


# circle = Circle("red", True, 5)
# print(circle.color)

# polymorphism = greek word that means to "have many forms or face"
# poly = many
# morph = face
# WAYS TO ACHIEVE POLYMORPHISM
# 1. inheritance = an object could be treated of the same type as a parent class
# 2. "duck typing" = object must have necessary attributes/methods


# class Shape:
#     @abstractmethod
#     def area(self):
#         pass


# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius ** 2


# class Square(Shape):

#     def __init__(self, side):
#         self.side = side

#     def area(self):
#         return self.side ** 2


# class triangle(Shape):

#     def __init__(self, base, height):
#         self.base = base
#         self.height = height

#     def area(self):
#         return 0.5 * self.base * self.height


# class Pizza(Circle):
#     def __init__(self, topping, radius):
#         super().__init__(radius)
#         self.topping = topping


# shapes = [Circle(4), Square(5), triangle(6, 7), Pizza("pepperoni", 15)]

# for shape in shapes:
#     print(shape.area())

# duck typing - another way to achieve polymorphism besides inheritance
# object must have minimum necessary attributes/methods
# "if it looks like a duck and quacks like a duck,it must be a duck"


# class Animal:
#     alive = True


# class Dog(Animal):

#     def speak(self):
#         print("woof")


# class Cat(Animal):

#     def speak(self):
#         print("meow")


# class Car:

#     alive = False

#     def speak(self):
#         print("honk")


# animals = [Dog(), Cat(), Car()]

# for animal in animals:
#     animal.speak()
#     print(animal.alive)

# aggregation - represents a relationship where one object(the whole)
# contains references to one or more independent objects(the parts)


# class Library:
#     def __init__(self, name):
#         self.name = name
#         self.books = []

#     def add_book(self, book):
#         self.books.append(book)

#     def list_books(self):
#         return [f"{book.title} by {book.author}"for book in self.books]


# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author


# library = Library("New york public library")
# book1 = Book("harry potter...", "JK Rowling")
# book2 = Book("the Hobbit...", "Bhanu")
# book3 = Book("the color of magic", "terry")

# library.add_book(book1)
# library.add_book(book2)
# library.add_book(book3)

# print(library.name)
# print(library.list_books())

# for book in library.list_books():
#     print(book)

# aggregation - a relationship where one object contains references to other INDEPENDENT objects
#               "has-a" relationship

# composition - the composed object directly owns its components which cannot exist independently
#               "owns-a" relationship

# class Engine:

#     def __init__(self, horse_power):
#         self.horse_power = horse_power


# class Wheel:

#     def __init__(self, size):
#         self.size = size


# class Car:

#     def __init__(self, make, model, horse_power, wheel_size):
#         self.make = make
#         self.model = model
#         self.engine = Engine(horse_power)
#         self.wheels = [Wheel(wheel_size) for wheel in range(4)]

#     def display_car(self):
#         return f" {self.make} {self.model} {self.engine.horse_power}(hp) {self.wheels[0].size}(inch)"


# car = Car("Ford", "mustang", 500, 18)

# print(car.display_car())

# Nested class - A class defined within another class
#                class Outer:
#                   class Inner:

# Benefits - Allows you to logically group classes that are closely related
#            Encapsulation Private details that aren't relevant outside of the outer class
#            keeps the name space clean; reduces the possibility of naming conflicts

# static methods
# class methods
# magic methods
# property decorator